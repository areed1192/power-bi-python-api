# Power BI Python API

The **Unofficial Python API wrapper** for the Microsoft Power BI REST API.

## Features

- **Full REST API coverage** — 16 service classes mapping 1-to-1 to Power BI REST endpoints.
- **Automatic authentication** — MSAL-based OAuth 2.0 with silent SSO and token refresh.
- **Data model builders** — `Dataset`, `Table`, `Column`, `Measure`, `Relationship` classes for Push Datasets.
- **Type-safe** — PEP 561 `py.typed` marker, return type annotations on all methods.
- **Context manager support** — use `with PowerBiClient(...) as client:` for automatic cleanup.

## Quick Install

```console
pip install python-power-bi
```

## Quick Example

```python
from powerbi import PowerBiClient

with PowerBiClient(
    client_id="<client_id>",
    client_secret="<client_secret>",
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri="https://localhost:44300/",
    credentials="config/power_bi_state.jsonc",
) as client:
    datasets = client.datasets().get_datasets(group_id="<group_id>")
    print(datasets)
```

## Navigation

- **[Getting Started](getting-started/installation.md)** — installation, authentication, first API call.
- **[API Reference](api/client.md)** — full autodoc for every class and method.
