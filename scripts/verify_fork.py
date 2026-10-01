"""Fast, dependency-free smoke check for a freshly cloned fork."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ".gitleaks.toml", ".pre-commit-config.yaml", "SECURITY.md",
    "PUBLISHING.md", "prash/middleware/security_headers.py",
    "tests/test_security_headers.py", ".github/workflows/security.yml",
]
missing = [item for item in required if not (ROOT / item).exists()]
if missing:
    print("Missing required fork files:")
    print("\n".join(f"- {item}" for item in missing))
    sys.exit(1)

forbidden = [ROOT / name for name in ("gitleaks-report.json", "gitleaks-report.sarif")]
committed_reports = [path.name for path in forbidden if path.exists()]
if committed_reports:
    print("Remove generated scanner reports before publishing:", ", ".join(committed_reports))
    sys.exit(1)

print(f"Fork smoke check passed: {len(required)} required files present")
