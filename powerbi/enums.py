import json
from enum import Enum

# https://docs.microsoft.com/en-us/rest/api/power-bi/datasets/getdatasources


class ColumnDataTypes(Enum):
    """Represents all the data types you can use
    when creating a new column in a `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnDataTypes
        >>> ColumnDataTypes.Int64.value
    """

    Int64 = 'Int64'
    Double = 'Double'
    Boolean = 'bool'
    Datetime = 'DateTime'
    String = 'string'
    Decimal = 'Decimal'


class ColumnAggregationMethods(Enum):
    """Represents all the aggregation methods you can
    use  when creating aggregating a new column in a
    `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnAggregationMethods
        >>> ColumnAggregationMethods.Count.value
    """

    Default = 'default'
    Null = 'none'
    Sum = 'sum'
    Min = 'min'
    Max = 'max'
    Count = 'count'
    Average = 'average'
    DistinctCount = 'distinctCount'


class DatasetModes(Enum):
    """Represents all the dataset modes you can
    use when creating a new `PowerBiDataset`

    ### Usage:
    ----
        >>> from powerbi.enums import DatasetModes
        >>> DatasetModes.AsAzure.value
    """

    AsAzure = 'AsAzure'
    AsOnPrem = 'AsOnPrem'
    Push = 'Push'
    PushStreaming = 'PushStreaming'
    Streaming = 'Streaming'


class DataSourceType(Enum):
    """Represents all the datasource type you can
    use when creating a new `PowerBiDataset`

    ### Usage:
    ----
        >>> from powerbi.enums import DataSourceType
        >>> DataSourceType.Web.value
    """

    AnalysisServices = 'AnalysisServices'
    Sql = 'Sql'
    File = 'File'
    OData = 'OData'
    Oracle = 'Oracle'
    SAPHana = 'SAPHana'
    SharePointList = 'SharePointList'


class GroupUserAccessRights(Enum):
    """Represents all the GroupUserAccessRights type you can
    use when creating a new `PowerBiGroupUser`.

    For more info, go to:
    https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#groupuseraccessright

    ### Usage:
    ----
        >>> from powerbi.enums import GroupUserAccessRights
        >>> GroupUserAccessRights.Admin.value
    """

    Admin = 'Admin'
    Contributor = 'Contributor'
    Member = 'Member'
    Remove = None
    Viewer = 'Viewer'


class PrincipalType(Enum):
    """Represents all the PrincipalTypes you can
    use when creating a new `PowerBiGroupUser`.

    For more info, go to:
    https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#principaltype

    ### Usage:
    ----
        >>> from powerbi.enums import PrincipalType
        >>> PrincipalType.App.value
    """

    App = 'App'
    Group = 'Group'
    User = 'User'


class ImportConflictHandlerMode(Enum):
    """Represents all the ImportConflictHandlerMode you can
    use when creating a new `PowerBiImport`.

    For more info, go to:
    https://docs.microsoft.com/en-us/rest/api/power-bi/imports/postimport#importconflicthandlermode

    ### Usage:
    ----
        >>> from powerbi.enums import ImportConflictHandlerMode
        >>> ImportConflictHandlerMode.Abort.value
    """

    Abort = 'Abort'
    CreateOrOverwrite = 'CreateOrOverwrite'
    GenerateUniqueName = 'GenerateUniqueName'
    Ignore = 'Ignore'
    Overwrite = 'Overwrite'

class ExportFileFormats(Enum):
    """Represents all the File Formats you can
    export a `PowerBiReport` to.

    ### Usage:
    ----
        >>> from powerbi.enums import ExportFileFormats
        >>> ExportFileFormats.Pdf.value
    """

    AccessiblePdf = 'ACCESSIBLEPDF'
    Csv = 'CSV'
    WordDocument = 'DOCX'
    Image = 'IMAGE'
    MHTML = 'MHTML'
    Pdf = 'PDF'
    Png = 'PNG'
    PowerPointDocument = 'PPTX'
    ExcelDocument = 'XLSX'
    Xml = 'XML'
