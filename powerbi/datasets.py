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
            endpoint=f"myorg/groups/{group_id}/datasets/{dataset_id}/refreshSchedule",
        )

        return content
