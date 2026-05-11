# Quick Start

## Initialize the Client

```python
from powerbi import PowerBiClient

power_bi_client = PowerBiClient(
    client_id="<client_id>",
    client_secret="<client_secret>",
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri="https://localhost:44300/",
    credentials="config/power_bi_state.jsonc",
)
```

## Working with Datasets

```python
datasets_service = power_bi_client.datasets()

# List all datasets in a workspace.
datasets = datasets_service.get_datasets(group_id="<group_id>")
```

## Working with Reports

```python
reports_service = power_bi_client.reports()

# Get all reports in a workspace.
reports = reports_service.get_reports(group_id="<group_id>")

# Export a report to PDF.
reports_service.export_to_file(
    report_id="<report_id>",
    file_format="PDF",
    group_id="<group_id>",
)
```

## Working with Pipelines

```python
pipelines_service = power_bi_client.pipelines()

# List deployment pipelines.
pipelines = pipelines_service.get_pipelines()

# Deploy all content from Development → Test.
pipelines_service.deploy_all(
    pipeline_id="<pipeline_id>",
    source_stage_order=0,
    options={"allowOverwriteArtifact": True},
)
```

## Context Manager

The client supports use as a context manager for automatic cleanup:

```python
with PowerBiClient(
    client_id="<client_id>",
    client_secret="<client_secret>",
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri="https://localhost:44300/",
) as client:
    dashboards = client.dashboards().get_dashboards()
```
