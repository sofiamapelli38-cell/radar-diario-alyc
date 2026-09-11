import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReproducibilityTests(unittest.TestCase):
 def test_run_manifest_hashes(self):
  manifests=sorted((ROOT/"corridas").glob("*/manifest.json"));self.assertGreaterEqual(len(manifests),3)
  for path in manifests:
   d=json.loads(path.read_text(encoding="utf-8"));checks=[(d["automation"]["path"],d["automation"]["sha256"]),(d["input"]["path"],d["input"]["sha256"]),(d["output"]["path"],d["output"]["sha256"])]
   for rel,expected in checks:self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),expected,rel)
if __name__=="__main__":unittest.main()
