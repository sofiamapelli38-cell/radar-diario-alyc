# Entrada ejecutada — RUN-20260907-0805

Instancia resuelta del user prompt versionado. El system prompt se conserva en `prompts/versions/system_prompt_v2.md`.

## Referencias exactas

- System prompt blob: `8cf03bb08ff893f9d6e7a6d5d4fda147a7d3b35f`
- User prompt blob: `643f42c85cadefac2a99b4bc0d91905d17e3bf29`
- Configuración: `config/versions/automation_v2.json`

## User prompt resuelto

# User prompt - Ejecución diaria

Ejecutá el Radar Diario ALyC correspondiente a la fecha objetivo `2026-09-06`.

## Pedido puntual

- Considerá exclusivamente publicaciones realizadas entre las 00:00 y las 23:59 de `2026-09-06`, según la zona horaria `America/Argentina/Buenos_Aires`.
- Relevá fuentes oficiales, periodísticas/profesionales y sectoriales definidas en el system prompt.
- Verificá las fechas, eliminá duplicados, buscá respaldo oficial y evaluá la relevancia concreta de cada hallazgo para una ALyC argentina.
- Generá la salida utilizando exactamente la estructura HTML definida en el system prompt.
- Asigná el identificador de corrida `RUN-20260907-0805`.
- Enviá el reporte terminado mediante Gmail únicamente a la cuenta de Sofía configurada para esta ejecución.
- Usá como asunto: `Radar ALyC | Novedades del {{FECHA_OBJETIVO_DDMMYYYY}}`.
- Si el envío falla, no cambies el destinatario: conservá el reporte y registrá el error en `Estado del envío` y en `Control de calidad`.

No ejecutes acciones derivadas de las novedades. El reporte debe quedar sujeto a revisión y firma de Sofía Mapelli.

## Variables de una corrida real

- `2026-09-06`: fecha analizada en formato AAAA-MM-DD.
- `{{FECHA_OBJETIVO_DDMMYYYY}}`: misma fecha en formato DD/MM/AAAA.
- `RUN-20260907-0805`: identificador único con formato RUN-AAAAMMDD-HHMM.

La automatización debe completar estas variables en cada ejecución. Para las corridas entregadas en el repositorio, el archivo de entrada debe conservar los valores utilizados, sin dejar los marcadores sin reemplazar.
