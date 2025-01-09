"""Module for the `Dataflows` service."""

from typing import Dict
from powerbi.session import PowerBiSession


class Dataflows:
    """Class for the `Dataflows` service."""

    def __init__(self, session: object) -> None:
        """Initializes the `Dataflows` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> groups_service = power_bi_client.dataflow()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = "myorg/groups/{group_id}/dataflows"

    def get_dataflows(self, group_id: str) -> Dict:
        """Returns a list of dataflows in a group.

        ### Returns
        -------
        Dict
            A collection of `Dataflow` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflows(group_id='')
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=self.endpoint.format(group_id=group_id)
        )

        return content

    def update_refresh_schedule(
        self, group_id: str, dataflow_id: str, refresh_schedule: dict
    ) -> None:
        """Creates or updates the refresh schedule for a specified dataflow.

        ### Parameters
        ----
        group_id : str
            The group ID.

        dataflow_id : str
            The dataflow ID.

        refresh_schedule : dict
            The refresh schedule.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflows(
                group_id='',
                dataflow_id='',
                refresh_schedule={}
            )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            json_payload=refresh_schedule,
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/refreshSchedule",
        )

        return content
