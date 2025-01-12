"""Module for the Power BI `Datasets` service."""

from typing import Dict
from powerbi.session import PowerBiSession


class Datasets:
    """Class for the `Datasets` service."""

    def __init__(self, session: object) -> None:
        """Initializes the `Datasets` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = "myorg/groups/{group_id}/datasets"

    def get_datasets_in_group(self, group_id: str) -> Dict:
        """Returns a list of datasets in a group.

        ### Returns
        -------
        Dict
            A collection of `Dataset` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_datasets_in_group(group_id='')
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/groups/{group_id}/datasets"
        )

        return content

    def update_refresh_schedule_in_group(
        self, group_id: str, dataset_id: str, refresh_schedule: dict
    ) -> None:
        """Creates or updates the refresh schedule for a specified dataset.

        ### Parameters
        ----
        group_id : str
            The group ID.

        dataset_id : str
            The dataset ID.

        refresh_schedule : dict
            The refresh schedule.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.get_dataflows(
                group_id='',
                dataset_id='',
                refresh_schedule={}
            )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            json_payload=refresh_schedule,
            endpoint=f"myorg/groups/{group_id}/datasets/{
                dataset_id}/refreshSchedule",
        )

        return content

    def bind_to_gateway(
        self,
        dataset_id: str,
        gateway_object_id: str,
        datasource_object_ids: list = None,
    ) -> None:
        """Binds a dataset to a specified gateway.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset to bind.

        gateway_object_id : str
            The ID of the gateway to bind the dataset to. When using a gateway cluster,
            this refers to the primary gateway.

        datasource_object_ids : list, (optional, default=None)
            A list of unique identifiers for the data sources in the gateway.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.bind_to_gateway(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934',
                    datasource_object_ids=[
                        'dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb',
                        '3bfe5d33-ab7d-4d24-b0b5-e2bb8eb01cf5'
                    ]
                )
        """

        # Prepare the payload.
        payload = {"gatewayObjectId": gateway_object_id}

        # Add datasource IDs if provided.
        if datasource_object_ids:
            payload["datasourceObjectIds"] = datasource_object_ids

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="post",
            json_payload=payload,
            endpoint=f"myorg/datasets/{dataset_id}/Default.BindToGateway",
        )

        return response

    def bind_to_gateway_in_group(
        self,
        group_id: str,
        dataset_id: str,
        gateway_object_id: str,
        datasource_object_ids: list = None,
    ) -> None:
        """Binds a dataset in a specified workspace to a specified gateway.

        ### Parameters
        ----
        group_id : str
            The ID of the workspace containing the dataset.

        dataset_id : str
            The ID of the dataset to bind.

        gateway_object_id : str
            The ID of the gateway to bind the dataset to. When using a gateway cluster,
            this refers to the primary gateway.

        datasource_object_ids : list, optional
            A list of unique identifiers for the data sources in the gateway.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.bind_to_gateway_in_group(
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48',
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934',
                    datasource_object_ids=[
                        'dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb',
                        '3bfe5d33-ab7d-4d24-b0b5-e2bb8eb01cf5'
                    ]
                )
        """

        # Prepare the payload.
        payload = {"gatewayObjectId": gateway_object_id}

        # Add datasource IDs if provided.
        if datasource_object_ids:
            payload["datasourceObjectIds"] = datasource_object_ids

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="post",
            json_payload=payload,
            endpoint=f"myorg/groups/{group_id}/datasets/{
                dataset_id}/Default.BindToGateway",
        )

        return response

    def cancel_refresh(self, dataset_id: str, refresh_id: str) -> None:
        """Cancels the specified refresh operation for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset.

        refresh_id : str
            The ID of the refresh operation to cancel.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.cancel_refresh(
                    dataset_id='f7fc6510-e151-42a3-850b-d0805a391db0',
                    refresh_id='87f31ef7-1e3a-4006-9b0b-191693e79e9e'
                )
        """

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/datasets/{dataset_id}/refreshes/{refresh_id}",
        )

        return response

    def cancel_refresh_in_group(
        self, group_id: str, dataset_id: str, refresh_id: str
    ) -> None:
        """Cancels the specified refresh operation for the specified dataset in a workspace.

        ### Parameters
        ----
        group_id : str
            The ID of the workspace containing the dataset.

        dataset_id : str
            The ID of the dataset.

        refresh_id : str
            The ID of the refresh operation to cancel.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.cancel_refresh_in_group(
                    group_id='fdb91b8f-0a9b-44c1-b6c0-0cb185c6ebfb',
                    dataset_id='f7fc6510-e151-42a3-850b-d0805a391db0',
                    refresh_id='87f31ef7-1e3a-4006-9b0b-191693e79e9e'
                )
        """

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/groups/{group_id}/datasets/{dataset_id}/refreshes/{refresh_id}",
        )

        return response

    def delete_dataset(self, dataset_id: str) -> None:
        """Deletes the specified dataset from My workspace.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset to delete.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.delete_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="delete", endpoint=f"myorg/datasets/{dataset_id}"
        )

        return response

    def delete_dataset_in_group(self, group_id: str, dataset_id: str) -> None:
        """Deletes the specified dataset from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The ID of the workspace containing the dataset.

        dataset_id : str
            The ID of the dataset to delete.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.delete_dataset_in_group(
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48',
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        # Make the API call.
        response = self.power_bi_session.make_request(
            method="delete", endpoint=f"myorg/groups/{group_id}/datasets/{dataset_id}"
        )

        return response
