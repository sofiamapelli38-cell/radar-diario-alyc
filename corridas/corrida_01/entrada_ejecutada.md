# Entrada ejecutada — RUN-20260906-0802

Instancia resuelta del user prompt versionado. El system prompt se conserva en `prompts/versions/system_prompt_v1.md`.

## Referencias exactas

- System prompt blob: `1ede4c2f029e9b1e7889efcc2b201846530421a6`
- User prompt blob: `6bde4dd7480bb3e903fa36be0f356778846bebf3`
- Configuración: `config/versions/automation_v1.json`

## User prompt resuelto

# User prompt - Ejecución diaria

Ejecutá el Radar Diario ALyC correspondiente a la fecha objetivo `2026-09-05`.

## Pedido puntual

- Considerá exclusivamente publicaciones realizadas entre las 00:00 y las 23:59 de `2026-09-05`, según la zona horaria `America/Argentina/Buenos_Aires`.
- Relevá fuentes oficiales, periodísticas/profesionales y sectoriales definidas en el system prompt.
- Verificá las fechas, eliminá duplicados, buscá respaldo oficial y evaluá la relevancia concreta de cada hallazgo para una ALyC argentina.
- Generá la salida utilizando exactamente la estructura Markdown definida en el system prompt.
- Asigná el identificador de corrida `RUN-20260906-0802`.
- Enviá el reporte terminado mediante Gmail únicamente a la cuenta de Sofía configurada para esta ejecución.
- Usá como asunto: `Radar ALyC | Novedades del 05/09/2026`.
- Si el envío falla, no cambies el destinatario: conservá el reporte y registrá el error en `Estado del envío` y en `Control de calidad`.

No ejecutes acciones derivadas de las novedades. El reporte debe quedar sujeto a revisión y firma de Sofía Mapelli.

## Variables de una corrida real

- `2026-09-05`: fecha analizada en formato AAAA-MM-DD.
- `05/09/2026`: misma fecha en formato DD/MM/AAAA.
- `RUN-20260906-0802`: identificador único con formato RUN-AAAAMMDD-HHMM.

La automatización debe completar estas variables en cada ejecución. Para las corridas entregadas en el repositorio, el archivo de entrada debe conservar los valores utilizados, sin dejar los marcadores sin reemplazar.
