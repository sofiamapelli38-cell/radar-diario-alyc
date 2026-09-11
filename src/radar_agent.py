#!/usr/bin/env python3
"""Portable, auditable implementation of Radar Diario ALyC.

Production ran as a scheduled ChatGPT Work task. This script reproduces the
same contract with the OpenAI Responses API and optionally sends the resulting
HTML through the Gmail API using the least-privilege gmail.send scope.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
from datetime import date, datetime, timedelta
from email.mime.text import MIMEText
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_HEADINGS = (
    "Radar ALyC",
    "Lo importante para tu trabajo",
    "Impuestos, Contabilidad y regulación de la ALyC",
    "Control de cobertura",
)
ALLOWED_RECIPIENT_ENV = "RADAR_ALLOWED_RECIPIENT"


def previous_business_days(target: date, count: int = 3) -> tuple[date, date]:
    days: list[date] = []
    cursor = target - timedelta(days=1)
    while len(days) < count:
        if cursor.weekday() < 5:
            days.append(cursor)
        cursor -= timedelta(days=1)
    return min(days), max(days)


def render_user_prompt(target: date, run_id: str) -> str:
    template = (ROOT / "prompts" / "user_prompt.md").read_text(encoding="utf-8")
    start, end = previous_business_days(target)
    values = {
        "{{FECHA_OBJETIVO}}": target.isoformat(),
        "{{FECHA_DDMMYYYY}}": target.strftime("%d/%m/%Y"),
        "{{ARRASTRE_DESDE}}": start.isoformat(),
        "{{ARRASTRE_HASTA}}": end.isoformat(),
        "{{RUN_ID}}": run_id,
    }
    for marker, value in values.items():
        template = template.replace(marker, value)
    if "{{" in template:
        raise ValueError("The user prompt still contains unresolved variables")
    return template


def validate_html(report: str) -> list[str]:
    errors: list[str] = []
    lowered = report.lower()
    for heading in REQUIRED_HEADINGS:
        if heading.lower() not in lowered:
            errors.append(f"missing required section: {heading}")
    if "<html" not in lowered or "<a " not in lowered:
        errors.append("output must be HTML and contain at least one link")
    if re.search(r"(?:^|\n)#{1,3}\s", report):
        errors.append("visible Markdown heading detected")
    return errors


def generate_report(target: date, run_id: str, model: str) -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit("Install dependencies with: pip install -r requirements.txt") from exc

    system_prompt = (ROOT / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
    user_prompt = render_user_prompt(target, run_id)
    client = OpenAI()
    response = client.responses.create(
        model=model,
        tools=[{"type": "web_search"}],
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    report = response.output_text
    errors = validate_html(report)
    if errors:
        raise RuntimeError("Invalid report: " + "; ".join(errors))
    return report


def send_gmail(report: str, subject: str, recipient: str, token_file: Path) -> str:
    allowed = os.environ.get(ALLOWED_RECIPIENT_ENV)
    if not allowed or recipient.casefold() != allowed.casefold():
        raise PermissionError("Recipient is not the exact allowlisted address")

    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/gmail.send"]
    credentials = Credentials.from_authorized_user_file(str(token_file), scopes)
    message = MIMEText(report, "html", "utf-8")
    message["To"] = recipient
    message["Subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode("ascii")
    result = build("gmail", "v1", credentials=credentials).users().messages().send(
        userId="me", body={"raw": raw}
    ).execute()
    return str(result["id"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Radar Diario ALyC")
    parser.add_argument("--date", required=True, help="Target date YYYY-MM-DD")
    parser.add_argument("--run-id", help="Defaults to RUN-AAAAMMDD-HHMM")
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--fixture", type=Path, help="Use saved HTML instead of the API")
    parser.add_argument("--output", type=Path, default=Path("output/radar.html"))
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--to", help="Must equal RADAR_ALLOWED_RECIPIENT")
    parser.add_argument("--gmail-token", type=Path)
    args = parser.parse_args()

    target = date.fromisoformat(args.date)
    run_id = args.run_id or datetime.now().strftime("RUN-%Y%m%d-%H%M")
    if args.fixture:
        report = args.fixture.read_text(encoding="utf-8")
        errors = validate_html(report)
        if errors:
            raise SystemExit("Invalid fixture: " + "; ".join(errors))
    else:
        report = generate_report(target, run_id, args.model)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    result = {"run_id": run_id, "output": str(args.output), "sent": False}
    if args.send:
        if not args.to or not args.gmail_token:
            raise SystemExit("--send requires --to and --gmail-token")
        subject = f"Radar ALyC | Novedades del {target:%d/%m/%Y}"
        result["gmail_message_id"] = send_gmail(report, subject, args.to, args.gmail_token)
        result["sent"] = True
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
