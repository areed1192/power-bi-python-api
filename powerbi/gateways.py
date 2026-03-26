"""Module for the `Gateways` service."""

from enum import Enum
from typing import Dict, Union

from powerbi.session import PowerBiSession
from powerbi.utils import CredentialDetails


class Gateways:
    """The `Gateways` service allows you to manage Gateways
    in Microsoft PowerBi."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Gateways` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    # ------------------------------------------------------------------
    # GET operations
    # ------------------------------------------------------------------

    def get_gateways(self) -> Dict:
        """Returns a list of gateways for which the user is an admin.

        ### Returns
        ----
        Dict
            A collection of gateway resources.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_gateways()
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/gateways",
        )

        return content

    def get_gateway(self, gateway_id: str) -> Dict:
        """Returns the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        ### Returns
        ----
        Dict
            A gateway resource.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_gateway(
                gateway_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/gateways/{gateway_id}",
        )

        return content

    def get_datasources(self, gateway_id: str) -> Dict:
        """Returns a list of data sources from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        ### Returns
        ----
        Dict
            A collection of datasource resources.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasources(
                gateway_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/gateways/{gateway_id}/datasources",
        )

        return content

    def get_datasource(self, gateway_id: str, datasource_id: str) -> Dict:
        """Returns the specified data source from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        ### Returns
        ----
        Dict
            A datasource resource.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}",
        )

        return content

    def get_datasource_status(self, gateway_id: str, datasource_id: str) -> Dict:
        """Checks the connectivity status of the specified data source
        from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        ### Returns
        ----
        Dict
            The connectivity status.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource_status(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/status",
        )

        return content

    def get_datasource_users(self, gateway_id: str, datasource_id: str) -> Dict:
        """Returns a list of users who have access to the specified
        data source.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        ### Returns
        ----
        Dict
            A collection of datasource user resources.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource_users(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users",
        )

        return content

    # ------------------------------------------------------------------
    # POST operations
    # ------------------------------------------------------------------

    def create_datasource(
        self,
        gateway_id: str,
        connection_details: str,
        credential_details: Union[dict, CredentialDetails],
        data_source_name: str,
        data_source_type: Union[str, Enum],
    ) -> Dict:
        """Creates a new data source on the specified on-premises gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        connection_details : str
            The connection details of the data source.

        credential_details : dict | CredentialDetails
            The credential details of the data source.

        data_source_name : str
            The data source name.

        data_source_type : str | Enum
            The data source type.

        ### Returns
        ----
        Dict
            The created datasource resource.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.create_datasource(
                gateway_id='12345678-1234-1234-1234-123456789012',
                connection_details='{"server":"MyServer","database":"MyDB"}',
                data_source_name='Sample Datasource',
                data_source_type='SQL',
                credential_details={
                    'credentialType': 'Windows',
                    'credentials': 'AB....EF==',
                    'encryptedConnection': 'Encrypted',
                    'encryptionAlgorithm': 'RSA-OAEP',
                    'privacyLevel': 'None'
                }
            )
        """

        if isinstance(data_source_type, Enum):
            data_source_type = data_source_type.value

        if isinstance(credential_details, CredentialDetails):
            credential_details = credential_details.to_dict()

        payload = {
            "dataSourceType": data_source_type,
            "connectionDetails": connection_details,
            "credentialDetails": credential_details,
            "datasourceName": data_source_name,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/gateways/{gateway_id}/datasources",
            json_payload=payload,
        )

        return content

    def add_datasource_user(
        self,
        gateway_id: str,
        datasource_id: str,
        data_source_access_right: Union[str, Enum],
        display_name: str = None,
        email_address: str = None,
        identifier: str = None,
        principal_type: Union[str, Enum] = None,
        profile: Union[str, Enum] = None,
    ) -> None:
        """Grants or updates the permissions required to use the
        specified data source for the specified user.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        data_source_access_right : str | Enum
            The access right (permission level) that a user has on
            the data source.

        display_name : str (optional)
            The display name of the principal.

        email_address : str (optional)
            The email address of the user.

        identifier : str (optional)
            The object ID of the principal.

        principal_type : str | Enum (optional)
            The principal type.

        profile : str | Enum (optional)
            A Power BI service principal profile. Only relevant for
            Power BI Embedded multi-tenancy solution.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.add_datasource_user(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012',
                data_source_access_right='Read',
                email_address='john@contoso.com',
                principal_type='User'
            )
        """

        if isinstance(data_source_access_right, Enum):
            data_source_access_right = data_source_access_right.value

        payload: Dict = {
            "datasourceAccessRight": data_source_access_right,
        }
        if display_name is not None:
            payload["displayName"] = display_name
        if email_address is not None:
            payload["emailAddress"] = email_address
        if identifier is not None:
            payload["identifier"] = identifier
        if principal_type is not None:
            if isinstance(principal_type, Enum):
                principal_type = principal_type.value
            payload["principalType"] = principal_type
        if profile is not None:
            if isinstance(profile, Enum):
                profile = profile.value
            payload["profile"] = profile

        self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users",
            json_payload=payload,
        )

    # ------------------------------------------------------------------
    # PATCH operations
    # ------------------------------------------------------------------

    def update_datasource(
        self,
        gateway_id: str,
        datasource_id: str,
        credential_details: Union[dict, CredentialDetails],
    ) -> None:
        """Updates the credentials of the specified data source from
        the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        credential_details : dict | CredentialDetails
            The credential details of the data source.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.update_datasource(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012',
                credential_details={
                    'credentialType': 'Windows',
                    'credentials': 'AB....EF==',
                    'encryptedConnection': 'Encrypted',
                    'encryptionAlgorithm': 'RSA-OAEP',
                    'privacyLevel': 'None'
                }
            )
        """

        if isinstance(credential_details, CredentialDetails):
            credential_details = credential_details.to_dict()

        payload = {"credentialDetails": credential_details}

        self.power_bi_session.make_request(
            method="patch",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}",
            json_payload=payload,
        )

    # ------------------------------------------------------------------
    # DELETE operations
    # ------------------------------------------------------------------

    def delete_datasource(self, gateway_id: str, datasource_id: str) -> None:
        """Deletes the specified data source from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.delete_datasource(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012'
            )
        """

        self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}",
        )

    def delete_datasource_user(
        self,
        gateway_id: str,
        datasource_id: str,
        email_address: str,
        profile_id: str = None,
    ) -> None:
        """Removes the specified user from the specified data source.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway
            ID refers to the primary (first) gateway in the cluster.

        datasource_id : str
            The data source ID.

        email_address : str
            The email address of the user.

        profile_id : str (optional)
            The service principal profile ID to delete.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.delete_datasource_user(
                gateway_id='12345678-1234-1234-1234-123456789012',
                datasource_id='12345678-1234-1234-1234-123456789012',
                email_address='john@contoso.com'
            )
        """

        params = None
        if profile_id is not None:
            params = {"profileId": profile_id}

        self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users/{email_address}",
            params=params,
        )
