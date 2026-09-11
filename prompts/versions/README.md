# Versiones del contrato

| Versión | Corrida | Cambio único/principal | System prompt | User prompt |
|---|---|---|---|---|
| V1 | RUN-20260906-0802 | Contrato inicial en Markdown | [system](system_prompt_v1.md) | [user](user_prompt_v1.md) |
| V2 | RUN-20260907-0805 | Pieza Formato: HTML y enlaces | [system](system_prompt_v2.md) | [user](user_prompt_v2.md) |
| V3 | RUN-20260908-0758 | Pieza Restricciones: síntesis y relevancia | [system](system_prompt_v3.md) | [user](user_prompt_v3.md) |
| V4 final | RUN-20260911-0758 | Calibración al puesto y arrastre | [system](system_prompt_v4_final.md) | [user](user_prompt_v4_final.md) |

## Integridad histórica

La V1 también permanece en el historial Git mediante los blobs inmutables:

- System V1: `1ede4c2f029e9b1e7889efcc2b201846530421a6`
- User V1: `6bde4dd7480bb3e903fa36be0f356778846bebf3`

V2 y V3 preservan el contrato efectivo aplicado después de cada cambio documentado. V4 es una copia de los prompts activos publicados en la raíz de `prompts/`.
