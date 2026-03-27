# Unofficial Power Bi Python API

## Table of Contents

- [Overview](#overview)
- [Resources](#resources)
- [Architecture](#architecture)
- [Setup](#setup)
- [Authentication](#authentication)
- [Quick Start](#quick-start)
- [Samples](#samples)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

Version: **0.1.2**

Power BI is a business analytics service by Microsoft. It aims to provide interactive
visualizations and business intelligence capabilities with an interface simple enough
for end users to create their own reports and dashboards. It is part of the Microsoft
Power Platform. This library allows you to use the Power BI Rest API from python. Along
with providing the different endpoints, it will also handle the authentication process
for you.

## Resources

- [Power BI App Registration Portal](https://dev.powerbi.com/Apps)
- [Power BI Rest API Documentation](https://learn.microsoft.com/en-us/rest/api/power-bi/)

## Architecture

The library follows a layered design:

```
PowerBiClient          ← Entry point: creates authenticated session, exposes services
  ├── PowerBiAuth      ← MSAL-based auth: handles login, token refresh, credential persistence
  ├── PowerBiSession   ← HTTP layer: builds headers/URLs, executes requests, raises on errors
  └── Service classes  ← One per API area (Dashboards, Datasets, Reports, …)
        └── make_request()  → PowerBiSession.make_request()  → requests.Session
```

| Layer         | Module                                      | Responsibility                                                                                   |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Client**    | `powerbi.client`                            | Lazy-initializes each service, owns the session lifecycle, context manager                       |
| **Auth**      | `powerbi.auth`                              | Wraps `msal.ConfidentialClientApplication`, handles OAuth 2.0 code flow + silent SSO             |
| **Session**   | `powerbi.session`                           | Adds `Authorization` header, builds REST URLs, calls `requests`, raises `HTTPError` with details |
| **Services**  | `powerbi.dashboards`, `powerbi.datasets`, … | One class per API area; methods map 1-to-1 to REST endpoints                                     |
| **Utilities** | `powerbi.utils`                             | Data-model classes (`Dataset`, `Table`, `Column`, `Measure`, `Relationship`, etc.)               |
| **Enums**     | `powerbi.enums`                             | Typed constants (`ColumnDataTypes`, `DatasetModes`, `DataSourceType`, etc.)                      |

## Setup

**Setup - Requirements Install:**

For this particular project, you only need to install the dependencies, to use the project. The dependencies
are listed in the `requirements.txt` file and can be installed by running the following command:

```console
pip install -r requirements.txt
```

After running that command, the dependencies should be installed.

**Setup - Local Install:**

If you are planning to make modifications to this project or you would like to access it
before it has been indexed on `PyPi`. I would recommend you either install this project
in `editable` mode or do a `local install`. For those of you, who want to make modifications
to this project. I would recommend you install the library in `editable` mode.

If you want to install the library in `editable` mode, make sure to run the `setup.py`
file, so you can install any dependencies you may need. To run the `setup.py` file,
run the following command in your terminal.

```console
pip install -e .
```

If you don't plan to make any modifications to the project but still want to use it across
your different projects, then do a local install.

```console
pip install .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

**Setup - PyPi Install:**

To **install** the library, run the following command from the terminal.

```console
pip install python-power-bi
```

**Setup - PyPi Upgrade:**

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade python-power-bi
```

## Authentication

This library uses **MSAL** (Microsoft Authentication Library) with a **Confidential Client**
flow, which is the recommended approach for server-side / backend applications.

### How it works

1. **Register an app** in the [Power BI App Registration Portal](https://dev.powerbi.com/Apps)
   (or Azure AD). Note your **Client ID**, **Client Secret**, and **Redirect URI**.

2. **First run** — the library opens a browser-based authorization prompt. After you
   sign in, paste the redirect URL back into the terminal. The resulting tokens are
   saved to a local JSON file (`power_bi_state.jsonc`).

3. **Subsequent runs** — the library loads the saved tokens and attempts a **silent SSO**.
   If the access token is still valid, no interaction is needed. If it has expired, the
   refresh token is used automatically to obtain a new access token.

### Configuration

Copy the example config and fill in your credentials:

```console
cp config/config.ini.example config/config.ini
```

```ini
[power_bi_api]
client_id = <your Azure AD app client id>
client_secret = <your Azure AD app client secret>
redirect_uri = https://localhost:44300/
group_id = <your workspace / group id>
```

> **Note:** `config/config.ini` is git-ignored and will never be committed.

## Quick Start

### Working with Datasets

```python
from powerbi import PowerBiClient

power_bi_client = PowerBiClient(
    client_id="<client_id>",
    client_secret="<client_secret>",
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri="https://localhost:44300/",
    credentials="config/power_bi_state.jsonc",
)

# List all datasets in a workspace.
datasets_service = power_bi_client.datasets()
datasets = datasets_service.get_datasets_in_group(group_id="<group_id>")
```

### Working with Reports

```python
reports_service = power_bi_client.reports()

# Get all reports in a workspace.
reports = reports_service.get_reports_in_group(group_id="<group_id>")

# Export a report to PDF.
reports_service.export_to_file_in_group(
    group_id="<group_id>",
    report_id="<report_id>",
    file_format="PDF",
)
```

### Working with Pipelines

```python
pipelines_service = power_bi_client.pipelines()

# List deployment pipelines.
pipelines = pipelines_service.get_pipelines()

# Deploy all content from Development → Test.
pipelines_service.deploy_all(
    pipeline_id="<pipeline_id>",
    source_stage_order=0,          # Development
    options={"allowOverwriteArtifact": True},
)
```

## Samples

The [`samples/`](samples/) directory contains working examples for every service:

| Sample                                                                 | Service                   |
| ---------------------------------------------------------------------- | ------------------------- |
| [`use_client.py`](samples/use_client.py)                               | Client initialization     |
| [`use_available_features.py`](samples/use_available_features.py)       | Available Features        |
| [`use_capacities.py`](samples/use_capacities.py)                       | Capacities                |
| [`use_dashboards_service.py`](samples/use_dashboards_service.py)       | Dashboards                |
| [`use_dataflows.py`](samples/use_dataflows.py)                         | Dataflows                 |
| [`use_dataflow_storage.py`](samples/use_dataflow_storage.py)           | Dataflow Storage Accounts |
| [`use_datasets.py`](samples/use_datasets.py)                           | Datasets                  |
| [`use_gateways_service.py`](samples/use_gateways_service.py)           | Gateways                  |
| [`use_groups_service.py`](samples/use_groups_service.py)               | Groups                    |
| [`use_imports.py`](samples/use_imports.py)                             | Imports                   |
| [`use_pipelines.py`](samples/use_pipelines.py)                         | Pipelines                 |
| [`use_push_datasets.py`](samples/use_push_datasets.py)                 | Push Datasets             |
| [`use_reports_service.py`](samples/use_reports_service.py)             | Reports                   |
| [`use_template_apps_service.py`](samples/use_template_apps_service.py) | Template Apps             |
| [`use_users_service.py`](samples/use_users_service.py)                 | Users                     |
| [`use_utils.py`](samples/use_utils.py)                                 | Utility classes           |

## Usage

Here is a simple example of using the `powerbi` library.

```python
from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
client_id = config.get('power_bi_api', 'client_id')
redirect_uri = config.get('power_bi_api', 'redirect_uri')
client_secret = config.get('power_bi_api', 'client_secret')

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Initialize the `Dashboards` service.
dashboard_service = power_bi_client.dashboards()

# Add a dashboard to our Workspace.
dashboard_service.add_dashboard(name='my_new_dashboard')

# Get all the dashboards in our Org.
pprint(dashboard_service.get_dashboards())
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).

**Questions:**
If you have questions please feel free to reach out to me at [coding.sigma@gmail.com](mailto:coding.sigma@gmail.com?subject=[GitHub]%20Fred%20Library)
