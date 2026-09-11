# Versiones del contrato

| Versión | Corrida | Cambio único/principal | System prompt | User prompt |
|---|---|---|---|---|
| V1 | RUN-20260906-0802 | Contrato inicial en Markdown | [system](system_prompt_v1.md) | [user](user_prompt_v1.md) |
| V2 | RUN-20260907-0805 | Pieza Formato: HTML y enlaces | [system](system_prompt_v2.md) | [user](user_prompt_v2.md) |
| V3 | RUN-20260908-0758 | Pieza Restricciones: síntesis y relevancia | [system](system_prompt_v3.md) | [user](user_prompt_v3.md) |
| V4-final | RUN-20260911-0758 | Calibración al puesto y arrastre | [system](system_prompt_v4_final.md) | [user](user_prompt_v4_final.md) |

## Referencias Git inmutables

| Versión | System blob SHA | User blob SHA |
|---|---|---|
| V1 | `1ede4c2f029e9b1e7889efcc2b201846530421a6` | `6bde4dd7480bb3e903fa36be0f356778846bebf3` |
| V2 | `8cf03bb08ff893f9d6e7a6d5d4fda147a7d3b35f` | `643f42c85cadefac2a99b4bc0d91905d17e3bf29` |
| V3 | `a97a7b742b25296425a91cb7f9c0871734911fdb` | `766df7ff888e3c3ea14ef2e3df5d172473e84527` |
| V4-final | `dd4e68704df522ba5c5958d991a9735239881029` | `0d844c8ff4bd868b0a6552abbede5a0aebf548fd` |

Cada corrida vincula estos blobs con su entrada resuelta, snapshot de configuración, salida original anonimizada y traza mediante un `manifest.json`.
