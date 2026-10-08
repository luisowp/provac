# Mapa preliminar por temas y nodos — 1 de octubre de 2026

**Entregable principal:** `mapa_tematico_nodos_conversaciones.xlsx`. Contiene 28 fichas de nodos conservando sus identificadores, 176 conversaciones candidatas clasificadas en varios temas y una hoja de marco jurídico/control. Se apartaron 62 entradas del índice preliminar por no registrar suficientes señales temáticas en mensajes del usuario o por ser ajenas al caso. **Apartar no equivale a borrar los archivos originales ni el índice histórico.** La asociación automática de una conversación con un nodo es una pista de búsqueda, no corroboración de lo que ahí se dijo.

## Cómo usarlo

- **Nodos y conexiones:** una fila por ficha; columnas de fecha, afirmación del mapa, anclas, conversaciones candidatas, temas, referencia jurídica y cotejo pendiente. Se conservan tres fichas sin ID previo; no se renumeran.
- **Conversaciones por tema:** filtrar la columna TEMAS; una misma conversación puede aparecer asociada a varios temas. Solo se computan mensajes del usuario en ChatGPT y fragmentos `REQUEST` en DeepSeek; las respuestas o razonamientos del modelo no acreditan hechos.
- **Marco y control:** referencias normativas y jurisprudenciales para estudiar, separadas de los documentos probatorios. La clasificación es preliminar y los resúmenes repetidos entre chats pueden multiplicar menciones de un mismo dato.

## Ejemplo de lectura integrada: demanda federal y posible problema de encauce

**NODO-08 — demanda federal, 13 de abril.** El mapa reporta folio `12341272/2026`, OCC `20260874032100030/2026`, archivo `.p7m` terminado en `57992839` y TSP `140024533`. El reporte de anomalías adjunto también ubica una firma de la demanda en la p. 19 del principal, **pero aquí no tenemos el archivo criptográfico original para validarlo**. El memorando aportado repite el folio en sus pp. 74, 237 y 256: es corroboración *entre relatos secundarios*, no tres pruebas independientes. Pregunta verificable: ¿coinciden el documento presentado, el acuse OCC, la firma, el registro de turno y la demanda que efectivamente llegó al juzgado?

**NODO-10 — solicitud de vinculación del 19 de abril.** El mapa indica folio `12374768/2026`, referencia al amparo `334/2026-4A` y posible tránsito OCC → Sexto/«Varios 100/2026» → Quinto. Esto **no demuestra por sí mismo radicación indebida**: es indispensable distinguir entre *turno original de la demanda*, *registro de una promoción posterior*, *remisión administrativa*, *radicación judicial*, *admisión* y *vinculación de usuario al expediente electrónico*. Cotejar el acuse, historial de eventos del portal, constancia de turno y acuerdos firmados; comparar órgano destinatario y momento de cada actuación.

**NODO-16 — aviso del 19 de mayo.** El mapa consigna folio `15998431/2026` y redirección a «Varios 1/2026». Puede ser una segunda incidencia de encauce, pero no debe fusionarse con el evento de abril ni con las variantes «1/2025» que el propio mapa advierte. Cotejar aviso, contenido de la promoción, su destino efectivo y si el cuaderno de suspensión la recibió oportunamente.

**Hipótesis de trabajo (no conclusión):** si una promoción identificaba el expediente correcto y fue dirigida a otro registro de forma que retrasó el conocimiento o el examen cautelar, ello podría ser relevante para tutela judicial efectiva. La secuencia exacta y el efecto concreto necesitan documentos primarios y contexto de las reglas de turno aplicables. Una discrepancia de etiquetas informáticas aislada no acredita mala fe, nulidad ni afectación procesal.

## Marco jurídico para contrastar, no para sustituir hechos

- La [Ley de Amparo, arts. 79, 108, 112–115 y 125–128](https://www.diputados.gob.mx/LeyesBiblio/pdf/LAmp.pdf) ofrece puntos de control sobre suplencia, contenido y trámite inicial de la demanda y suspensión; verificar versión vigente **en la fecha de cada acto** y supuesto concreto antes de citarla en un escrito. [1](https://www.diputados.gob.mx/LeyesBiblio/pdf/LAmp.pdf)
- La tesis SJF **2024924** se refiere a suplencia y protección de niñas, niños y adolescentes en juzgados familiares; **no** resuelve por sí sola el turno electrónico de una demanda federal. [1](https://sjf2.scjn.gob.mx/detalle/tesis/2024924)
- La tesis SJF **2025562** describe la exhaustividad cualitativa frente a las cuestiones efectivamente planteadas, y advierte que la cita genérica de normas no exige contestación artículo por artículo. Sirve para delimitar núcleos de respuesta, no para afirmar automáticamente una omisión. [1](https://sjf2.scjn.gob.mx/detalle/tesis/2025562)
- **Pendiente específico:** localizar el acuerdo administrativo de OCC/turno efectivamente vigente para el circuito y fechas del caso, así como criterio jurisprudencial directamente aplicable a la incidencia concreta de vinculación electrónica. No se inventa una tesis sobre «radicación indebida».

## Alertas del memorando aportado

El PDF `Memorando de inteligencia jurídica.pdf` (302 páginas) contiene valoraciones y lenguaje categórico, incluso imputaciones graves y afirmaciones clínicas sobre personas. Es **fuente secundaria de hipótesis**, no dictamen ni prueba de corrupción, diagnóstico o autenticidad digital. En su p. 237 habla de un principal de 1,067 páginas y de incidente «no localizado»; el reporte de anomalías aportado habla de principal de **1,069 páginas** y dice haber revisado un expediente incidental. Esa divergencia debe resolverse con identificación de versión, fecha de descarga y archivos originales, no mediante conciliación narrativa. Evitar reproducir datos personales o diagnósticos de menores sin necesidad.

**Siguiente comprobación prioritaria:** aportar acuse OCC y demanda originales del 13 de abril, el escrito y acuse del 19 de abril, aviso y promoción del 19 de mayo, y los autos de turno/remisión. Con ello las columnas de estado probatorio pueden cambiar de «referido» a «cotejado», siempre dejando registro de la fuente exacta.

## Integración posterior: tutela y vista de marzo

Se agregaron **dos hojas** al libro: «Tutela nueva - no fusionar» (15 nodos del JSON `nodos_tutela_334_2026.json`) y «Documento marzo - cotejo» (8 referencias por página del PDF `Vista 19 de Marzo Adicion, Contexto y Finalidad.docx.pdf`). Las relaciones con NODO-00, NODO-05, NODO-07, NODO-13, NODO-15 y otros son **sugerencias temáticas**, no identidad de hechos ni prueba de promoción. Se mantienen separados los ID `N-`/`S-`/`CTX-` de los ID del mapa anterior.

**Precauciones de fecha y fuente:** el PDF menciona comparecencia/notificación del 19 de marzo en p. 2, pero termina fechado **24 de marzo de 2026** en p. 7. No acredita por sí mismo cuándo fue presentado, firmado o recibido. Se requiere acuse y versión incorporada al expediente. Su petición de oficio escolar (p. 3), convivencia provisional (p. 4) e intervención DIF (p. 5) no prueban que se hayan acordado. Las aseveraciones sobre personas y posible riesgo son alegaciones a contrastar.

El JSON de tutela se describe como **compilación para una queja o promoción**, no auditoría. Sus estados «ACTIVO», cálculos de oportunidad y referencias de tesis son estados internos del borrador; no certifican procedencia ni vigencia. En particular, antes de usar su planteamiento sobre el artículo 98-II de la Ley de Amparo y la tesis registro 2019798 deben cotejarse la hipótesis procesal exacta, notificaciones y textos oficiales. No se fusiona la omisión de tramitar una demanda con una falta de respuesta a promoción cautelar posterior.
