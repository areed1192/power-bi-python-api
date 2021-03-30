from typing import Dict
from powerbi.session import PowerBiSession


class Users():

    def __init__(self, session: object) -> None:
        """Initializes the `Users` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> users_service = power_bi_client.users()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = 'myorg/RefreshUserPermissions'

    def refresh_user_permissions(self) -> None:
        """Refreshes user permissions in Power BI.

        ### Overview
        ----
        When a user is granted permissions to a workspace, app, or
        artifact, it might not be immediately available through API
        calls. This operation refreshes user permissions and makes
        sure the user permissions are fully updated. Make the refresh
        user permissions call, before any other API calls. It takes
        about two minutes for the permissions to get refreshed. 
        Before calling other APIs, wait for two minutes.

        ### Usage
        ----
            >>> users_service = power_bi_client.users()
            >>> users_service.refresh_user_permissions()
        """

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=self.endpoint
        )

        return content
