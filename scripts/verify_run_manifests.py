#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 manifests=sorted((ROOT/"corridas").glob("*/manifest.json"))
 if len(manifests)<3:raise SystemExit("Expected at least three run manifests")
 for path in manifests:
  d=json.loads(path.read_text(encoding="utf-8"));checks=[(d["automation"]["path"],d["automation"]["sha256"]),(d["input"]["path"],d["input"]["sha256"]),(d["output"]["path"],d["output"]["sha256"])]
  for rel,expected in checks:
   if digest(ROOT/rel)!=expected:raise SystemExit(f"{d['run_id']}: hash mismatch for {rel}")
  print(f"{d['run_id']}: OK")
 return 0
if __name__=="__main__":raise SystemExit(main())
