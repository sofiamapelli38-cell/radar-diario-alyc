# Decisiones e historia del proceso

Este documento registra la evolución real del sistema **Radar Diario ALyC**. Se mantiene de forma incremental: las decisiones posteriores no reemplazan ni borran las anteriores.

## Estado al 5 de septiembre de 2026

El contrato inicial, la automatización y la integración con Gmail están configurados. Las tres corridas exigidas todavía no fueron completadas. Por lo tanto, este archivo distingue entre:

- decisiones ya tomadas y verificables;
- problemas observados en la experiencia anterior;
- hipótesis que deberán validarse con las corridas reales.

## DEC-001 - Continuar un caso real iniciado en la Entrega 1

**Fecha:** 05/09/2026  
**Pieza afectada:** contexto y alcance.

### Situación inicial

En la Entrega 1 se trabajó con un agente de seguimiento de novedades regulatorias, impositivas y operativas para una ALyC argentina. La tarea respondía a una necesidad real del área de Impuestos y Contabilidad, pero funcionaba principalmente como un contrato de prompts ejecutado manualmente.

### Decisión

Mantener el problema real y convertirlo en un sistema agéntico completo, con ejecución programada, búsqueda web, envío por Gmail, supervisión definida y evidencia reconstruible.

### Motivo

Partir de una necesidad ya probada permite dedicar el trabajo final a mejorar el sistema, sus controles y su trazabilidad, en lugar de inventar un caso nuevo.

### Resultado esperado

Pasar de un prompt aislado a un flujo diario que utilice herramientas reales y produzca evidencia comparable.

## DEC-002 - Ampliar las fuentes más allá de los organismos oficiales

**Fecha:** 05/09/2026  
**Pieza afectada:** contexto.

### Problema observado

El alcance centrado principalmente en organismos oficiales podía detectar normas y vencimientos, pero dejaba fuera novedades profesionales o competitivas. Por ejemplo, un lanzamiento tecnológico de una ALyC puede ser relevante para el negocio aunque no sea publicado por CNV, ARCA o BCRA.

### Cambio realizado

Se definieron tres grupos de fuentes:

1. oficiales;
2. periodísticas y profesionales;
3. sectoriales, incluyendo publicaciones públicas de ALyCs, mercados y fintechs.

Se incorporaron expresamente Errepar, iProfesional y El Cronista como ejemplos de fuentes profesionales o periodísticas.

### Restricción agregada

Las fuentes periodísticas y sectoriales se consideran señales y no normativa confirmada. Cuando mencionan una norma, el agente debe buscar la publicación oficial.

### Impacto esperado

Obtener un radar más útil para el trabajo diario sin confundir una noticia con una obligación normativa.

## DEC-003 - Reemplazar “últimas 24 horas” por “día calendario anterior”

**Fecha:** 05/09/2026  
**Pieza afectada:** tarea.

### Problema observado

La expresión `últimas 24 horas` depende de la hora exacta en la que se ejecuta la consulta. Si una corrida se retrasa o se adelanta, puede generar solapamientos o dejar publicaciones sin revisar. También dificulta que un tercero reconstruya el período analizado.

### Cambio realizado

Cada ejecución de las 08:00 analiza desde las 00:00 hasta las 23:59 del día calendario anterior en la zona horaria `America/Argentina/Buenos_Aires`.

### Impacto esperado

Que todas las corridas tengan una ventana temporal inequívoca, comparable y reproducible.

## DEC-004 - Incorporar ejecución programada y envío real por Gmail

**Fecha:** 05/09/2026  
**Pieza afectada:** herramientas y tarea.

### Situación inicial

La Entrega 1 requería que Sofía iniciara manualmente cada relevamiento y guardara la respuesta.

### Cambio realizado

Se configuró una automatización diaria a las 08:00, hora argentina, y se conectó Gmail para enviar el reporte únicamente a la cuenta validada de Sofía.

### Control de privacidad

La dirección completa y las credenciales no se publican en el repositorio. El contrato identifica a la destinataria por su rol y la configuración privada conserva el dato operativo.

### Evidencia pendiente

La primera ejecución real y el primer email deberán guardarse en `corridas/corrida_01/`. Hasta que eso ocurra, no se declara validado el envío de punta a punta.

## DEC-005 - Separar automatización de decisión profesional

**Fecha:** 05/09/2026  
**Pieza afectada:** restricciones y gobierno.

### Riesgo identificado

Un resumen generado automáticamente puede equivocarse en la aplicabilidad de una norma, un vencimiento o una acción recomendada. También podría reenviarse fuera de contexto.

### Cambio realizado

- **L3:** el agente busca, filtra, clasifica, redacta y envía el informe a Sofía para revisión posterior.
- **L1:** las interpretaciones, prioridades y acciones sugeridas son recomendaciones preliminares.
- **L0:** Sofía conserva las decisiones, presentaciones, registraciones, cambios operativos y comunicaciones a terceros.

### Responsable final

Sofía Mapelli revisa y firma cualquier uso profesional del reporte. El email automático es informativo y no constituye una instrucción para actuar.

## DEC-006 - Fijar un formato estricto y comparable

**Fecha:** 05/09/2026  
**Pieza afectada:** formato.

### Problema observado

Una salida narrativa puede resultar clara para leer, pero dificulta comparar corridas y detectar si faltan datos esenciales.

### Cambio realizado

Se definieron cinco secciones obligatorias y una tabla con columnas fijas. La salida incluye datos de la corrida, resumen ejecutivo, novedades, control de calidad y supervisión humana.

También se estableció que una corrida sin novedades debe conservar toda la estructura y no inventar contenido para completar la tabla.

### Impacto esperado

Permitir la comparación entre días y facilitar la corrección automática del repositorio.

## DEC-007 - Incorporar controles contra errores de búsqueda y clasificación

**Fecha:** 05/09/2026  
**Pieza afectada:** restricciones.

### Riesgos identificados

- confundir la fecha de una noticia con la fecha de una norma citada;
- presentar una nota periodística como confirmación oficial;
- duplicar el mismo hecho publicado por varios medios;
- incluir una publicación sin fecha verificable;
- completar el reporte con noticias generales sin relevancia concreta.

### Controles incorporados

- verificación de la fecha de publicación;
- prioridad para el enlace original y oficial;
- estados de validación explícitos;
- consolidación de duplicados;
- sección obligatoria de control de calidad;
- exclusión de información cuya relevancia no pueda explicarse.

## Plan de calibración con las corridas reales

Después de cada ejecución se registrará:

| Corrida | Qué se controlará | Estado |
|---|---|---|
| 01 | Cobertura, respeto de fecha, enlaces, formato y envío | Pendiente |
| 02 | Corrección de la primera falla textual mediante un solo cambio | Pendiente |
| 03 | Efecto de la segunda iteración y estabilidad del formato | Pendiente |

Para cada iteración se conservarán el texto que falló, la pieza del contrato modificada y el efecto observable en la corrida siguiente. No se describirá una mejora como `quedó mejor` sin señalar evidencia concreta.

## Decisiones todavía pendientes

- Medir tokens de entrada y salida de las corridas reales.
- Confirmar el modelo utilizado y su tarifa vigente al momento del cálculo.
- Calcular costo por corrida, semanal y anual.
- Registrar fallas reales de acceso, búsqueda o envío.
- Completar la matriz final de riesgos con evidencia de las tres ejecuciones.
