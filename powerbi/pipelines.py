import json

from typing import Dict
from typing import Union
from powerbi.utils import Dataset
from powerbi.utils import Table
from powerbi.utils import PowerBiEncoder
from powerbi.session import PowerBiSession
from enum import Enum


class Pipelines():

    def __init__(self, session: object) -> None:
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

    def get_pipelines(self) -> Dict:
        """Returns a list of deployment `pipelines` the user has access to.

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
            method='get',
            endpoint=f'myorg/pipelines',
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
            url = f'myorg/pipelines/{pipeline_id}?$expand=stages'
        else:
            url = f'myorg/pipelines/{pipeline_id}',

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=url,
        )

        return content

    def get_pipeline_operations(self, pipeline_id: str) -> Dict:
        """Returns a list of up to 20 last deploy operations performed on
        the specified deployment pipeline.

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
            method='get',
            endpoint=f'myorg/pipelines/{pipeline_id}/operations',
        )

        return content

    def get_pipeline_operation(self, pipeline_id: str, operation_id: str) -> Dict:
        """Returns the details of the specified deploy operation performed
        on the specified deployment pipeline including the executionPlan.
        Use to track the status of the deploy operation.

        ### Parameters
        ----
        pipeline_id : str
            The pipeline ID.

        operation_id : str
            The operation ID.

        ### Returns
        ----
        Dict
            A collection of `PipelineOperation` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_operation(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                operation_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/pipelines/{pipeline_id}/operations/{operation_id}',
        )

        return content

    def get_pipeline_stage_artifacts(self, pipeline_id: str, stage_order: int) -> Dict:
        """Returns the supported items from the workspace assigned to the specified
        deployment pipeline stage.

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
            A collection of `PipelineOperation` resources.

        ### Usage
        ----
            >>> pipeline_service = power_bi_client.pipelines()
            >>> pipeline_service.get_pipeline_stage_artifacts(
                pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
                stage_order=1
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/pipelines/{pipeline_id}/stages/{stage_order}/artifacts',
        )

        return content