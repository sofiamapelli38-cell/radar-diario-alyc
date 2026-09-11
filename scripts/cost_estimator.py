#!/usr/bin/env python3
import csv
import sys
from decimal import Decimal


def calculate(row):
    million = Decimal("1000000")
    thousand = Decimal("1000")
    return (
        Decimal(row["input_tokens_estimated"]) / million * Decimal(row["input_usd_per_million"])
        + Decimal(row["output_tokens_estimated"]) / million * Decimal(row["output_usd_per_million"])
        + Decimal(row["web_calls"]) / thousand * Decimal(row["web_usd_per_1000"])
    )


def main(path):
    with open(path, newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    costs = [calculate(row) for row in rows]
    for row, cost in zip(rows, costs):
        print(f'{row["run_id"]}: USD {cost.quantize(Decimal("0.000001"))}')
    average = sum(costs) / len(costs)
    print(f'average: USD {average.quantize(Decimal("0.000001"))}')
    print(f'30 days: USD {(average * 30).quantize(Decimal("0.01"))}')
    print(f'365 days: USD {(average * 365).quantize(Decimal("0.01"))}')


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "costs/corridas.csv")
