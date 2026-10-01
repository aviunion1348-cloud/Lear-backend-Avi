.PHONY: security-test secrets-scan headers-check

security-test:
	python -m pytest -q tests/test_security_headers.py

secrets-scan:
	gitleaks git --config .gitleaks.toml --redact .

headers-check:
	python scripts/check_security_headers.py $${BASE_URL:-http://127.0.0.1:8000}
