# Radar Diario ALyC

**Trabajo final individual - Programación de y con Agentes de IA - MBA UCEMA 2026**

**Autora:** Sofía Mapelli  
**Estado:** sistema implementado, automatizado y validado con corridas reales.

## 1. Problema real

El área de Impuestos y Contabilidad de una ALyC necesita revisar diariamente numerosas fuentes regulatorias, impositivas y profesionales. El relevamiento manual consume tiempo y puede omitir novedades relevantes entre información operativa de poco valor para el puesto.

## 2. Objetivo

Construir un agente que todos los días detecte, verifique y priorice novedades que puedan modificar o anticipar tareas impositivas, contables, societarias, regulatorias o de control de una ALyC argentina, y que envíe un correo claro para revisión humana.

## 3. Funcionamiento validado

1. Se ejecuta diariamente a las 08:00, hora argentina.
2. Releva el día calendario anterior.
3. Hace un control de arrastre de los tres días hábiles anteriores para recuperar novedades importantes omitidas.
4. Consulta fuentes oficiales, profesionales, periodísticas y sectoriales.
5. Prioriza Impuestos, Contabilidad y regulación aplicable a la ALyC.
6. Incluye como máximo cuatro novedades principales y una de innovación.
7. Genera un correo HTML con prioridades, acciones sugeridas y enlaces clicables.
8. Envía el resultado únicamente a la cuenta privada validada de la responsable.
9. Conserva la decisión profesional y cualquier acción posterior bajo supervisión humana.

## 4. Fuentes

- **Oficiales:** CNV, ARCA, UIF, BCRA, Boletín Oficial, Argentina.gob.ar/Normativa, BYMA, MAE, MAV y Caja de Valores.
- **Profesionales y periodísticas:** Errepar, Blog del Contador/SIAP, Consejo Profesional, iProfesional, El Cronista, Ámbito, iProUP y medios pertinentes.
- **Sector e innovación:** ALyCs, mercados y fintechs, con foco en cambios tecnológicos e inteligencia artificial que puedan afectar el negocio o la forma de trabajar.

Las fuentes periodísticas se usan como señales. Cuando mencionan una norma, el agente busca también respaldo oficial.

## 5. Criterio de relevancia final

Se priorizan:

- normas CNV sobre agentes, categorías, compatibilidades, patrimonio, AIF, estados contables y auditoría;
- cambios de ARCA o fiscos provinciales sobre IVA, Ganancias, retenciones, percepciones, facturación, IIBB y Convenio Multilateral;
- cambios UIF/PLAFT con impacto en matrices, informes, documentación o directorio;
- novedades contables, societarias y de auditoría;
- cambios operativos sólo cuando generan una consecuencia concreta para Impuestos o Contabilidad;
- como máximo una noticia relevante de IA, tecnología o innovación sectorial.

Se excluyen altas de especies, dividendos, eventos particulares de emisores, cotizaciones y contenido promocional, salvo impacto directo en el área.

## 6. Herramientas reales

- búsqueda web para consultar fuentes públicas;
- Gmail para el envío automático;
- automatización diaria en la zona horaria `America/Argentina/Buenos_Aires`.

Las credenciales y la dirección privada de envío no se publican.

## 7. Supervisión humana

- **L3:** búsqueda, filtrado, clasificación, redacción y envío automático a Sofía.
- **L1:** impacto, prioridad y acción sugerida como recomendaciones preliminares.
- **L0:** presentaciones, registraciones, cambios de sistemas, operaciones y comunicaciones a terceros.
- **Responsable final:** Sofía Mapelli.

## 8. Estructura

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
  validacion_final/
```

Las primeras tres carpetas documentan las corridas exigidas y las dos iteraciones. `validacion_final/` conserva la prueba posterior con la orientación definitiva.

## 9. Resultado

- Corrida 1: envío exitoso, pero el Markdown llegó como texto sin procesar.
- Iteración 1: se modificó únicamente el formato y el correo pasó a HTML.
- Corrida 2: formato correcto, pero todavía había demasiado texto y una novedad institucional de baja utilidad.
- Iteración 2: se ajustaron las restricciones de selección y síntesis.
- Corrida 3: confirmó la mejora formal, aunque evidenció que el perfil seguía demasiado orientado a Operaciones.
- Calibración final: se incorporó el puesto real de la destinataria como criterio rector, control de arrastre y bloque separado de innovación.
- Validación final: recuperó la RG CNV 1165/2026, priorizó facturación e IIBB, incluyó una señal relevante de IA y excluyó altas de especies sin impacto directo.

## 10. Limitaciones

El agente consulta web pública. Las circulares privadas, correos internos y áreas autenticadas requieren control humano. Una recomendación del reporte no prueba por sí sola que una norma resulte aplicable a la ALyC.
