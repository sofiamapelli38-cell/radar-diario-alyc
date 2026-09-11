# Reproducibilidad exacta de las corridas

Este documento operacionaliza FR-03: referencia exacta del agente, entrada resuelta, configuración relevante y salida original.

## Matriz de evidencia

| Corrida | Contrato | Entrada ejecutada | Configuración | Salida original anonimizada | Manifiesto |
|---|---|---|---|---|---|
| RUN-20260906-0802 | V1 | [entrada](corridas/corrida_01/entrada_ejecutada.md) | [config](config/versions/automation_v1.json) | [salida](corridas/corrida_01/salida_original_redactada.txt) | [manifest](corridas/corrida_01/manifest.json) |
| RUN-20260907-0805 | V2 | [entrada](corridas/corrida_02/entrada_ejecutada.md) | [config](config/versions/automation_v2.json) | [salida](corridas/corrida_02/salida_original_redactada.html) | [manifest](corridas/corrida_02/manifest.json) |
| RUN-20260908-0758 | V3 | [entrada](corridas/corrida_03/entrada_ejecutada.md) | [config](config/versions/automation_v3.json) | [salida](corridas/corrida_03/salida_original_redactada.html) | [manifest](corridas/corrida_03/manifest.json) |
| RUN-20260911-0758 | V4-final | [entrada](corridas/validacion_final/entrada_ejecutada.md) | [config](config/versions/automation_v4_final.json) | [salida](corridas/validacion_final/salida_original_redactada.html) | [manifest](corridas/validacion_final/manifest.json) |

## Integridad y privacidad

Cada manifiesto conserva blobs Git inmutables de los prompts y SHA-256 de la entrada, configuración y salida publicada. La única transformación aplicada al cuerpo original fue reemplazar la dirección privada por `[CUENTA_PRIVADA]`, con autorización expresa de la titular. No se publican encabezados ni metadatos privados del buzón.

## Límite histórico declarado

ChatGPT Work no ofreció un export bruto versionado de la tarea. Los snapshots de `config/versions/` se reconstruyeron desde los contratos versionados, las trazas ya documentadas y las decisiones registradas; no se presentan como exportes nativos inexistentes.

## Discrepancia temporal preservada

Los documentos existentes de la Corrida 2 registran ejecución a las 08:05 y observación del envío a las 08:03. No se corrigió por inferencia: se conserva como discrepancia histórica no resuelta.

## Verificación

```bash
python scripts/verify_run_manifests.py
python -m unittest discover -s tests -v
```
