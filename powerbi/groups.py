from typing import Dict
from powerbi.session import PowerBiSession


class Groups():

    def __init__(self, session: object) -> None:
        """Initializes the `Groups` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = 'myorg/groups'

    def get_groups(self) -> Dict:
        """Returns a list of workspaces the user has access to.

        ### Returns
        -------
        Dict
            A collection of `Group` resources.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.get_groups()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.endpoint
        )

        return content
