# Concentración de piezas — nulidad federal del 27 de junio de 2026

**Nodo vinculado:** `NODO-NULIDAD-27JUN`. Esta es una **ficha de organización**; incorpora literalmente identificadores, fuentes y relaciones. **No convalida** el acto, no declara procedencia de nulidad y no atribuye intención a nadie. Este evento federal es distinto del incidente local del 24 de marzo.

## Tres piezas recibidas y vínculo objetivo

| Pieza | Lo que dice | Identificador de enlace |
|---|---|---|
| `27 junio nulidad Folio 16455181-2026 - AcusePromocion.pdf`, p. 1 | Acuse de envío el **27/06/2026 a las 03:45, tiempo del centro**, al Juzgado Quinto de Distrito; asunto **Amparo Indirecto 334/2025**; archivo denominado «27 de Junio Incidente de Nulidad de Notificaciones.pdf» (2,512,349 bytes). | **Folio `16455181/2026`**. |
| `Nulidad NEUN Ageno Aviso de Cambio.pdf`, p. 1 | Aviso: promoción originalmente asociada a **334/2025** y redirigida por personal del órgano jurisdiccional a **334/2026**, ambos como Amparo Indirecto. | Mismo folio **`16455181/2026`**. El aviso aportado no indica fecha/hora del cambio. |
| `Incidente Nulidad 02650000386542110109800107550015.md` | Texto que se presenta como incidente de nulidad de una notificación del **15/05/2026** en el cuaderno incidental (menciona p. 25 y la referencia a LFT, art. 745 Ter); repite **NEUN `41504452`** y expediente **334/2026**. | El número `02650000386542110109800107550015` aparece en el nombre de archivo y URL inicial: **nombre de descarga/representación institucional**, distinto de la firma `.p7m` nativa; su bloque `38654211` ocupa en el benchmarking aportado la posición donde otros nombres muestran `41504452` (hipótesis, no NEUN oficialmente confirmado). Posteriormente se aportó un PDF legible de 14 páginas asociado al identificador de descarga; su tamaño difiere del archivo descrito en el acuse (véase actualización al final). |

## Mantener separados los identificadores

- **334/2025** = número de expediente asentado en el **acuse**; **334/2026** = destino que declara el **aviso**. Esa discrepancia y su redirección constituyen el hecho documental que debe rastrearse. El acuse no se reescribe retroactivamente.
- **`41504452`** = NEUN que aparece en el **texto del incidente aportado**. Los dos PDF de una página recibidos **no muestran un campo NEUN**: de ellos no se deduce cuál era el NEUN vinculado a 334/2025, ni puede afirmarse todavía que se asignó «NEUN ajeno». Mantenerlo como pregunta de trazabilidad.
- **`16455181/2026`** = folio de la **promoción del 27 de junio**; sirve para enlazar acuse y aviso, no equivale al expediente ni al NEUN.
- **`02650000386542110109800107550015`** = identificador del archivo transcrito; no es el `.p7m` de demanda ni el número de expediente.
- **Ceros significativos:** en otra sección del reporte (1) consta `0265002000000000058298083.p7m` (**25 dígitos**), frente a `02650020000000000058298083.p7m` (**26 dígitos**) del reporte anterior. **No son cadenas idénticas**, aunque parezcan referirse a una pieza cercana. No se normalizan ni se les agrega/quita un cero. Tampoco se atribuyen automáticamente al incidente del 27 de junio.

## Preguntas que quedan abiertas, sin adelantar conclusión

1. ¿Qué dato del portal o formulario produjo la asociación inicial a **334/2025** y cuál fue el historial técnico de redirección a **334/2026**?
2. ¿Qué **NEUN** correspondía a cada registro en el sistema, antes y después del cambio? Se necesita pantalla/certificación del expediente o bitácora; el aviso no ofrece ese dato.
3. ¿Cuándo se practicó la redirección, dónde quedó incorporado el escrito, y en qué cuaderno se proveyó? ¿Se preservaron firma, anexos y fecha original de presentación?
4. ¿Coincide íntegramente el PDF enviado de 2,512,349 bytes con la transcripción Markdown? ¿Qué dice exactamente la constancia incidental de notificación en p. 25?

## Nueva pieza incorporada: PDF de 14 páginas

Se recibió `html_02650000386542110109800107550015.pdf` (14 páginas; **2,547,709 bytes**; SHA-256 `f00e6239f636165ec317b511f0e9f185708a112e7e676bc186cf765b82816e16`). Las pp. 1–13 contienen el texto del incidente —por tanto ya no dependemos solo de la transcripción `.md` para leerlo— y repiten en encabezados **NEUN `41504452` / expediente `334/2026`**. Son datos impresos en el *escrito*, no una certificación de la asociación del sistema al expediente inicialmente señalado como `334/2025`.

La **p. 14** presenta una hoja de «Evidencia criptográfica - transacción» que consigna *otro identificador diferente*: archivo firmado `02650020000000000060532616.p7m`; firmante declarado Luis Alberto Carvajal Durán; fecha indicada **27/06/26 03:44:52 CDMX**; respuesta TSP `173741864` a las **03:44:53 CDMX**. Se registra exactamente como dato visible de la hoja, sin verificar criptográficamente el `.p7m` original.

**Diferencia material a preservar:** el acuse anterior describe un PDF enviado de **2,512,349 bytes**; el nuevo `html_...pdf` pesa **2,547,709 bytes** (35,360 bytes más). No se afirma que ambos archivos sean binariamente iguales ni que el PDF extraído sea exactamente el adjunto recibido por el juzgado; la hoja de evidencia adicional u otra transformación podrían influir, pero eso requiere cotejo. El aviso de cambio vuelto a adjuntar tiene SHA-256 `85e8f32b13f1249b1e31d592c64874cd47f7e9ec3c2ee144160c9ee1c3db3055`.

**Estado del nodo:** se cuenta ahora con PDF legible del incidente y hoja de evidencia visible, además de acuse y aviso enlazados por folio; **siguen pendientes** la comparación con el PDF original de 2,512,349 bytes, el campo NEUN real de cada registro en el sistema, la causa de la asociación inicial, el momento del cambio y la actuación judicial posterior.

## Rectificación de clasificación: promoción nativa frente a nombre institucional

**Corrección del usuario:** en sus promociones **nativas** no aparece el NEUN incorporado a su identificador. Los ejemplos a la vista son `08740010000000000057992839.p7m` (demanda) y `02650020000000000060532616.p7m` (hoja de evidencia de esta nulidad): ninguno contiene literalmente `41504452`. Se registra la afirmación de alcance general como **declaración del usuario pendiente de inventario exhaustivo**, no como regla técnica ya certificada.

El nombre de **descarga/representación institucional** `02650000386542110109800107550015.pdf` es de otra clase de objeto que el `.p7m` nativo. La nota de benchmarking aportada segmenta el nombre como `0265 | 0000 | 38654211 | 010980 | 010755 | 0015`, frente al patrón comparativo `0265 | 0000 | 41504452 | …`. La posición de ocho dígitos constituye una **hipótesis estructural fundada en comparación de nombres**, no una especificación oficial del sistema ni prueba por sí sola de asignación de NEUN `38654211` a una persona o expediente. El texto del PDF, en cambio, imprime `NEUN: 41504452` en el encabezado. Conservar ambos datos sin reducir uno al otro.

Así, **«falta de NEUN en la promoción nativa» y «bloque discordante en el nombre institucional» son fenómenos distintos**: lo primero no demuestra por sí solo fallo de asociación interna; lo segundo justifica solicitar la correspondencia certificada entre archivo original, registro SISE, ruta de descarga, folio y NEUN. No se llama «NEUN ajeno confirmado» hasta obtener el diccionario/bitácora correspondiente. Los textos `benchmarking matem tico serio de la nomenclatura-neun-ageno.md`, `factura-metafora-neun.md`, `prompt-normativo-neun.md` y `S   Faltaba un   bloque t cnico-normativo separado.txt` se incorporan como **análisis y propuestas de argumentación**, no como fuentes institucionales ni normas verificadas.

## Pieza posterior: AC-023 (transcripción Markdown, 23 de julio)

`AC-023 File name [0265000041504452023.pdf].md` se incorpora como **transcripción aportada de un acuerdo/audiencia incidental**, no como PDF original verificado. Se relaciona con la notificación electrónica del auto de 13 de mayo, reportada como practicada el 15 de mayo; el texto dice que el incidente de nulidad se recibió **29 de junio**, se admitió el **30 de junio**, se fijó audiencia el **10 de julio** y se celebró/resolvió el **23 de julio**. En el resultando II figura, en cambio, «se admitió ... el **13 de junio**»: conservar esa discordancia sin corregirla. El acuse aportado documenta **envío el 27 de junio a las 03:45** (folio `16455181/2026`); envío y recepción asentada por el juzgado pueden ser eventos distintos y requieren bitácora para enlazarlos.

La transcripción atribuye a la resolución el razonamiento de que una **promoción del 19 de mayo en el incidente** fue la siguiente comparecencia posterior a la notificación del 15 de mayo, y que la nulidad promovida en junio no satisfizo el artículo 68 de la Ley de Amparo. Registra una diferencia terminológica interna: en el análisis se declara **«improcedente»**, mientras el resolutivo dice **«infundado»**. También cita la tesis registro **811075** y la jurisprudencia **P./J. 4/2018 (10a.), registro 2015994**, cuya hipótesis textual se refiere a notificación por lista de sentencia de **amparo directo**; anotar su cita no equivale a afirmar aplicabilidad automática al aviso electrónico incidental aquí discutido.

El texto transcrito **no menciona `16455181` ni `38654211`** y tampoco reproduce expresamente la frase «745 Ter» que el escrito de nulidad señala como objeto de su crítica. Esta ausencia en la transcripción no prueba por sí sola omisión de estudio: hace falta comparar el PDF firmado completo, el incidente presentado, las pruebas y los argumentos efectivamente sometidos. La hoja criptográfica que la transcripción reproduce señala `161582744_0265000041504452023.p7m`, dos firmantes y horas del 23 de julio; se registra como **dato transcrito**, pendiente del PDF/archivo original.

**Nuevo enlace temático:** `NODO-NULIDAD-27JUN` ↔ `NODO-16` / `NODO-19MAY` (promoción incidental del 19 de mayo identificada por el juzgado), sin fusionar promoción, notificación y decisión. El escrito del 27 de junio y el fallo narrado en AC-023 son piezas distintas de la misma secuencia.
