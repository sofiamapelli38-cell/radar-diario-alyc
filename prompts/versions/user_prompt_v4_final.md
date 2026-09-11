# User prompt - Ejecución diaria (versión final)

Ejecutá el Radar Diario ALyC.

- Fecha principal: `{{FECHA_OBJETIVO}}`, de 00:00 a 23:59 en `America/Argentina/Buenos_Aires`.
- Ventana de arrastre: `{{ARRASTRE_DESDE}}` a `{{ARRASTRE_HASTA}}`.
- Identificador: `{{RUN_ID}}`.
- Revisá los correos anteriores con asunto “Radar ALyC” para recuperar omisiones y evitar duplicados.
- Aplicá el perfil, prioridades, exclusiones y control previo del system prompt.
- Generá el correo en HTML real, con asunto `Radar ALyC | Novedades del {{FECHA_DDMMYYYY}}`.
- Enviá únicamente a la cuenta privada de Sofía configurada en la automatización.
- Si falla una fuente, declaralo. Si falla Gmail, conservá el resultado y no cambies el destinatario.
- No ejecutes ninguna acción derivada de las novedades.

Sofía Mapelli valida las conclusiones y la aplicabilidad antes de actuar.
