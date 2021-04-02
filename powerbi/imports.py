from enum import Enum
from typing import Union
from typing import Dict
from powerbi.session import PowerBiSession


class Imports():

    def __init__(self, session: object) -> None:
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

    def create_temporary_upload_location(self) -> Dict:
        """Creates a temporary blob storage to be used to import large .pbix
        files larger than 1 GB and up to 10 GB.

        ### Overview
        ----
        To import large .pbix files, create a temporary upload location and
        upload the .pbix file using the shared access signature (SAS) url from
        the response, and then call Post Import and specify 'fileUrl' to be the
        SAS url in the Request Body

        ### Returns
        ----
            A `TemporaryUploadLocation` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.create_temporary_upload_location()
        """

        content = self.power_bi_session.make_request(
            method='post',
            endpoint='myorg/imports/createTemporaryUploadLocation'
        )

        return content

    def create_group_temporary_upload_location(self, group_id: str) -> Dict:
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
        group_id : str
            The Workspace ID.

        ### Returns
        ----
            A `TemporaryUploadLocation` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.create_group_temporary_upload_location(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'/myorg/groups/{group_id}/imports/createTemporaryUploadLocation'
        )

        return content

    def get_imports(self) -> Dict:
        """Returns a list of imports from "My Workspace".

        ### Returns
        ----
            A collection `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_imports()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'/myorg/imports'
        )

        return content

    def get_group_imports(self, group_id: str) -> Dict:
        """Returns a list of imports from the specified workspace.

        ### parameters
        ----
        group_id : str
            The workspace ID.

        ### Returns
        ----
            A collection `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_group_imports(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'/myorg/groups/{group_id}/imports'
        )

        return content

    def get_import(self, import_id: str) -> Dict:
        """Returns the specified import from "My Workspace".

        ### Parameters
        ----
        import_id : str
            The import ID you want to query.

        ### Returns
        ----
            A `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_import(
                import_id='e40f7c73-84d1-4cf5-a696-5850a5ec8ad3'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'/myorg/imports/{import_id}'
        )

        return content

    def get_group_import(self, group_id: str, import_id: str) -> Dict:
        """Returns the specified import from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        import_id : str
            The import ID you want to query.

        ### Returns
        ----
            A `Import` resource.

        ### Usage
        ----
            >>> imports_service = power_bi_client.imports()
            >>> imports_service.get_group_import(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                import_id='e40f7c73-84d1-4cf5-a696-5850a5ec8ad3'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'/myorg/groups/{group_id}/imports/{import_id}'
        )

        return content

