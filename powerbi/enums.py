"""Power BI Python SDK Enums"""

from enum import Enum


class ColumnDataTypes(Enum):
    """Represents all the data types you can use
    when creating a new column in a `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnDataTypes
        >>> ColumnDataTypes.INT64.value
    """

    INT64 = "Int64"
    DOUBLE = "Double"
    BOOLEAN = "bool"
    DATETIME = "DateTime"
    STRING = "string"
    DECIMAL = "Decimal"


class ColumnAggregationMethods(Enum):
    """Represents all the aggregation methods you can
    use  when creating aggregating a new column in a
    `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnAggregationMethods
        >>> ColumnAggregationMethods.COUNT.value
    """

    DEFAULT = "default"
    NULL = "none"
    SUM = "sum"
    MIN = "min"
    MAX = "max"
    COUNT = "count"
    AVERAGE = "average"
    DISTINCT_COUNT = "distinctCount"


class DatasetModes(Enum):
    """Represents all the dataset modes you can
    use when creating a new `PowerBiDataset`

    ### Usage:
    ----
        >>> from powerbi.enums import DatasetModes
        >>> DatasetModes.AS_AZURE.value
    """

    AS_AZURE = "AsAzure"
    AS_ON_PREM = "AsOnPrem"
    PUSH = "Push"
    PUSH_STREAMING = "PushStreaming"
    STREAMING = "Streaming"


class DataSourceType(Enum):
    """Represents all the datasource type you can
    use when creating a new `PowerBiDataset`

    ### Usage:
    ----
        >>> from powerbi.enums import DataSourceType
        >>> DataSourceType.SQL.value
    """

    ANALYSIS_SERVICES = "AnalysisServices"
    SQL = "Sql"
    FILE = "File"
    ODATA = "OData"
    ORACLE = "Oracle"
    SAP_HANA = "SAPHana"
    SHAREPOINT_LIST = "SharePointList"


class GroupUserAccessRights(Enum):
    """Represents all the GroupUserAccessRights type you can
    use when creating a new `PowerBiGroupUser`.

    For more info, go to:
    https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#groupuseraccessright

    ### Usage:
    ----
        >>> from powerbi.enums import GroupUserAccessRights
        >>> GroupUserAccessRights.ADMIN.value
    """

    ADMIN = "Admin"
    CONTRIBUTOR = "Contributor"
    MEMBER = "Member"
    REMOVE = None
    VIEWER = "Viewer"


class PrincipalType(Enum):
    """Represents all the PrincipalTypes you can
    use when creating a new `PowerBiGroupUser`.

    For more info, go to:
    https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#principaltype

    ### Usage:
    ----
        >>> from powerbi.enums import PrincipalType
        >>> PrincipalType.APP.value
    """

    APP = "App"
    GROUP = "Group"
    USER = "User"
    NONE = "None"


class ImportConflictHandlerMode(Enum):
    """Represents all the ImportConflictHandlerMode you can
    use when creating a new `PowerBiImport`.

    ### Usage:
    ----
        >>> from powerbi.enums import ImportConflictHandlerMode
        >>> ImportConflictHandlerMode.ABORT.value
    """

    ABORT = "Abort"
    CREATE_OR_OVERWRITE = "CreateOrOverwrite"
    GENERATE_UNIQUE_NAME = "GenerateUniqueName"
    IGNORE = "Ignore"
    OVERWRITE = "Overwrite"


class ExportFileFormats(Enum):
    """Represents all the File Formats you can
    export a `PowerBiReport` to.

    ### Usage:
    ----
        >>> from powerbi.enums import ExportFileFormats
        >>> ExportFileFormats.PDF.value
    """

    ACCESSIBLE_PDF = "ACCESSIBLEPDF"
    CSV = "CSV"
    DOCX = "DOCX"
    IMAGE = "IMAGE"
    MHTML = "MHTML"
    PDF = "PDF"
    PNG = "PNG"
    PPTX = "PPTX"
    XLSX = "XLSX"
    XML = "XML"


class GatewayDataSourceAccessRights(Enum):
    """Represents all the Gateway Data Source Access Rights you can
    use when creating a new `PowerBiGatewayDataSourceUser`.

    ### Usage:
    ----
        >>> from powerbi.enums import GatewayDataSourceAccessRights
        >>> GatewayDataSourceAccessRights.READ.value
    """

    READ = "Read"
    READ_OVERRIDE_EFFECTIVE_IDENTITY = "ReadOverrideEffectiveIdentity"
    NONE = None


class GatewayPrincipalType(Enum):
    """Represents all the Gateway Principal Types you can
    use when creating a new `PowerBiGatewayDataSourceUser`.

    ### Usage:
    ----
        >>> from powerbi.enums import GatewayPrincipalType
        >>> GatewayPrincipalType.APP.value
    """

    APP = "App"
    GROUP = "Group"
    NONE = "None"
    USER = "User"


class GatewayServicePrincipalProfile(Enum):
    """Represents all the Gateway ServicePrincipalProfile you can
    use when creating a new `PowerBiGatewayDataSourceUser`.

    ### Usage:
    ----
        >>> from powerbi.enums import GatewayServicePrincipalProfile
        >>> GatewayServicePrincipalProfile.DISPLAY_NAME.value
    """

    DISPLAY_NAME = "displayName"
    ID = "id"


class CredentialTypes(Enum):
    """Represents all the Credential Types you can
    use when creating a new `PowerBiGatewayDataSource`.

    ### Usage:
    ----
        >>> from powerbi.enums import CredentialTypes
        >>> CredentialTypes.BASIC.value
    """

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"
    KEY = "Key"
    OAUTH2 = "OAuth2"
    SAS = "SAS"
    WINDOWS = "Windows"


class EncryptedConnections(Enum):
    """Represents all the Encrypted Connections you can
    use when creating a new `PowerBiGatewayDataSource`.

    ### Overview:
    ----
    Whether to encrypt the data source connection. The API
    call will fail if you select encryption and Power BI
    is unable to establish an encrypted connection with
    the data source.

    ### Usage:
    ----
        >>> from powerbi.enums import EncryptedConnections
        >>> EncryptedConnections.ENCRYPTED.value
    """

    ENCRYPTED = "Encrypted"
    NOT_ENCRYPTED = "NotEncrypted"


class EncryptionAlgorithm(Enum):
    """Represents all the Encryption Algorithm you can
    use when creating a new `PowerBiGatewayDataSource`.

    ### Usage:
    ----
        >>> from powerbi.enums import EncryptionAlgorithm
        >>> EncryptionAlgorithm.RSA_OAEP.value
    """

    NONE = "None"
    RSA_OAEP = "RSA-OAEP"


class PrivacyLevels(Enum):
    """Represents all the Privacy Levels you can
    use when creating a new `PowerBiGatewayDataSource`.

    ### Usage:
    ----
        >>> from powerbi.enums import PrivacyLevels
        >>> PrivacyLevels.PUBLIC.value
    """

    PUBLIC = "Public"
    ORGANIZATIONAL = "Organizational"
    PRIVATE = "Private"
    NONE = "None"
