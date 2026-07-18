"""The Unofficial Python API wrapper for the Microsoft Power BI REST API."""

from __future__ import annotations

from powerbi.client import PowerBiClient
from powerbi.token_provider import StaticTokenProvider, TokenProvider
from powerbi.enums import (
    ColumnAggregationMethods,
    ColumnDataTypes,
    ComputeEngineBehavior,
    CredentialTypes,
    DatasetModes,
    DataSourceType,
    EncryptedConnections,
    EncryptionAlgorithm,
    ExportFileFormats,
    GatewayDataSourceAccessRights,
    GatewayPrincipalType,
    GatewayServicePrincipalProfile,
    GroupUserAccessRights,
    ImportConflictHandlerMode,
    NotifyOption,
    PrincipalType,
    PrivacyLevels,
    WorkloadStates,
)
from powerbi.utils import (
    Column,
    Columns,
    CredentialDetails,
    DataSource,
    DataSources,
    Dataset,
    Measure,
    Measures,
    Relationship,
    Relationships,
    Table,
    Tables,
)

__all__ = [
    # Client
    "PowerBiClient",
    # Token providers
    "TokenProvider",
    "StaticTokenProvider",
    # Enums
    "ColumnAggregationMethods",
    "ColumnDataTypes",
    "ComputeEngineBehavior",
    "CredentialTypes",
    "DatasetModes",
    "DataSourceType",
    "EncryptedConnections",
    "EncryptionAlgorithm",
    "ExportFileFormats",
    "GatewayDataSourceAccessRights",
    "GatewayPrincipalType",
    "GatewayServicePrincipalProfile",
    "GroupUserAccessRights",
    "ImportConflictHandlerMode",
    "NotifyOption",
    "PrincipalType",
    "PrivacyLevels",
    "WorkloadStates",
    # Utility classes
    "Column",
    "Columns",
    "CredentialDetails",
    "DataSource",
    "DataSources",
    "Dataset",
    "Measure",
    "Measures",
    "Relationship",
    "Relationships",
    "Table",
    "Tables",
]
