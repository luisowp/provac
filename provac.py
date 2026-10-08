#!/usr/bin/env python3
"""Integración local de PROVAC. Python estándar; sin red ni claves de API."""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import pathlib
import re
import sqlite3
import unicodedata

RULES = {
    'PROVAC': ['provac', 'autocita'],
    'PILAR': ['pilar method', 'pilar-method', 'pilar_method'],
    'AMPARO': ['amparo', '334/2026', '334-2026'],
    'FAMILIAR': ['01259/2025', '1259/2025', 'convivencia', 'patria potestad'],
    'TRAZABILIDAD': ['p7m', 'tsp', 'neun', 'hash', 'firma electronica'],
    'NOTIFICACION': ['notificacion', 'actuaria'],
    'CAUTELAR': ['suspension', 'cautelar', 'medidas provisionales'],
    'NULIDAD': ['nulidad'],
    'OMISION': ['omision', 'no resuelto', 'sin respuesta'],
    'MARCO_JURIDICO': ['jurisprudencia', 'convencion', 'ley de amparo'],
    'INFRAESTRUCTURA': ['github', 'google drive', 'notebooklm', 'json', 'repositorio'],
}
CODE = re.compile(r'\b(?:AC|HF|EVD|OM|DIF|DOC|DEC|EX|IN|MF|P|NUL|VIA|DIG|PATRON|COM|RP)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b')

def norm(value):
    return ''.join(c for c in unicodedata.normalize('NFD', str(value).lower()) if unicodedata.category(c) != 'Mn')

def suggest(value):
    text = norm(value)
    return [label for label, terms in RULES.items() if any(t in text for t in terms)]

def sha(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def iso(value):
    if value is None:
        return ''
    try:
        return dt.datetime.fromtimestamp(float(value), dt.timezone.utc).isoformat()
    except (ValueError, TypeError, OverflowError):
        return str(value)

def current_path(conv):
    mapping, seen = conv.get('mapping', {}), set()
    key = conv.get('current_node')
    while key and key in mapping and key not in seen:
        seen.add(key)
        key = mapping[key].get('parent')
    return seen

def safe_csv(value):
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=False)
    if isinstance(value, str) and value.lstrip().startswith(('=', '+', '-', '@')):
        return "'" + value
    return value

def build(takeout, inventory, matrices, annotations=None):
    if not isinstance(takeout, list):
        raise ValueError('El takeout debe ser una lista de conversaciones')
    annotations = annotations or {}
    files, conversations, messages, matrix_rows = [], [], [], []
    by_name = collections.Counter(f['title'] for f in inventory)
    for f in inventory:
        code = CODE.findall(f['title'].upper())
        files.append(dict(id=f['id'], title=f['title'], parent_id=f.get('parent_id'),
            folder_path=f.get('folder_path'), mime_type=f.get('mime_type'), size=f.get('size'),
            url=f.get('url'), codes_in_name=code, suggested_tags=suggest(f['title']),
            accepted_tags='', review_status='PENDIENTE',
            same_name_count=by_name[f['title']], content_status='SOLO_METADATOS'))
    for source in matrices:
        for index, row in enumerate(csv.DictReader(io.StringIO(source['text'])), 2):
            row = {k:v for k,v in row.items() if k}
            code = row.get('Codigo_PROVAC') or row.get('PROVAC') or ''
            desc = row.get('Descripcion_Sintesis') or row.get('Descripcion_Contenido') or row.get('CITA_TEXTO') or row.get('Incidencia Detectada') or ''
            matrix_rows.append(dict(id=f"{source['id']}:row:{index}", source_id=source['id'],
                source_title=source['title'], source_url=source['url'], row=index,
                existing_code=code, existing_node=row.get('ID_Nodo',''),
                record_type=row.get('Tipo_Nodo') or row.get('TIPO') or '',
                date_original=row.get('Fecha_Evento') or row.get('FECHA') or '',
                description=desc, source_status=row.get('Estatus_Depuracion',''),
                original=row, suggested_tags=suggest(json.dumps(row, ensure_ascii=False)),
                accepted_tags='', review_status='PENDIENTE'))
        for f in files:
            if f['id'] == source['id']:
                f['content_status'] = 'MATRIZ_IMPORTADA'
    code_counts = collections.Counter(r['existing_code'] for r in matrix_rows if r['existing_code'])
    for row in matrix_rows:
        row['code_occurrences'] = code_counts[row['existing_code']] if row['existing_code'] else 0
    ids = set()
    for conv in takeout:
        cid = conv.get('conversation_id') or conv.get('id')
        if not cid or cid in ids:
            raise ValueError('ID de conversación ausente o repetido')
        ids.add(cid)
        title, mapping, active = conv.get('title',''), conv.get('mapping',{}), current_path(conv)
        records = []
        for node_id, node in mapping.items():
            m = node.get('message')
            if not m:
                continue
            content = m.get('content') or {}
            parts = content.get('parts') or []
            text = '\n'.join(p for p in parts if isinstance(p, str))
            role = (m.get('author') or {}).get('role', 'unknown')
            rec = dict(id=f'{cid}:{node_id}', conversation_id=cid, conversation_title=title,
                node_id=node_id, message_id=m.get('id'), parent_id=node.get('parent'),
                role=role, create_time=iso(m.get('create_time')), on_current_path=node_id in active,
                text=text, original_content=content, text_sha256=sha(text),
                suggested_tags=suggest(text), accepted_tags='', review_status='PENDIENTE',
                codes_mentioned=sorted(set(CODE.findall(text.upper()))),
                source_pointer=f'conversations-003.json::conversation={cid}::mapping={node_id}::message',
                conversation_url=f'https://chatgpt.com/c/{cid}')
            messages.append(rec)
            records.append(rec)
        role_counts = collections.Counter(r['role'] for r in records)
        conversations.append(dict(id=cid, title=title, create_time=iso(conv.get('create_time')),
            update_time=iso(conv.get('update_time')), message_count=len(records),
            user_messages=role_counts['user'], assistant_messages=role_counts['assistant'],
            current_path_messages=sum(r['on_current_path'] for r in records),
            suggested_tags=sorted(set(suggest(title)+[t for r in records for t in r['suggested_tags']])),
            accepted_tags='', review_status='PENDIENTE', conversation_url=f'https://chatgpt.com/c/{cid}'))
    hashes = collections.Counter(r['text_sha256'] for r in messages if r['text'])
    for row in messages:
        row['same_text_count'] = hashes[row['text_sha256']] if row['text'] else 0
    for rows in (files, conversations, messages, matrix_rows):
        for row in rows:
            if row['id'] in annotations:
                a = annotations[row['id']]
                row['accepted_tags'] = a.get('accepted_tags', '')
                row['review_status'] = a.get('review_status', 'PENDIENTE')
    return dict(schema_version='1.0', generated_at=dt.datetime.now(dt.timezone.utc).isoformat(),
        scope='Primer lote: metadatos Drive, cuatro matrices y conversations-003.json.',
        rules={'tags':'Sugerencias temáticas por coincidencia de palabras; no califican hechos ni valor probatorio.',
            'codes':'Códigos existentes y menciones se conservan; no se asignan códigos canónicos nuevos.',
            'hash':'SHA256 de texto derivado o archivo importado; no valida P7M, FIREL, TSP ni firma judicial.',
            'branches':'Se conservan todas las ramas. on_current_path distingue el diálogo seleccionado.',
            'dates':'create_time corresponde al mensaje UTC, no a la fecha del hecho relatado.',
            'duplicates':'Nombres repetidos y textos idénticos se señalan sin eliminar fuentes.'},
        files=files, conversations=conversations, messages=messages, matrix_rows=matrix_rows)

def write_bundle(data, out):
    out.mkdir(parents=True, exist_ok=True)
    (out/'base_provac.json').write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    for key in ('files','conversations','messages','matrix_rows'):
        rows = data[key]
        with (out/f'{key}.csv').open('w', newline='', encoding='utf-8-sig') as f:
            if rows:
                fields=[k for k in rows[0] if k not in ('original_content',)]
                writer=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
                writer.writeheader()
                writer.writerows({k:safe_csv(r.get(k)) for k in fields} for r in rows)
    db = out/'provac.sqlite'
    # Construir en memoria evita depender de journal/locking de carpetas sincronizadas.
    with sqlite3.connect(':memory:') as conn:
        conn.execute('CREATE TABLE records (kind TEXT, id TEXT, title TEXT, role TEXT, tags TEXT, accepted_tags TEXT, review_status TEXT, payload TEXT, PRIMARY KEY(kind,id))')
        conn.execute('CREATE VIRTUAL TABLE search USING fts5(kind UNINDEXED, id UNINDEXED, title, text)')
        for kind in ('files','conversations','messages','matrix_rows'):
            for r in data[kind]:
                title=r.get('title') or r.get('conversation_title') or r.get('source_title') or ''
                text=r.get('text') or r.get('description') or ''
                conn.execute('INSERT INTO records VALUES (?,?,?,?,?,?,?,?)', (kind,r['id'],title,r.get('role',''),' | '.join(r['suggested_tags']),r['accepted_tags'],r['review_status'],json.dumps(r,ensure_ascii=False)))
                conn.execute('INSERT INTO search VALUES (?,?,?,?)', (kind,r['id'],title,text))
        conn.commit()
        db.write_bytes(conn.serialize())
    counts={k:len(data[k]) for k in ('files','conversations','messages','matrix_rows')}
    (out/'control.json').write_text(json.dumps(counts,indent=2), encoding='utf-8')
    return counts

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command', required=True)
    imp=sub.add_parser('integrar')
    imp.add_argument('--takeout',type=pathlib.Path,required=True)
    imp.add_argument('--inventario',type=pathlib.Path,required=True)
    imp.add_argument('--matrices',type=pathlib.Path,required=True)
    imp.add_argument('--anotaciones',type=pathlib.Path)
    imp.add_argument('--salida',type=pathlib.Path,required=True)
    find=sub.add_parser('buscar')
    find.add_argument('--base',type=pathlib.Path,required=True)
    find.add_argument('--texto',required=True)
    find.add_argument('--autor',choices=['user','assistant'])
    find.add_argument('--limite',type=int,default=10)
    a=p.parse_args()
    if a.command=='integrar':
        annotations=json.loads(a.anotaciones.read_text()) if a.anotaciones else None
        data=build(json.loads(a.takeout.read_text()),json.loads(a.inventario.read_text()),json.loads(a.matrices.read_text()),annotations)
        data['takeout_sha256']=hashlib.sha256(a.takeout.read_bytes()).hexdigest()
        print(json.dumps(write_bundle(data,a.salida)))
    else:
        with sqlite3.connect(':memory:') as conn:
            conn.deserialize(a.base.read_bytes())
            query='SELECT r.kind,r.id,r.title,r.role,snippet(search,3,"[","]","…",30) FROM search JOIN records r ON r.id=search.id AND r.kind=search.kind WHERE search MATCH ?'
            params=[a.texto]
            if a.autor:
                query+=' AND r.role=?'
                params.append(a.autor)
            query+=' LIMIT ?'
            params.append(max(1,min(a.limite,100)))
            for r in conn.execute(query,params):
                print(json.dumps(dict(zip(('tipo','id','titulo','autor','extracto'),r)),ensure_ascii=False))

if __name__=='__main__':
    main()
