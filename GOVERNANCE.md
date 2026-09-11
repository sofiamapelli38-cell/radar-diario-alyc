# Gobierno, permisos y contingencias

## Responsabilidad y supervisión

| Actividad | Nivel | Responsable | Evidencia |
|---|---|---|---|
| Buscar, filtrar, redactar y enviar a la cuenta propia | L3 | Agente | ID de corrida e ID de Gmail |
| Interpretar impacto, prioridad y acción sugerida | L1 | Agente propone; Sofía valida | Reporte y fuente enlazada |
| Registrar, presentar, cambiar sistemas u operar | L0 | Sofía/área competente | Fuera del agente |
| Autorizar un destinatario distinto | L0 | Sofía | Cambio manual y documentado |

## Mínimo privilegio

- Web: sólo lectura de páginas públicas; sin credenciales de CNV, ARCA, UIF, BCRA, mercados o sistemas internos.
- Gmail en producción: buscar/leer únicamente mensajes previos con asunto `Radar ALyC` para evitar duplicados y enviar a una única cuenta propia. Se prohíbe borrar, archivar, etiquetar, modificar o reenviar.
- Implementación portátil: usa sólo el scope `gmail.send`; la historia se toma de archivos locales.
- Secretos: variables de entorno y token OAuth local. Nunca se guardan en GitHub ni en las corridas.

## Protocolo de contingencias

| Evento | Detección | Respuesta automática | Decisión humana / escalamiento |
|---|---|---|---|
| Gmail no envía | API/conector devuelve error o no hay ID | Guardar salida, marcar `ENVIO_FALLIDO`, no cambiar destinatario ni reintentar en bucle | Sofía revisa y decide reenvío manual |
| Más del 50% de fuentes críticas inaccesibles | Control de cobertura | Enviar sólo un reporte `COBERTURA_PARCIAL`; no formular conclusiones de ausencia | Sofía repite control manual de CNV, ARCA, UIF y BCRA |
| Fuente periodística contradice la oficial | Comparación de contenido/fecha | Priorizar la oficial, marcar contradicción y bloquear acción sugerida | Sofía o especialista valida aplicabilidad |
| Fecha o norma no verificable | Falta publicación original | Excluir del bloque principal y registrar como pendiente | Revisar en la siguiente corrida o manualmente |
| Dato personal, reservado o documento interno | Detección durante entrada/salida | Detener procesamiento de ese contenido; no enviarlo ni versionarlo | Sofía evalúa incidente y elimina el insumo |
| Destinatario no coincide con allowlist | Validación exacta antes del envío | Cancelar envío y devolver error | No se habilita tercero sin cambio manual aprobado |
| Dos fallas consecutivas de envío o búsqueda crítica | Metadatos de corridas | No continuar en modo degradado indefinidamente | Activar kill switch y revisión técnica |

## Kill switch

1. Pausar la tarea `Radar diario ALyC` en Automatizaciones de ChatGPT.
2. Si el riesgo involucra correo, desconectar temporalmente Gmail.
3. Conservar la última salida segura y el mensaje de error; no borrar evidencia.
4. Registrar fecha, causa, alcance y decisión de reactivación en `INCIDENTES.md`.
5. Reactivar sólo después de una prueba de solo lectura y un envío controlado a la cuenta propia.

## Criterios de detención

El agente debe detener el envío cuando detecta destinatario no autorizado, contenido reservado o salida que no supera las validaciones de formato. Debe degradar a `COBERTURA_PARCIAL` ante fallas de fuentes y escalar a pausa manual después de dos fallas críticas consecutivas.
