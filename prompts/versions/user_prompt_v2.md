# User prompt - Ejecución diaria

Ejecutá el Radar Diario ALyC correspondiente a la fecha objetivo `{{FECHA_OBJETIVO}}`.

## Pedido puntual

- Considerá exclusivamente publicaciones realizadas entre las 00:00 y las 23:59 de `{{FECHA_OBJETIVO}}`, según la zona horaria `America/Argentina/Buenos_Aires`.
- Relevá fuentes oficiales, periodísticas/profesionales y sectoriales definidas en el system prompt.
- Verificá las fechas, eliminá duplicados, buscá respaldo oficial y evaluá la relevancia concreta de cada hallazgo para una ALyC argentina.
- Generá la salida utilizando exactamente la estructura HTML definida en el system prompt.
- Asigná el identificador de corrida `{{RUN_ID}}`.
- Enviá el reporte terminado mediante Gmail únicamente a la cuenta de Sofía configurada para esta ejecución.
- Usá como asunto: `Radar ALyC | Novedades del {{FECHA_OBJETIVO_DDMMYYYY}}`.
- Si el envío falla, no cambies el destinatario: conservá el reporte y registrá el error en `Estado del envío` y en `Control de calidad`.

No ejecutes acciones derivadas de las novedades. El reporte debe quedar sujeto a revisión y firma de Sofía Mapelli.

## Variables de una corrida real

- `{{FECHA_OBJETIVO}}`: fecha analizada en formato AAAA-MM-DD.
- `{{FECHA_OBJETIVO_DDMMYYYY}}`: misma fecha en formato DD/MM/AAAA.
- `{{RUN_ID}}`: identificador único con formato RUN-AAAAMMDD-HHMM.

La automatización debe completar estas variables en cada ejecución. Para las corridas entregadas en el repositorio, el archivo de entrada debe conservar los valores utilizados, sin dejar los marcadores sin reemplazar.
