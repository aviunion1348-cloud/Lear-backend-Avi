# S-05 / S-06 Security Delivery Record

## S-05 — Secrets audit

**Prior security:** The repository had a Gitleaks connector for scanning other repositories, but no committed policy, pre-commit hook configuration, or documented full-history audit record for this repository.

**Restriction:** Never expose findings, commit scanner reports, blanket-ignore files, or claim a credential is safe without provider verification. History must not be rewritten casually.

**Now:** Added `.gitleaks.toml`, an intentionally empty `.gitleaksignore`, `.pre-commit-config.yaml` pinned to Gitleaks `v8.30.1`, and ignored report outputs. The hook scans staged changes before commits. A full-history scan was attempted with Gitleaks; the release binary download was blocked by the sandbox's external release-assets TLS/network failure, so no clean-scan claim is made from this environment.

**Operator verification:** Install Gitleaks using the platform guide, then run:

```bash
gitleaks version
gitleaks git --config .gitleaks.toml --report-format json --report-path gitleaks-report.json --redact .
pre-commit install
pre-commit run --all-files
```

Delete any report after review. If a real credential is found, rotate it with the provider before considering remediation complete.

## S-06 — Secure headers

**Prior security:** FastAPI responses did not have a central security-header layer.

**Restriction:** Headers must apply to JSON, HTML, 404 and error responses; CSP must preserve WebSocket/SSE and existing inline demo behavior; HSTS must not use preload.

**Now:** Added `prash/middleware/security_headers.py` and wired it into `prash.server` after CORS. Responses receive:

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- Configurable `Content-Security-Policy` via `LEAR_CSP`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`

Added `tests/test_security_headers.py` for JSON and 404 responses plus exact values, and `scripts/check_security_headers.py` for live verification.

## Verification status

- Security middleware syntax checked.
- Frontend build/tests remain passing before this backend-only addition.
- Gitleaks full-history scan: **blocked/unverified in this sandbox** because the official release binary could not be downloaded; the repository now contains the prevention configuration and exact repeatable commands.
- No secrets or scanner report files were added.
