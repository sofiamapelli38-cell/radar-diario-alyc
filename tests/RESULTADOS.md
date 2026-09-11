# Resultados de pruebas

Fecha de ejecución: 11/09/2026.

Comando:

```bash
python3 -m unittest discover -s tests -v
```

Resultado:

```text
test_business_day_window ... ok
test_prompt_has_no_unresolved_variables ... ok
test_valid_html ... ok

Ran 3 tests
OK
```

También se ejecutó `python3 -m py_compile src/radar_agent.py scripts/cost_estimator.py` sin errores.
