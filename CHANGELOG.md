# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Clean public API exports in `powerbi/__init__.py` — all client, enum, and utility
  classes can now be imported directly from `powerbi`.
- PEP 561 `py.typed` marker for inline type-checking support.
- `config/config.ini.example` template with placeholder credentials.
- `CHANGELOG.md` (this file).
- `CONTRIBUTING.md` with development setup and contribution guidelines.
- GitHub Actions CI workflow testing Python 3.9 – 3.13.
- `samples/use_gateways_service.py` example file.
- **reports**: `bind_to_gateway` — binds a paginated report data source to a gateway
  (supports both My Workspace and In Group).
- **reports**: `rebind_report` — rebinds a report to a different dataset
  (supports both My Workspace and In Group).
- **reports**: `take_over_in_group` — transfers ownership of paginated report data
  sources to the current authorized user.
- **reports**: `update_datasources` — updates data sources of a paginated report (RDL)
  (supports both My Workspace and In Group).
- **reports**: `get_export_to_file_status` — returns the status of an Export to File job
  (supports both My Workspace and In Group).
- **reports**: `get_file_of_export_to_file` — returns the file from an Export to File job
  (supports both My Workspace and In Group).
- **reports**: `update_report_content` — updates report content from a source report
  (supports both My Workspace and In Group; replaces `update_report_content_in_group`).

### Fixed
- **push_datasets**: `post_dataset` now sends JSON body (`json_payload=`) instead of
  form-encoded `data=`; `defaultRetentionPolicy` moved to query params.
- **push_datasets**: `post_dataset_rows` now wraps rows in the required `{"rows": [...]}` envelope.
- **push_datasets**: `put_dataset` uses `Table.to_dict()` and no longer mutates the
  original `Table` object.
- **utils**: `Measure.expression` getter returned wrong dict key.
- **utils**: `Table.add_measure` was decorated as `@property` instead of being a method.
- **utils**: `DataSource.__init__` crashed when setting properties before the backing
  dict was created.
- **utils**: `Column.to_json()` returned a `dict`, not a JSON string.
- **utils**: `Measures.__setitem__` and `Relationships.__setitem__` crashed on type
  validation.
- **utils**: `CredentialDetails.to_dict()` returned all dataclass fields instead of
  just `credential_details`.
- **utils**: 12 incorrect type hints across `Column`, `Table`, `Dataset`, `Measures`,
  `Relationships`, and `Tables`.
- **utils**: Removed dead code (`ConnectionDetails` empty class, duplicate `Dataset` in
  `PowerBiEncoder`, unused `asdict` import).
- **gateways**: `add_datasource_user` None-guard for optional enum parameters.
- **enums**: Corrected 3 docstring issues (wrong import path, wrong class name,
  outdated `docs.microsoft.com` URLs).

### Changed
- Minimum Python version is now **3.9** (previously 3.6).
- Packaging moved from `setup.py` to `pyproject.toml` (PEP 621).
- **reports**: `get_datasources` now supports `group_id` parameter for workspace-scoped
  calls (previously only supported My Workspace).
- **reports**: `export_to_file` now supports `group_id` parameter for workspace-scoped
  calls (previously only supported My Workspace).
- **reports**: `update_report_content_in_group` renamed to `update_report_content` with
  optional `group_id` parameter, supporting both My Workspace and In Group variants.

## [0.1.2] - 2024-01-15

### Added
- Pipelines service with 16 methods covering all deployment pipeline operations.
- Gateways service with 11 methods covering all gateway operations.
- `datasets.py` expanded with full API coverage.
- `imports.py` rewritten to match current API spec.
- ANSI-colored `HTTPError` messages for improved terminal readability.
- Method duplication refactor across service modules.

## [0.1.1] - 2023-06-01

### Added
- Initial service classes: Apps, Dashboards, Dataflows, Dataflow Storage, Datasets,
  Groups, Imports, Push Datasets, Reports, Template Apps, Users.
- `PowerBiClient` with lazy service initialization.
- `PowerBiAuth` with MSAL confidential client flow.
- `PowerBiSession` with persistent `requests.Session`.
- Utility classes: `Column`, `Table`, `Dataset`, `Measure`, `Relationship`.
- Enum classes for column types, dataset modes, data source types, etc.
- 15 sample files demonstrating each service.

## [0.1.0] - 2023-01-01

### Added
- Initial release with core authentication and basic API coverage.

[Unreleased]: https://github.com/areed1192/power-bi-python-api/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/areed1192/power-bi-python-api/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/areed1192/power-bi-python-api/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/areed1192/power-bi-python-api/releases/tag/v0.1.0
