# Radar Diario ALyC

**Trabajo final individual - Programación de y con Agentes de IA - MBA UCEMA 2026**

**Autora:** Sofía Mapelli  
**Estado:** sistema configurado; corridas reales y documentación final en preparación.

## 1. Problema real

Una persona que trabaja en Impuestos y Contabilidad de una ALyC necesita revisar diariamente fuentes regulatorias, impositivas, operativas y sectoriales. El relevamiento manual consume tiempo, puede dejar fuentes sin revisar y dificulta comparar lo detectado entre distintos días.

## 2. Objetivo

Construir un sistema agéntico que, todos los días, releve las publicaciones del día calendario anterior, identifique novedades relevantes para una ALyC argentina, las verifique y clasifique, genere un reporte estructurado y lo envíe por correo electrónico para revisión humana.

El sistema no reemplaza el criterio profesional ni toma decisiones regulatorias, impositivas, contables, operativas o de Compliance.

## 3. Alcance

El agente consulta tres grupos de fuentes:

1. **Oficiales:** CNV, ARCA, UIF, BCRA, BYMA, MAE, MAV, Caja de Valores, Boletín Oficial y otros organismos o mercados pertinentes.
2. **Periodísticas y profesionales:** Errepar, iProfesional, El Cronista y otros medios especializados relevantes.
3. **Sectoriales:** publicaciones públicas de ALyCs, mercados y fintechs sobre productos, integraciones tecnológicas, servicios, alianzas y cambios operativos.

Cada novedad se clasifica como `ACCIÓN`, `RIESGO`, `OPORTUNIDAD` o `ACTUALIZACIÓN`, con prioridad `ALTA`, `MEDIA` o `BAJA`.

## 4. Funcionamiento

1. La automatización se activa diariamente a las 08:00, hora argentina.
2. Determina el día calendario anterior como fecha objetivo.
3. Utiliza búsqueda web para consultar fuentes públicas.
4. Verifica fecha, relevancia y respaldo de cada hallazgo.
5. Elimina duplicados y genera un reporte Markdown con estructura fija.
6. Envía el reporte por Gmail únicamente a la responsable configurada.
7. Sofía revisa la salida antes de tomar cualquier decisión o compartirla.

## 5. Herramientas reales

- **Búsqueda web:** consulta de publicaciones y enlaces directos.
- **Gmail:** envío del reporte diario a la responsable.
- **Automatización programada:** ejecución diaria con zona horaria `America/Argentina/Buenos_Aires`.

Las credenciales y la dirección privada de envío no se publican en este repositorio.

## 6. Entrada y salida

La entrada de cada corrida contiene la fecha objetivo y un identificador único. La salida es un reporte Markdown con:

- datos de ejecución y cobertura;
- resumen ejecutivo;
- tabla estructurada de novedades;
- control de calidad;
- supervisión humana requerida;
- estado del envío.

## 7. Supervisión humana

- **L3:** búsqueda, filtrado, clasificación, generación del reporte y envío automático a Sofía, con revisión posterior.
- **L1:** recomendaciones preliminares de impacto, prioridad y acción sugerida, sujetas a validación.
- **L0:** decisiones profesionales, presentaciones, registraciones, cambios operativos y comunicaciones a terceros.
- **Responsable final:** Sofía Mapelli.

El email automático es informativo y no constituye aprobación ni instrucción para actuar.

## 8. Estructura del repositorio

```text
README.md
DECISIONES.md
prompts/
  system_prompt.md
  user_prompt.md
corridas/
  corrida_01/
  corrida_02/
  corrida_03/
```

Cada corrida deberá conservar su entrada, salida, fecha, metadatos y evidencia del estado del envío para que un tercero pueda reconstruirla.

## 9. Estado de validación

- Contrato inicial redactado.
- Automatización diaria configurada.
- Gmail conectado y destinatario validado.
- Primera corrida real: pendiente.
- Segunda corrida real: pendiente.
- Tercera corrida real: pendiente.
- Análisis económico: pendiente de completar con mediciones reales.
- Gobierno y riesgos: diseño inicial incorporado; validación final pendiente.

## 10. Criterio de éxito

El sistema será considerado útil si detecta novedades relevantes sin inventar información, diferencia correctamente fuentes oficiales de señales periodísticas o sectoriales, conserva evidencia reconstruible y deja todas las decisiones profesionales bajo responsabilidad humana.
