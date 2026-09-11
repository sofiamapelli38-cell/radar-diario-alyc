# Matriz de correcciones según evaluadores

Esta tabla vincula cada descuento observado con evidencia concreta del repositorio.

| Criterio observado | Corrección | Evidencia verificable |
|---|---|---|
| SC-02 - Herramienta o conector real | Configuración real de ChatGPT Work y réplica ejecutable con web search y Gmail | [configuración](config/chatgpt_work_automation.json), [script](src/radar_agent.py), [trazas](corridas/) |
| D1 - Sistema ejecutable | Código, dependencias, variables de entorno y pruebas | [src](src/radar_agent.py), [requirements](requirements.txt), [.env.example](.env.example), [tests](tests/) |
| FR-03 - Reproducibilidad exacta | Blobs Git de prompts, entradas resueltas, configuración versionada, salidas originales anonimizadas y manifiestos con hashes | [procedimiento](REPRODUCIBILIDAD.md), [versiones](prompts/versions/), [manifiestos](corridas/) |
| PD - Trazabilidad de decisiones | Cada corrección nueva tiene ID, motivo y artefactos | [DECISIONES.md](DECISIONES.md) |
| AE-01 - Costo por corrida | Estimación API por corrida, moneda, supuestos, tarifas y fórmula | [análisis](ANALISIS_ECONOMICO.md), [datos](costs/corridas.csv) |
| AE-02 - Proyección | Frecuencia diaria, horizonte mensual/anual y aritmética ejecutable | [análisis](ANALISIS_ECONOMICO.md), [calculadora](scripts/cost_estimator.py) |
| AE-03 - Modelo costo-eficiente | Comparación Luna/Terra/Sol/Astra y regla de escalamiento | [selección](ANALISIS_ECONOMICO.md#elección-costo-eficiente) |
| GR-01 - Mínimo privilegio | Operaciones y sistemas permitidos/prohibidos; scope portable gmail.send | [permisos](config/permissions.json), [gobierno](GOVERNANCE.md) |
| GR-03 - Contingencias operables | Umbrales de degradación, detención, escalamiento y kill switch | [contingencias](GOVERNANCE.md#protocolo-de-contingencias) |
| Inconsistencia “automatizado sin configuración” | README enlaza configuración y código, distinguiendo producción y réplica | [README](README.md#11-implementación-y-reproducción-técnica) |

## Nota sobre privacidad

Con autorización expresa, las copias del cuerpo original se publican reemplazando únicamente la dirección exacta por `[CUENTA_PRIVADA]`. No se publican encabezados, metadatos privados, tokens ni credenciales.
