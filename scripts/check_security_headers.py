"""Check security headers against a running Lear API."""
from __future__ import annotations
import sys
import urllib.request

REQUIRED = {
    "x-content-type-options": "nosniff",
    "x-frame-options": "DENY",
    "strict-transport-security": "max-age=31536000; includeSubDomains",
    "content-security-policy": "",
    "referrer-policy": "strict-origin-when-cross-origin",
    "permissions-policy": "camera=(), microphone=(), geolocation=()",
}
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"
with urllib.request.urlopen(f"{base}/api/system/version", timeout=5) as response:
    headers = {k.lower(): v for k, v in response.headers.items()}
missing = [key for key, expected in REQUIRED.items() if key not in headers or (expected and headers[key] != expected)]
for key in REQUIRED:
    print(("OK   " if key not in missing else "FAIL ") + key + (f": {headers.get(key, '')}" if key in headers else ""))
if missing:
    raise SystemExit(1)
