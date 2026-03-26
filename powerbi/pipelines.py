"""Microsoft PowerBi `Pipeline` Service."""

from typing import Dict, List
from powerbi.session import PowerBiSession


class Pipelines:
    """Class for the `Pipelines` service."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Pipelines` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    # ------------------------------------------------------------------
    # GET operations
    # ------------------------------------------------------------------

    def get_pipelines(self) -> Dict:
        """Returns a list of deployment pipelines the user has access to.

        ### Returns
        ----
        Dict
            A collection of `DeploymentPipeline` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipelines()
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/pipelines",
        )

        return content

    def get_pipeline(self, pipeline_id: str, expand_stages: bool = True) -> Dict:
        """Returns the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        expand_stages : bool (optional, Default=True)
            Expands related entities inline, receives a comma-separated list
            of data types.

        ### Returns
        ----
        Dict
            A `DeploymentPipeline` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
            )
        """

        if expand_stages:
            url = f"myorg/pipelines/{pipeline_id}?$expand=stages"
        else:
            url = f"myorg/pipelines/{pipeline_id}"

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=url,
        )

        return content

    def get_pipeline_operations(self, pipeline_id: str) -> Dict:
        """Returns a list of the up-to-20 most recent deploy operations
        performed on the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        ### Returns
        ----
        Dict
            A collection of `PipelineOperation` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_operations(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/pipelines/{pipeline_id}/operations",
        )

        return content

    def get_pipeline_operation(self, pipeline_id: str, operation_id: str) -> Dict:
        """Returns the details of the specified deploy operation performed
        on the specified deployment pipeline, including the deployment
        execution plan. Use to track the status of the deploy operation.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        operation_id : str
            The operation ID.

        ### Returns
        ----
        Dict
            A `PipelineOperation` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_operation(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                operation_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/pipelines/{pipeline_id}/operations/{operation_id}",
        )

        return content

    def get_pipeline_stages(self, pipeline_id: str) -> Dict:
        """Returns the stages of the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        ### Returns
        ----
        Dict
            A collection of `PipelineStage` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_stages(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/pipelines/{pipeline_id}/stages",
        )

        return content

    def get_pipeline_stage_artifacts(self, pipeline_id: str, stage_order: int) -> Dict:
        """Returns the supported items from the workspace assigned to the
        specified stage of the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        stage_order : int
            The deployment pipeline stage order. Development (0),
            Test (1), Production (2).

        ### Returns
        ----
        Dict
            A collection of pipeline stage artifact resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_stage_artifacts(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                stage_order=1
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/pipelines/{pipeline_id}/stages/{stage_order}/artifacts",
        )

        return content

    def get_pipeline_users(self, pipeline_id: str) -> Dict:
        """Returns a list of users that have access to the specified
        deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        ### Returns
        ----
        Dict
            A collection of `PipelineUser` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_users(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/pipelines/{pipeline_id}/users",
        )

        return content

    # ------------------------------------------------------------------
    # POST operations
    # ------------------------------------------------------------------

    def create_pipeline(
        self, display_name: str, description: str = None
    ) -> Dict:
        """Creates a new deployment pipeline.

        ### Parameters
        ----
        display_name : str
            The display name for the new deployment pipeline.
            Max length: 256.

        description : str (optional)
            The description for the new deployment pipeline.
            Max length: 1024.

        ### Returns
        ----
        Dict
            A `Pipeline` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.create_pipeline(
                display_name='My Deployment Pipeline',
                description='Pipeline for deploying reports.'
            )
        """

        body = {"displayName": display_name}
        if description is not None:
            body["description"] = description

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/pipelines",
            json_payload=body,
        )

        return content

    def deploy_all(
        self,
        pipeline_id: str,
        source_stage_order: int,
        options: Dict = None,
        note: str = None,
        is_backward_deployment: bool = None,
        new_workspace: Dict = None,
        update_app_settings: Dict = None,
    ) -> Dict:
        """Deploys all supported items from the source stage of the
        specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        source_stage_order : int
            The numeric identifier of the pipeline deployment stage
            that the content should be deployed from. Development (0),
            Test (1), Production (2).

        options : dict (optional)
            Options that control the behavior of the entire deployment.
            Keys: allowOverwriteArtifact, allowCreateArtifact,
            allowOverwriteTargetArtifactLabel, allowPurgeData,
            allowSkipTilesWithMissingPrerequisites, allowTakeOver.

        note : str (optional)
            A note describing the deployment.

        is_backward_deployment : bool (optional)
            Whether the deployment will be from a later stage to an
            earlier one. Default is False.

        new_workspace : dict (optional)
            Configuration details for creating a new workspace when
            deploying to a stage with no assigned workspace.
            Keys: name, capacityId.

        update_app_settings : dict (optional)
            Configuration for updating the org app after deployment.
            Keys: updateAppInTargetWorkspace.

        ### Returns
        ----
        Dict
            A `PipelineOperation` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.deploy_all(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                source_stage_order=0,
                options={
                    'allowOverwriteArtifact': True,
                    'allowCreateArtifact': True
                },
                note='Deploying business ready items'
            )
        """

        body: Dict = {"sourceStageOrder": source_stage_order}
        if options is not None:
            body["options"] = options
        if note is not None:
            body["note"] = note
        if is_backward_deployment is not None:
            body["isBackwardDeployment"] = is_backward_deployment
        if new_workspace is not None:
            body["newWorkspace"] = new_workspace
        if update_app_settings is not None:
            body["updateAppSettings"] = update_app_settings

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/pipelines/{pipeline_id}/deployAll",
            json_payload=body,
        )

        return content

    def selective_deploy(
        self,
        pipeline_id: str,
        source_stage_order: int,
        datasets: List[Dict] = None,
        reports: List[Dict] = None,
        dashboards: List[Dict] = None,
        dataflows: List[Dict] = None,
        datamarts: List[Dict] = None,
        options: Dict = None,
        note: str = None,
        is_backward_deployment: bool = None,
        new_workspace: Dict = None,
        update_app_settings: Dict = None,
    ) -> Dict:
        """Deploys the specified items from the source stage of the
        specified deployment pipeline. Maximum 300 deployed items per
        request.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        source_stage_order : int
            The numeric identifier of the pipeline deployment stage
            that the content should be deployed from. Development (0),
            Test (1), Production (2).

        datasets : list of dict (optional)
            A list of datasets to be deployed. Each dict must contain
            a 'sourceId' key, and may contain an 'options' key.

        reports : list of dict (optional)
            A list of reports to be deployed.

        dashboards : list of dict (optional)
            A list of dashboards to be deployed.

        dataflows : list of dict (optional)
            A list of dataflows to be deployed.

        datamarts : list of dict (optional)
            A list of datamarts to be deployed.

        options : dict (optional)
            Options that control the behavior of the entire deployment.

        note : str (optional)
            A note describing the deployment.

        is_backward_deployment : bool (optional)
            Whether the deployment will be from a later stage to an
            earlier one. Default is False.

        new_workspace : dict (optional)
            Configuration details for creating a new workspace when
            deploying to a stage with no assigned workspace.

        update_app_settings : dict (optional)
            Configuration for updating the org app after deployment.

        ### Returns
        ----
        Dict
            A `PipelineOperation` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.selective_deploy(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                source_stage_order=0,
                reports=[{'sourceId': '2d225191-65f8-4ec3-b77d-06100602b1f7'}],
                options={
                    'allowOverwriteArtifact': True,
                    'allowCreateArtifact': True
                },
                note='Deploying selected items'
            )
        """

        body: Dict = {"sourceStageOrder": source_stage_order}
        if datasets is not None:
            body["datasets"] = datasets
        if reports is not None:
            body["reports"] = reports
        if dashboards is not None:
            body["dashboards"] = dashboards
        if dataflows is not None:
            body["dataflows"] = dataflows
        if datamarts is not None:
            body["datamarts"] = datamarts
        if options is not None:
            body["options"] = options
        if note is not None:
            body["note"] = note
        if is_backward_deployment is not None:
            body["isBackwardDeployment"] = is_backward_deployment
        if new_workspace is not None:
            body["newWorkspace"] = new_workspace
        if update_app_settings is not None:
            body["updateAppSettings"] = update_app_settings

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/pipelines/{pipeline_id}/deploy",
            json_payload=body,
        )

        return content

    def assign_workspace(
        self, pipeline_id: str, stage_order: int, workspace_id: str
    ) -> None:
        """Assigns the specified workspace to the specified deployment
        pipeline stage.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        stage_order : int
            The deployment pipeline stage order. Development (0),
            Test (1), Production (2).

        workspace_id : str
            The workspace ID.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.assign_workspace(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                stage_order=0,
                workspace_id='4de5bcc4-2c88-4efe-b827-4ee7b289b496'
            )
        """

        body = {"workspaceId": workspace_id}

        self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/pipelines/{pipeline_id}/stages/{stage_order}/assignWorkspace",
            json_payload=body,
        )

    def unassign_workspace(self, pipeline_id: str, stage_order: int) -> None:
        """Unassigns the workspace from the specified stage in the
        specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        stage_order : int
            The deployment pipeline stage order. Development (0),
            Test (1), Production (2).

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.unassign_workspace(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                stage_order=0
            )
        """

        self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/pipelines/{pipeline_id}/stages/{stage_order}/unassignWorkspace",
        )

    def update_pipeline_user(
        self,
        pipeline_id: str,
        identifier: str,
        principal_type: str,
        access_right: str = "Admin",
    ) -> None:
        """Grants user permissions to the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        identifier : str
            For principal type User, provide the UPN. Otherwise
            provide the object ID of the principal.

        principal_type : str
            The principal type. Valid values: 'User', 'Group', 'App'.

        access_right : str (optional, Default='Admin')
            The access right to grant. Currently only 'Admin' is
            supported.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.update_pipeline_user(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                identifier='john@contoso.com',
                principal_type='User',
                access_right='Admin'
            )
        """

        body = {
            "identifier": identifier,
            "accessRight": access_right,
            "principalType": principal_type,
        }

        self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/pipelines/{pipeline_id}/users",
            json_payload=body,
        )

    # ------------------------------------------------------------------
    # PATCH operations
    # ------------------------------------------------------------------

    def update_pipeline(
        self,
        pipeline_id: str,
        display_name: str = None,
        description: str = None,
    ) -> Dict:
        """Updates the specified deployment pipeline. An updated display
        name and/or a description is required.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        display_name : str (optional)
            The updated display name for the deployment pipeline.
            Max length: 256.

        description : str (optional)
            The updated description for the deployment pipeline.
            Max length: 1024.

        ### Returns
        ----
        Dict
            A `Pipeline` resource.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.update_pipeline(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                display_name='Updated Pipeline Name',
                description='Updated description'
            )
        """

        body: Dict = {}
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=f"myorg/pipelines/{pipeline_id}",
            json_payload=body,
        )

        return content

    # ------------------------------------------------------------------
    # DELETE operations
    # ------------------------------------------------------------------

    def delete_pipeline(self, pipeline_id: str) -> None:
        """Deletes the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.delete_pipeline(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
            )
        """

        self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/pipelines/{pipeline_id}",
        )

    def delete_pipeline_user(
        self, pipeline_id: str, identifier: str
    ) -> None:
        """Removes user permissions from the specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        identifier : str
            To delete user pipeline permissions, provide the user
            principal name (UPN). To delete a service principal or
            security group's permissions, provide the Object ID.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.delete_pipeline_user(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                identifier='john@contoso.com'
            )
        """

        self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/pipelines/{pipeline_id}/users/{identifier}",
        )
