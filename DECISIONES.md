# Decisiones e historia del proceso

Este documento registra la evolución real del **Radar Diario ALyC**. Las fallas se conservan porque forman parte de la evidencia del aprendizaje.

## DEC-001 - Continuar un problema real

**Fecha:** 05/09/2026  
**Pieza:** contexto.

Se continuó el caso de la Entrega 1: seguimiento de novedades para una ALyC. El objetivo fue convertir un prompt manual en un sistema con ejecución diaria, búsqueda web, Gmail y evidencia reconstruible.

## DEC-002 - Usar fuentes oficiales, profesionales y sectoriales

**Fecha:** 05/09/2026  
**Pieza:** contexto.

El agente no debía limitarse a organismos oficiales. Se agregaron fuentes profesionales como Errepar y fuentes sectoriales para detectar cambios tecnológicos o competitivos. Las noticias funcionan como señales; una obligación normativa requiere respaldo oficial.

## DEC-003 - Usar día calendario y no “últimas 24 horas”

**Fecha:** 05/09/2026  
**Pieza:** tarea.

Cada ejecución toma el día anterior entre 00:00 y 23:59, hora argentina. Esto evita ventanas variables y permite comparar las corridas.

## DEC-004 - Automatizar y enviar por Gmail

**Fecha:** 05/09/2026  
**Pieza:** herramientas y tarea.

Se programó la ejecución diaria a las 08:00 y el envío a una única cuenta privada validada. La dirección y las credenciales no se publican.

## DEC-005 - Separar automatización y decisión profesional

**Fecha:** 05/09/2026  
**Pieza:** restricciones y gobierno.

El agente opera en L3 para buscar, redactar y enviar; en L1 para recomendar; y en L0 para cualquier presentación, registración, cambio operativo o comunicación. La responsable final es Sofía Mapelli.

## Iteración 1 - Corregir la presentación del correo

**Falla observada en la Corrida 1 (06/09):**

> El correo mostraba `#`, `##`, guiones y separadores de tabla como texto. La tabla de trece columnas no se renderizó y los enlaces se mezclaban con el Markdown.

La cabecera técnica confirmó `Content-Type: text/plain`.

**Pieza modificada:** formato, y solamente formato.

**Cambio:**

- enviar HTML real con estilos compatibles con Gmail;
- reducir la tabla a seis columnas;
- usar prioridades visuales;
- mostrar enlaces clicables;
- omitir una tabla vacía cuando no haya novedades.

**Resultado en la Corrida 2 (07/09):**

La cabecera pasó a `Content-Type: text/html; charset=UTF-8`. Gmail mostró encabezado, colores, tabla y tres enlaces clicables. El envío de punta a punta quedó validado.

## Iteración 2 - Reducir ruido y extensión

**Falla observada en la Corrida 2:**

> La tabla todavía concentraba párrafos largos en seis columnas y agregó la versión en inglés de los resultados de BYMA, una actualización institucional sin impacto práctico.

**Pieza modificada:** restricciones y criterios de relevancia.

**Cambio:**

- máximo cinco novedades;
- excluir traducciones, promoción y contenido institucional sin impacto;
- resumir cada novedad en hasta tres líneas;
- exigir “qué pasó, por qué importa y qué conviene hacer”.

**Resultado en la Corrida 3 (08/09):**

El agente incluyó tres novedades, evitó completar con actualizaciones adicionales de baja utilidad y mantuvo el HTML estable. La mejora fue parcial: el reporte seguía priorizando asuntos de Operaciones —cuentas comitentes, un cambio de ratio de CEDEAR y recompra de ON— por encima del trabajo cotidiano de Impuestos y Contabilidad.

## Calibración posterior - Orientar el agente al puesto real

**Problema detectado después de las tres corridas:**

El radar omitió la RG CNV 1165/2026 sobre Matriz de Compatibilidades y una noticia relevante sobre lineamientos para IA, mientras informaba altas de especies, CEDEARs y eventos de emisores. El criterio era válido para una ALyC en general, pero no para la destinataria.

**Decisión final:**

- convertir el perfil “Impuestos y Contabilidad de una ALyC” en el criterio principal;
- priorizar CNV, ARCA, fiscos, UIF, contabilidad, auditoría, AIF y aspectos societarios;
- agregar un control de arrastre de tres días hábiles;
- separar hasta cuatro novedades principales de una única noticia de sector e innovación;
- excluir información operativa sin consecuencia contable, impositiva o regulatoria concreta;
- exigir búsquedas alternativas cuando Errepar, AIF u otra página dinámica no pueda abrirse.

## Validación final - Corrida del 11/09

La salida sobre el 10/09 recuperó la RG CNV 1165/2026, incorporó un control de facturación de ARCA, una prórroga de AGIP y una señal de IA útil para política interna. También explicó el impacto indirecto de una comunicación BCRA y documentó las exclusiones.

La destinataria evaluó que la función quedó alineada al 100 % con su objetivo. Por eso se congeló el criterio de búsqueda y selección: los cambios futuros deberán considerarse mantenimiento, no una nueva iteración del contrato.

## Matriz breve de riesgos

| Riesgo | Control |
|---|---|
| Omitir una norma relevante | Arrastre de tres días hábiles y control previo por organismo/tema |
| Confundir noticia con norma | Enlace oficial y estado de validación |
| Incluir ruido operativo | Prioridad por puesto y exclusiones expresas |
| Página dinámica inaccesible | Búsqueda por título, fecha y palabras clave |
| Aplicabilidad mal interpretada | Recomendación preliminar y validación humana |
| Envío a terceros | Destinatario único configurado de forma privada |


## DEC-006 - Publicar una implementación auditable

**Fecha:** 11/09/2026  
**Motivo:** los evaluadores detectaron que las corridas probaban funcionamiento, pero faltaba un artefacto técnico ejecutable.

Se conservó la configuración real de ChatGPT Work y se agregó una réplica portátil en Python. La réplica usa Responses API con web search, valida HTML y ofrece envío Gmail con scope `gmail.send`. Se aclara que las corridas históricas fueron producidas por ChatGPT Work.

**Evidencia:** `config/chatgpt_work_automation.json`, `src/radar_agent.py`, `tests/test_radar_agent.py`.

## DEC-007 - Hacer reproducible cada corrida

**Fecha:** 11/09/2026  
**Motivo:** las entradas y salidas no vinculaban la versión exacta del contrato.

Se agregaron V1, V2, V3 y V4 final. Cada metadata enlaza prompts, configuración, entrada, salida y traza de envío.

**Evidencia:** `prompts/versions/` y los cuatro `metadata.json`.

## DEC-008 - Separar costo real y equivalente API

**Fecha:** 11/09/2026  
**Motivo:** ChatGPT Work no expone tokens/modelo facturado por tarea; asignar un costo exacto hubiera sido inventado.

Se declaró esa limitación y se creó un equivalente API estimado con supuestos, tarifas oficiales, fórmula, CSV y script. Se eligió Luna como alternativa costo-eficiente y se comparó con Terra, Sol y Astra.

**Evidencia:** `ANALISIS_ECONOMICO.md`, `costs/corridas.csv`, `scripts/cost_estimator.py`.

## DEC-009 - Operacionalizar permisos y contingencias

**Fecha:** 11/09/2026  
**Motivo:** la matriz de riesgos no indicaba cuándo detener, degradar o escalar.

Se definieron allowlist de destinatario, operaciones Gmail permitidas/prohibidas, umbral de cobertura parcial, detención por datos sensibles, escalamiento tras dos fallas y kill switch.

**Evidencia:** `GOVERNANCE.md`, `config/permissions.json`, `INCIDENTES.md`.
