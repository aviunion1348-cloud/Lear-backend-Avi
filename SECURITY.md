# Security workflow

## Before publishing a fork

Install the development and security tools:

```bash
python -m pip install -e ".[dev]"
python -m pip install pre-commit
pre-commit install
```

Run the local checks:

```bash
make security-test
make secrets-scan
pre-commit run --all-files
```

On Windows PowerShell, run the test with `python -m pytest -q tests/test_security_headers.py` and the header check with `./scripts/check_security_headers.ps1`.

## Secret findings

Do not paste scanner output into issues, pull requests, logs, or chat. If a real credential is found, revoke or rotate it with the provider first. Do not add broad entries to `.gitleaksignore`; only a reviewed fingerprint may be added.

Generated reports such as `gitleaks-report.json` are ignored intentionally and must not be committed.

## CI

`.github/workflows/security.yml` runs a full-history scan (`fetch-depth: 0`) and the secure-header tests on pushes and pull requests, including fork pull requests.
