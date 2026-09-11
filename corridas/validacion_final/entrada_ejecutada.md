# Entrada ejecutada — RUN-20260911-0758

Instancia resuelta del user prompt versionado. El system prompt se conserva en `prompts/versions/system_prompt_v4_final.md`.

## Referencias exactas

- System prompt blob: `dd4e68704df522ba5c5958d991a9735239881029`
- User prompt blob: `0d844c8ff4bd868b0a6552abbede5a0aebf548fd`
- Configuración: `config/versions/automation_v4_final.json`

## User prompt resuelto

# User prompt - Ejecución diaria (versión final)

Ejecutá el Radar Diario ALyC.

- Fecha principal: `2026-09-10`, de 00:00 a 23:59 en `America/Argentina/Buenos_Aires`.
- Ventana de arrastre: `2026-09-07` a `2026-09-09`.
- Identificador: `RUN-20260911-0758`.
- Revisá los correos anteriores con asunto “Radar ALyC” para recuperar omisiones y evitar duplicados.
- Aplicá el perfil, prioridades, exclusiones y control previo del system prompt.
- Generá el correo en HTML real, con asunto `Radar ALyC | Novedades del 10/09/2026`.
- Enviá únicamente a la cuenta privada de Sofía configurada en la automatización.
- Si falla una fuente, declaralo. Si falla Gmail, conservá el resultado y no cambies el destinatario.
- No ejecutes ninguna acción derivada de las novedades.

Sofía Mapelli valida las conclusiones y la aplicabilidad antes de actuar.
