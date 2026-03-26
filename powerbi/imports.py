"""Module for the `Imports` service."""

import os
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
        import_file: str = None,
        file_url: str = None,
        onedrive_file_path: str = None,
        connection_type: str = None,
        name_conflict: Union[str, Enum] = "Ignore",
        skip_report: bool = None,
        override_report_label: bool = None,
        override_model_label: bool = None,
        subfolder_object_id: str = None,
        group_id: str = None,
    ) -> Dict:
        """Creates new content by importing a file.

        ### Overview
        ----
        Supports three import modes:

        1. **File upload** — Pass `import_file` with a local file path
           (.pbix, .json, .xlsx, .rdl). The file is uploaded as
           multipart/form-data.
        2. **Large file** — First call `create_temporary_upload_location`
           to get a SAS URL, upload the file to that URL, then pass
           the SAS URL as `file_url`. For .pbix files between 1-10 GB.
        3. **OneDrive for Business** — Pass `onedrive_file_path` with
           the path to an .xlsx file on OneDrive for Business.

        ### Parameters
        ----
        dataset_display_name : str
            The display name of the dataset, should include file extension.
            Not supported when importing from OneDrive for Business.

        import_file : str (optional, Default=None)
            Local file path to upload via multipart/form-data.

        file_url : str (optional, Default=None)
            The SAS URL from `create_temporary_upload_location` for
            importing large .pbix files (1-10 GB).

        onedrive_file_path : str (optional, Default=None)
            The path of the OneDrive for Business Excel (.xlsx) file
            to import. Power BI .pbix files aren't supported via OneDrive.

        connection_type : str (optional, Default=None)
            The import connection type for a OneDrive for Business file.
            Can be 'import' or 'connect'.

        name_conflict : Union[str, Enum] (optional, Default='Ignore')
            Determines what to do if a dataset with the same name already
            exists. Options: Ignore, Abort, Overwrite, CreateOrOverwrite,
            GenerateUniqueName. For RDL files, only Abort and Overwrite
            are supported.

        skip_report : bool (optional, Default=None)
            Whether to skip report import. If specified, the value must
            be True. Only supported for PBIX files.

        override_report_label : bool (optional, Default=None)
            Whether to override the existing label on a report when
            republishing a Power BI .pbix file.

        override_model_label : bool (optional, Default=None)
            Whether to override the existing label on a model when
            republishing a Power BI .pbix file.

        subfolder_object_id : str (optional, Default=None)
            The subfolder ID to import the file into.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            An `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()

            >>> # Upload a local .pbix file
            >>> imports_service.post_import(
                dataset_display_name='MyReport.pbix',
                import_file='C:/reports/MyReport.pbix',
                name_conflict='Overwrite'
            )

            >>> # Import a large file via SAS URL
            >>> location = imports_service.create_temporary_upload_location()
            >>> imports_service.post_import(
                dataset_display_name='LargeReport.pbix',
                file_url=location['url'],
                name_conflict='CreateOrOverwrite',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        if isinstance(name_conflict, Enum):
            name_conflict = name_conflict.value

        params = {
            "datasetDisplayName": dataset_display_name,
            "nameConflict": name_conflict,
            "skipReport": skip_report,
            "overrideReportLabel": override_report_label,
            "overrideModelLabel": override_model_label,
            "subfolderObjectId": subfolder_object_id,
        }

        # Remove None values so they aren't sent as query params.
        params = {k: v for k, v in params.items() if v is not None}

        endpoint = self._build_endpoint("imports", group_id)

        # Mode 1: Local file upload via multipart/form-data.
        if import_file:
            file_name = os.path.basename(import_file)
            with open(import_file, "rb") as f:
                content = self.power_bi_session.make_request(
                    method="post",
                    endpoint=endpoint,
                    params=params,
                    files={"file": (file_name, f)},
                )
            return content

        # Mode 2: Large file via SAS URL.
        if file_url:
            content = self.power_bi_session.make_request(
                method="post",
                endpoint=endpoint,
                params=params,
                json_payload={"fileUrl": file_url},
            )
            return content

        # Mode 3: OneDrive for Business import.
        if onedrive_file_path:
            body = {"filePath": onedrive_file_path}
            if connection_type:
                body["connectionType"] = connection_type

            content = self.power_bi_session.make_request(
                method="post",
                endpoint=endpoint,
                params=params,
                json_payload=body,
            )
            return content

        raise ValueError(
            "One of 'import_file', 'file_url', or 'onedrive_file_path' must be provided."
        )
