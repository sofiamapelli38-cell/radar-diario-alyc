# Entrada ejecutada — RUN-20260908-0758

Instancia resuelta del user prompt versionado. El system prompt se conserva en `prompts/versions/system_prompt_v3.md`.

## Referencias exactas

- System prompt blob: `a97a7b742b25296425a91cb7f9c0871734911fdb`
- User prompt blob: `766df7ff888e3c3ea14ef2e3df5d172473e84527`
- Configuración: `config/versions/automation_v3.json`

## User prompt resuelto

# User prompt - Ejecución diaria

Ejecutá el Radar Diario ALyC correspondiente a la fecha objetivo `2026-09-07`.

## Pedido puntual

- Considerá exclusivamente publicaciones realizadas entre las 00:00 y las 23:59 de `2026-09-07`, según la zona horaria `America/Argentina/Buenos_Aires`.
- Relevá fuentes oficiales, periodísticas/profesionales y sectoriales definidas en el system prompt.
- Verificá fechas, eliminá duplicados y buscá respaldo oficial.
- Aplicá un máximo de cinco hallazgos, excluí contenido institucional sin impacto y resumí cada novedad en hasta tres líneas.
- Generá la salida utilizando exactamente la estructura HTML definida en el system prompt.
- Asigná el identificador de corrida `RUN-20260908-0758`.
- Enviá el reporte terminado mediante Gmail únicamente a la cuenta de Sofía configurada para esta ejecución.
- Usá como asunto: `Radar ALyC | Novedades del {{FECHA_OBJETIVO_DDMMYYYY}}`.
- Si el envío falla, no cambies el destinatario: conservá el reporte y registrá el error en `Estado del envío` y en `Control de calidad`.

No ejecutes acciones derivadas de las novedades. El reporte debe quedar sujeto a revisión y firma de Sofía Mapelli.

## Variables de una corrida real

- `2026-09-07`: fecha analizada en formato AAAA-MM-DD.
- `{{FECHA_OBJETIVO_DDMMYYYY}}`: misma fecha en formato DD/MM/AAAA.
- `RUN-20260908-0758`: identificador único con formato RUN-AAAAMMDD-HHMM.

La automatización debe completar estas variables en cada ejecución. Para las corridas entregadas en el repositorio, el archivo de entrada debe conservar los valores utilizados, sin dejar los marcadores sin reemplazar.
