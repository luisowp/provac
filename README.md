# PROVAC — integración y etiquetado

La operación diaria se realiza en la hoja **PROVAC Integración y Etiquetas**. Los documentos originales permanecen en Drive. Esta primera integración contiene un inventario por ID de Drive, cuatro matrices existentes y el lote `conversations-003.json`.

## Uso diario

1. Abra **Archivos** o **Conversaciones** y filtre la columna `Etiquetas sugeridas`.
2. Escriba las etiquetas que decida conservar en `Etiquetas aceptadas` y cambie `Revisión` a `REVISADO`. Esto registra revisión de etiquetas, no validación probatoria.
3. En **Mensajes**, filtre `Autor` por `user` para recuperar declaraciones del usuario; `assistant` identifica respuestas de IA. `Rama actual` distingue el recorrido seleccionado de versiones alternativas.
4. Consulte **Texto** por el ID del mensaje para leerlo completo. Los mensajes mayores de 28,000 caracteres se dividen en fragmentos numerados; se reconstruyen concatenándolos sin separadores.
5. **Matrices** conserva los códigos, tipos, fechas, estatus y campos originales de cada fila. Un código repetido entre matrices se conserva por fuente y fila; no se fusiona automáticamente.

Las etiquetas sugeridas proceden de palabras presentes en el nombre o contenido. No asignan responsabilidad, intención ni una conclusión jurídica. Los códigos encontrados en títulos o conversaciones son menciones, no códigos PROVAC asignados. La fecha de un mensaje no se convierte en fecha del hecho.

## Alcance del primer lote

- Archivos: inventario de la carpeta raíz y sus siete subcarpetas directas. No se ha leído el contenido de todos los archivos.
- Conversaciones: sólo `conversations-003.json`; los lotes 000, 001 y 002 están inventariados y pendientes de integración.
- Matrices: `Provac`, `pilar_provac_maestro`, `Matriz Nodal PROVAC` y `BD Provac`.
- Los archivos con nombres repetidos quedan separados por ID. La coincidencia de nombre no prueba identidad de bytes.
- No se realiza una nueva auditoría del expediente ni validación criptográfica de P7M, FIREL o TSP.
- La hoja es un corte de trabajo. No existe sincronización automática entre Google Drive y GitHub.

## Soporte reproducible opcional

`provac.py` utiliza Python 3.11+ y su biblioteca estándar con SQLite FTS5; no necesita red, claves ni servicios externos. Produce JSON completo, CSV protegidos contra interpretación de texto como fórmulas y una base SQLite con búsqueda de texto.

```bash
python3 provac.py integrar \
  --takeout conversations-003.json \
  --inventario drive_inventory.json \
  --matrices source_matrices.json \
  --salida resultados

python3 provac.py buscar --base resultados/provac.sqlite \
  --texto '"27 de marzo"' --autor user --limite 10
```

El inventario es una lista de metadatos observados: `id`, `title`, `url`, `mime_type`, `parent_id` y `folder_path`. Las matrices son una lista de objetos `id`, `title`, `url`, `text` (CSV leído de la fuente).

Para conservar revisión al regenerar, exporte primero las columnas de etiquetas y revisión como un diccionario JSON de anotaciones indexado por ID. Páselo con `--anotaciones anotaciones.json`:

```json
{
  "ID_DE_REGISTRO": {
    "accepted_tags": "PROVAC | TRAZABILIDAD",
    "review_status": "REVISADO"
  }
}
```

La regeneración reemplaza únicamente la salida derivada indicada. No regenera la hoja nativa ni toma sus cambios automáticamente. Mantenga anotaciones y documentos originales antes de regenerar.

## Verificación

El primer lote fue reconciliado por IDs, autores, ramas, conteos y SHA256 del texto derivado; se comprobó búsqueda SQLite y reconstrucción íntegra de fragmentos. Los hash derivados no certifican firmas judiciales. El repositorio conserva soporte de importación; las conversaciones y documentos privados no se incorporan a su historial.
