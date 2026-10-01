## Security and publish checklist

- [ ] I ran `python -m pytest -q tests/test_security_headers.py`.
- [ ] I ran `pre-commit run --all-files` (or explained why it was unavailable).
- [ ] I ran the full-history Gitleaks scan for changes affecting secrets or configuration.
- [ ] No scanner report, credential, token, or private key is included in this PR.
- [ ] Any reviewed false positive has a specific documented fingerprint; no broad ignore was added.
- [ ] API, CORS, WebSocket, SSE, and frontend behavior were not unintentionally changed.
- [ ] The change is safe to pull into a fork and publish.

## Summary

<!-- What changed and why? -->

## Verification

<!-- Commands and results. -->
