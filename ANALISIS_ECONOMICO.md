# Análisis económico reproducible

## Alcance y honestidad del cálculo

La implementación real utiliza una tarea de ChatGPT Work. La plataforma no expone en la evidencia de cada tarea el modelo exacto ni los tokens facturados y no cobra una línea API separada por este envío. Por eso no se presenta un costo real inventado: se calcula un **equivalente API estimado** para que la comparación sea reproducible.

Fecha de consulta de tarifas: 11/09/2026. Fuente oficial: https://developers.openai.com/api/docs/pricing

## Supuestos por corrida

- 15.000 tokens de entrada: contrato, pedido diario y contexto recuperado por búsquedas. Es un supuesto conservador porque ChatGPT Work no informa el consumo exacto.
- Tokens de salida estimados desde el tamaño UTF-8 del email original dividido por 4; el CSV conserva la cifra por corrida.
- 10 llamadas de búsqueda web por corrida.
- Modelo de referencia: `gpt-5.6-luna`, contexto corto, procesamiento Standard.
- Tarifas por 1 millón de tokens: USD 0,20 entrada y USD 1,20 salida.
- Web search: USD 10 por 1.000 llamadas, equivalente a USD 0,01 por llamada.

## Fórmula

`costo = input_tokens / 1.000.000 * 0,20 + output_tokens / 1.000.000 * 1,20 + web_calls / 1.000 * 10`

Ejemplo para la validación final:

`15.000/1.000.000*0,20 + 2.635/1.000.000*1,20 + 10/1.000*10 = USD 0,106162`

## Resultado y proyección

El promedio de las cuatro corridas documentadas es **USD 0,1054 por corrida** como equivalente API.

- Frecuencia: 1 corrida diaria.
- Mes de 30 días: `0,1054 * 30 = USD 3,16`.
- Año de 365 días: `0,1054 * 365 = USD 38,47`.

Estos importes no incluyen impuestos, tipo de cambio, una suscripción de ChatGPT ni trabajo humano. Son una estimación marginal comparable de modelo y búsqueda.

## Elección costo-eficiente

Con los mismos supuestos de 15.000 tokens de entrada, 1.500 de salida y 10 búsquedas:

| Modelo | Entrada USD/M | Salida USD/M | Costo estimado/corrida |
|---|---:|---:|---:|
| gpt-5.6-luna | 0,20 | 1,20 | USD 0,1048 |
| gpt-5.6-terra | 2,00 | 12,00 | USD 0,1480 |
| gpt-5.6-sol | 4,00 | 20,00 | USD 0,1900 |
| gpt-6-astra | 10,00 | 50,00 | USD 0,3250 |

Se elige `gpt-5.6-luna` para la réplica API porque la tarea es clasificación y síntesis estructurada, el control humano es obligatorio y las corridas reales demostraron que el contrato y los controles pesan más que usar el modelo más caro. Terra, Sol o Astra quedan como escalamiento manual para contradicciones complejas, no como costo diario por defecto.

## Recalcular

Ejecutar:

```bash
python scripts/cost_estimator.py costs/corridas.csv
```

El script recalcula cada fila y la proyección mensual/anual. Si cambian precios o volumen, se actualizan las columnas del CSV sin cambiar la fórmula.
