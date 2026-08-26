"""Microsoft Fabric `CopyJob` Items Service."""

from __future__ import annotations

from typing import Dict, List
from powerbi.session import PowerBiSession


class CopyJobs:
    """Class for the `CopyJobs` service.

    ### Overview
    ----
    Wraps the Microsoft Fabric `CopyJob` Items REST API. Unlike the rest of
    this library, Copy Jobs are a Microsoft Fabric resource, not a Power BI
    resource, so requests are sent to the Fabric API host
    (`https://api.fabric.microsoft.com/v1/`) instead of the Power BI host.

    Because of this, the `PowerBiClient` instance used to reach this service
    must be authenticated with a Fabric-compatible scope, for example
    `https://api.fabric.microsoft.com/.default`, rather than the default
    Power BI scope.
    """

    FABRIC_BASE_URL = "https://api.fabric.microsoft.com/v1/"

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `CopyJobs` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    # ------------------------------------------------------------------
    # GET operations
    # ------------------------------------------------------------------

    def get_copy_jobs(
        self,
        workspace_id: str,
        recursive: bool = None,
        root_folder_id: str = None,
        continuation_token: str = None,
    ) -> Dict:
        """Returns a list of Copy Jobs in the specified workspace.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        recursive : bool (optional, Default=None)
            Whether to recursively list Copy Jobs from the folder tree,
            including subfolders.

        root_folder_id : str (optional, Default=None)
            The folder ID to start the search from, if not provided, the
            search starts from the root folder.

        continuation_token : str (optional, Default=None)
            A token for retrieving the next page of results.

        ### Returns
        ----
        Dict
            A collection of `CopyJob` resources.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.get_copy_jobs(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
            )
        """

        params: Dict = {}
        if recursive is not None:
            params["recursive"] = recursive
        if root_folder_id is not None:
            params["rootFolderId"] = root_folder_id
        if continuation_token is not None:
            params["continuationToken"] = continuation_token

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"workspaces/{workspace_id}/copyJobs",
            params=params,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    def get_copy_job(self, workspace_id: str, copy_job_id: str) -> Dict:
        """Returns the specified Copy Job.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        ### Returns
        ----
        Dict
            A `CopyJob` resource.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.get_copy_job(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}",
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    def get_copy_job_definition(
        self, workspace_id: str, copy_job_id: str, format: str = None
    ) -> Dict:
        """Returns the specified Copy Job definition.

        May return a `202 Accepted` response with a `Location`,
        `x-ms-operation-id`, and `Retry-After` header when the request is
        being processed as a Long Running Operation.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        format : str (optional, Default=None)
            The format of the Copy Job definition.

        ### Returns
        ----
        Dict
            A `CopyJobDefinitionResponse` resource, or a Long Running
            Operation status dictionary containing polling headers.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.get_copy_job_definition(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715'
            )
        """

        params: Dict = {}
        if format is not None:
            params["format"] = format

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}/getDefinition",
            params=params,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    # ------------------------------------------------------------------
    # POST operations
    # ------------------------------------------------------------------

    def create_copy_job(
        self,
        workspace_id: str,
        display_name: str,
        definition: Dict = None,
        description: str = None,
        folder_id: str = None,
        sensitivity_label_settings: Dict = None,
    ) -> Dict:
        """Creates a Copy Job in the specified workspace.

        May return a `202 Accepted` response with a `Location`,
        `x-ms-operation-id`, and `Retry-After` header when the request is
        being processed as a Long Running Operation.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        display_name : str
            The Copy Job display name.

        definition : Dict (optional, Default=None)
            The Copy Job public definition.

        description : str (optional, Default=None)
            The Copy Job description. Maximum length is 256 characters.

        folder_id : str (optional, Default=None)
            The folder ID. If not provided, the item is created in the
            workspace root folder.

        sensitivity_label_settings : Dict (optional, Default=None)
            The sensitivity label settings applied to the Copy Job.

        ### Returns
        ----
        Dict
            A `CopyJob` resource, or a Long Running Operation status
            dictionary containing polling headers.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.create_copy_job(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                display_name='CopyJob 1'
            )
        """

        body: Dict = {"displayName": display_name}
        if definition is not None:
            body["definition"] = definition
        if description is not None:
            body["description"] = description
        if folder_id is not None:
            body["folderId"] = folder_id
        if sensitivity_label_settings is not None:
            body["sensitivityLabelSettings"] = sensitivity_label_settings

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"workspaces/{workspace_id}/copyJobs",
            json_payload=body,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    def update_copy_job_definition(
        self,
        workspace_id: str,
        copy_job_id: str,
        definition: Dict,
        update_metadata: bool = None,
    ) -> Dict:
        """Updates the definition of the specified Copy Job.

        May return a `202 Accepted` response with a `Location`,
        `x-ms-operation-id`, and `Retry-After` header when the request is
        being processed as a Long Running Operation.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        definition : Dict
            The Copy Job public definition.

        update_metadata : bool (optional, Default=None)
            When `True`, the item's metadata is updated using the metadata
            in the `.platform` file.

        ### Returns
        ----
        Dict
            A response resource, or a Long Running Operation status
            dictionary containing polling headers.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.update_copy_job_definition(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715',
                definition={'parts': []}
            )
        """

        params: Dict = {}
        if update_metadata is not None:
            params["updateMetadata"] = update_metadata

        body = {"definition": definition}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}/updateDefinition",
            params=params,
            json_payload=body,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    def reset_copy_job(
        self,
        workspace_id: str,
        copy_job_id: str,
        copy_job_entities_to_reset: List[Dict] = None,
        reset_all_copy_job_entities: bool = None,
    ) -> Dict:
        """Resets the specified Copy Job entities so they run as a full
        copy on the next execution.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        copy_job_entities_to_reset : List[Dict] (optional, Default=None)
            A list of `CopyJobEntityReset` resources identifying the
            entities to reset, e.g. `[{'copyJobEntityId': '<id>'}]`.

        reset_all_copy_job_entities : bool (optional, Default=None)
            When `True`, resets all Copy Job entities.

        ### Returns
        ----
        Dict
            An empty response on success.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.reset_copy_job(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715',
                reset_all_copy_job_entities=True
            )
        """

        body: Dict = {}
        if copy_job_entities_to_reset is not None:
            body["copyJobEntitiesToReset"] = copy_job_entities_to_reset
        if reset_all_copy_job_entities is not None:
            body["resetAllCopyJobEntities"] = reset_all_copy_job_entities

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}/resetCopyJob",
            json_payload=body,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    # ------------------------------------------------------------------
    # PATCH operations
    # ------------------------------------------------------------------

    def update_copy_job(
        self,
        workspace_id: str,
        copy_job_id: str,
        display_name: str = None,
        description: str = None,
    ) -> Dict:
        """Updates the properties of the specified Copy Job.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        display_name : str (optional, Default=None)
            The Copy Job display name.

        description : str (optional, Default=None)
            The Copy Job description. Maximum length is 256 characters.

        ### Returns
        ----
        Dict
            The updated `CopyJob` resource.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.update_copy_job(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715',
                display_name='CopyJob 1 renamed'
            )
        """

        body: Dict = {}
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}",
            json_payload=body,
            base_url=self.FABRIC_BASE_URL,
        )

        return content

    # ------------------------------------------------------------------
    # DELETE operations
    # ------------------------------------------------------------------

    def delete_copy_job(
        self, workspace_id: str, copy_job_id: str, hard_delete: bool = None
    ) -> Dict:
        """Deletes the specified Copy Job.

        ### Parameters
        ----
        workspace_id : str
            The workspace ID.

        copy_job_id : str
            The Copy Job ID.

        hard_delete : bool (optional, Default=None)
            When `True`, the Copy Job is permanently deleted immediately,
            bypassing the recycle bin.

        ### Returns
        ----
        Dict
            An empty response on success.

        ### Usage
        ----
            >>> copy_jobs_service = power_bi_client.copy_jobs()
            >>> copy_jobs_service.delete_copy_job(
                workspace_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                copy_job_id='5b218778-e7a5-4d73-8187-f10824047715'
            )
        """

        params: Dict = {}
        if hard_delete is not None:
            params["hardDelete"] = hard_delete

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"workspaces/{workspace_id}/copyJobs/{copy_job_id}",
            params=params,
            base_url=self.FABRIC_BASE_URL,
        )

        return content
