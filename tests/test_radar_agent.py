import tempfile
import unittest
from datetime import date
from pathlib import Path

from src.radar_agent import previous_business_days, render_user_prompt, validate_html


class RadarAgentTests(unittest.TestCase):
    def test_business_day_window(self):
        start, end = previous_business_days(date(2026, 9, 10))
        self.assertEqual(start.isoformat(), "2026-09-07")
        self.assertEqual(end.isoformat(), "2026-09-09")

    def test_prompt_has_no_unresolved_variables(self):
        rendered = render_user_prompt(date(2026, 9, 10), "RUN-TEST")
        self.assertNotIn("{{", rendered)
        self.assertIn("RUN-TEST", rendered)

    def test_valid_html(self):
        html = """<html><body><h1>Radar ALyC</h1>
        <h2>Lo importante para tu trabajo</h2>
        <h2>Impuestos, Contabilidad y regulación de la ALyC</h2>
        <h2>Control de cobertura</h2><a href='https://example.com'>Fuente</a></body></html>"""
        self.assertEqual(validate_html(html), [])


if __name__ == "__main__":
    unittest.main()
