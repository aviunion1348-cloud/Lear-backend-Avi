# Pull and publish checklist

This repository is designed to work from a fork without private workspace paths.

## Pull the feature branch

```bash
git fetch origin arena/01a0ee2a-lear-backend-avi
git checkout arena/01a0ee2a-lear-backend-avi
git pull --ff-only origin arena/01a0ee2a-lear-backend-avi
```

## Install and verify

```bash
python -m pip install -e ".[dev]"
python -m pytest -q tests/test_security_headers.py
pre-commit run --all-files
```

Run the full-history secrets scan before publishing:

```bash
gitleaks git --config .gitleaks.toml --redact .
```

## Publish from a fork

1. Fork the repository on GitHub.
2. Push your branch to the fork.
3. Open a pull request against the upstream feature or target branch.
4. Wait for the `Security checks` workflow and the normal `CI` workflow.
5. Do not publish if Gitleaks reports a real credential; rotate it with the provider first.

The workflow uses only repository-relative paths, read-only contents permission, and the built-in GitHub token. No local secrets are required for pull requests from forks.

Before opening a pull request from a fork, run the dependency-free repository smoke check:

```bash
python scripts/verify_fork.py
```

Or:

```bash
make fork-check
```

For one local security gate, run `make ci-security`; it checks the fork layout and secure-header tests together.
