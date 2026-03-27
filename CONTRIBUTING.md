# Contributing to power-bi-python-api

Thanks for your interest in contributing! This guide covers everything you need to get
started.

## Development Setup

1. **Clone the repo**

   ```console
   git clone https://github.com/areed1192/power-bi-python-api.git
   cd power-bi-python-api
   ```

2. **Create a virtual environment**

   ```console
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install in editable mode**

   ```console
   pip install -e .
   ```

4. **Configure credentials**

   ```console
   cp config/config.ini.example config/config.ini
   ```

   Fill in your own Client ID, Client Secret, and Group IDs. The `config/` directory
   is git-ignored so your secrets stay local.

## Running Tests

```console
python -m unittest discover -s tests -v
```

## Code Style

- **Type hints** on all public method signatures.
- **Docstrings** in the NumPy/Google hybrid style already used throughout the codebase
  (`### Parameters`, `### Returns`).
- Keep imports sorted: stdlib → third-party → local.
- Use `enum_to_value()` from `powerbi.utils` when an API parameter accepts both a
  raw value and an `Enum` member.

## Adding a New Service

1. Create `powerbi/<service>.py` with a class that accepts a `PowerBiSession` in
   `__init__` and stores it as `self._power_bi_session`.
2. Implement a `_build_endpoint()` helper that returns the base URL segment.
3. Map each REST endpoint to a method; use `self._power_bi_session.make_request()`.
4. Register the service in `powerbi/client.py`:
   - Import the class.
   - Add a lazy-initialized private attribute (`self._<service>`).
   - Add a public accessor method that creates the instance on first call.
5. Re-export the new class in `powerbi/__init__.py` if it's user-facing.
6. Add a sample file under `samples/`.
7. Add or update tests under `tests/`.

## Pull Request Checklist

- [ ] All existing tests pass (`python -m unittest discover -s tests -v`).
- [ ] New or changed public methods have type hints and docstrings.
- [ ] Update `CHANGELOG.md` under `[Unreleased]`.
- [ ] Sample file added or updated if a new endpoint was added.

## Reporting Issues

Open an issue on [GitHub](https://github.com/areed1192/power-bi-python-api/issues)
with:

- Python version and OS
- Minimal code to reproduce the problem
- Full traceback (if applicable)
