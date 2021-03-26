from typing import Dict
from powerbi.session import PowerBiSession


class Dashboards():

    def __init__(self, session: object) -> None:
        """Initializes the `Dashboards` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = 'myorg/dashboards'
        self.group_endpoint = 'myorg/groups/{group_id}/dashboards'

    def add_dashboard(self, name: str) -> Dict:
        """Creates a new empty dashboard on `My Workspace`.

        ### Parameters
        ----
        name : str
            The name of the new dashboard.

        ### Returns
        ----
        Dict
            A `Dashboard` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.add_dashboard(name='my_new_dashboard')
        """

        # Define the payload.
        payload = {
            'name': name
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method='post',
            endpoint=self.endpoint,
            json_payload=payload
        )

        return content

    def get_dashboards(self) -> Dict:
        """Returns a list of dashboards from `My Workspace`.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_dashboards()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.endpoint
        )

        return content

    def get_group_dashboards(self, group_id: str) -> Dict:
        """Returns a list of dashboards from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_group_dashboards(group_id='')
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.group_endpoint.format(group_id=group_id)
        )

        return content
