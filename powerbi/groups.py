from enum import Enum
from typing import Union
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

    def get_group_users(self, group_id: str) -> Dict:
        """Returns a list of users that have access to the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        ### Returns
        ----
        Dict
            A collection of `GroupUsers` resources.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.get_group_users(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/users'
        )

        return content

    def create_group(self, name: str, workspace_v2: bool = None) -> Dict:
        """Creates new workspace.

        ### Parameters
        ----
        name : str
            The name of the workspace.

        workspace_v2 : bool (optional, Default=None)
            Preview feature: Create a workspace V2. The only
            supported value is true.

        ### Returns
        ----
        Dict
            A `Group` resource.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.create_group(
                name='my-new-workspace',
                workspace_v2=True
            )
        """

        params = {
            'name': name
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups?workspaceV2={workspace_v2}',
            json_payload=params
        )

        return content

    def delete_group(self, group_id: str) -> None:
        """Deletes the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.delete_group(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/groups/{group_id}'
        )

        return content

    def add_group_user(
        self,
        group_id: str,
        group_user_access_rights: Union[str, Enum],
        display_name: str = None,
        email_address: str = None,
        identifier: str = None,
        principal_type: Union[str, Enum] = None
    ) -> None:
        """Grants the specified user permissions to the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        group_user_access_rights : Union[str, Enum]
            Access rights user has for the workspace.

        display_name : str (optional, Default=None)
            Display name of the principal.

        email_address : str (optional, Default=None)
            Email address of the user.  

        identifier : str (optional, Default=None)
            Object ID of the principal

        principal_type : str (optional, Default=None)
            The principal type.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.add_group_user(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                group_user_access_right='Admin',
                email_address='john@contoso.com'
            )
        """

        if isinstance(group_user_access_rights, Enum):
            group_user_access_rights = group_user_access_rights.value

        if isinstance(principal_type, Enum):
            principal_type = principal_type.value

        params = {}
        params['groupUserAccessRight'] = group_user_access_rights
        params['displayName'] = display_name
        params['emailAddress'] = email_address
        params['identifier'] = identifier
        params['principalType'] = principal_type

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/users',
            json_payload=params
        )

        return content

    def delete_group_user(
        self,
        group_id: str,
        email_address: str
    ) -> None:
        """Deletes the specified user permissions from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        email_address : str
            Email address of the user.  

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.delete_group_user(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                email_address='john@contoso.com'
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/groups/{group_id}/users/{email_address}'
        )

        return content

    def update_group_user(
        self,
        group_id: str,
        group_user_access_rights: Union[str, Enum],
        display_name: str = None,
        email_address: str = None,
        identifier: str = None,
        principal_type: Union[str, Enum] = None
    ) -> None:
        """Update the specified user permissions to the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        group_user_access_rights : Union[str, Enum]
            Access rights user has for the workspace.

        display_name : str (optional, Default=None)
            Display name of the principal.

        email_address : str (optional, Default=None)
            Email address of the user.  

        identifier : str (optional, Default=None)
            Object ID of the principal

        principal_type : str (optional, Default=None)
            The principal type.

        ### Usage
        ----
            >>> groups_service = power_bi_client.groups()
            >>> groups_service.update_group_user(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                group_user_access_right='Admin',
                email_address='john@contoso.com'
            )
        """

        if isinstance(group_user_access_rights, Enum):
            group_user_access_rights = group_user_access_rights.value

        if isinstance(principal_type, Enum):
            principal_type = principal_type.value

        params = {}
        params['groupUserAccessRight'] = group_user_access_rights
        params['displayName'] = display_name
        params['emailAddress'] = email_address
        params['identifier'] = identifier
        params['principalType'] = principal_type

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/users',
            json_payload=params
        )

        return content
