"""Module for the `Imports` service."""

from enum import Enum
from typing import Union
from typing import Dict
from powerbi.session import PowerBiSession


class Imports:
    """Class for the `Imports` service."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Imports` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def _build_endpoint(self, path: str, group_id: str = None) -> str:
        if group_id:
            return f"/myorg/groups/{group_id}/{path}"
        return f"/myorg/{path}"

    def create_temporary_upload_location(self, group_id: str = None) -> Dict:
        """Creates a temporary blob storage to be used to import large .pbix
        files larger than 1 GB and up to 10 GB.

        ### Overview
        ----
        To import large .pbix files, create a temporary upload location and
        upload the .pbix file using the shared access signature (SAS) url from
        the response, and then call Post Import and specify 'fileUrl' to be the
        SAS url in the Request Body

        ### Parameters
        ----
        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
            A `TemporaryUploadLocation` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.create_temporary_upload_location()
            >>> imports_service.create_temporary_upload_location(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                "imports/createTemporaryUploadLocation", group_id
            ),
        )

        return content

    def get_imports(self, group_id: str = None) -> Dict:
        """Returns a list of imports.

        ### Parameters
        ----
        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
            A collection `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_imports()
            >>> imports_service.get_imports(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint("imports", group_id),
        )

        return content

    def get_import(self, import_id: str, group_id: str = None) -> Dict:
        """Returns the specified import.

        ### Parameters
        ----
        import_id : str
            The import ID you want to query.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
            A `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_import(
                import_id='e40f7c73-84d1-4cf5-a696-5850a5ec8ad3'
            )
            >>> imports_service.get_import(
                import_id='e40f7c73-84d1-4cf5-a696-5850a5ec8ad3',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"imports/{import_id}", group_id),
        )

        return content

    def post_import(
        self,
        dataset_display_name: str,
        name_conflict: Union[str, Enum] = "Ignore",
        skip_report: bool = None,
    ) -> Dict:
        """Creates new content on "My Workspace" from PBIX (Power BI Desktop),
        JSON, XLSX (Excel), RDL or file path in OneDrive for Business.

        ### Parameters
        ----
        dataset_display_name : str
            The display name of the dataset, should include file extension.
            Not supported when importing from OneDrive for Business.

        name_conflict : Union[str, Enum] (optional, Default='Ignore')
            Determines what to do if a dataset with the same name already
            exists. Only `Abort` and `Overwrite` are supported with Rdl files.

        skip_report : bool (optional, Default=None)
            Determines whether to skip report import, if specified value must
            be `True`. Only supported for PBIX files.

        ### Returns
        ----
            A `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.post_import(
                dataset_display_name='my_dataset.pbix',
                name_conflict='Ignore'
            )
        """

        content_types = {"file": "multipart/form-data", "xlsx": "application/json"}

        if isinstance(name_conflict, Enum):
            name_conflict = name_conflict.value

        params = {
            "datasetDisplayName": dataset_display_name,
            "nameConflict": name_conflict,
            "skipReport": skip_report,
        }

        request = self.power_bi_session.build_custom_request()
        request.headers["Content-Type"] = content_types["file"]
        request.data = ""

        content = self.power_bi_session.make_request(
            method="get", endpoint="/myorg/imports", params=params
        )

        return content
