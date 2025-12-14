"""Module for the `Gateways` service."""

from enum import Enum

from powerbi.session import PowerBiSession
from powerbi.utils import CredentialDetails


class Gateways:
    """The `Gateways` service allows you to manage Gateways
    in Microsoft PowerBi."""

    def __init__(self, session: object) -> None:
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

    def add_datasource_user(
        self,
        gateway_id: str,
        datasource_id: str,
        data_source_access_right: str | Enum,
        display_name: str = None,
        email_address: str = None,
        identifier: str = None,
        principal_type: str | Enum = None,
        profile: str | Enum = None,
    ) -> None:
        """Grants or updates the permissions required to use the
        specified data source for the specified user.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        data_source_access_right : str | Enum
            The access right (permission level) that a user has on the data source.

        display_name : str, optional
            The display name of the principal.

        email_address : str, optional
            The email address of the user.

        identifier : str, optional
            The object ID of the principal.

        principal_type : str | Enum, optional
            The principal type.

        profile : str | Enum, optional
            A Power BI service principal profile. Only
            relevant for Power BI Embedded multi-tenancy
            solution.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.add_datasource_user(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012",
                    data_source_access_right="Read",
                )
        """

        if not isinstance(data_source_access_right, str):
            data_source_access_right = data_source_access_right.value

        if not isinstance(principal_type, str):
            principal_type = principal_type.value

        if not isinstance(profile, str):
            profile = profile.value

        # Define the payload.
        payload = {
            "datasourceAccessRight": data_source_access_right,
            "displayName": display_name,
            "emailAddress": email_address,
            "identifier": identifier,
            "principalType": principal_type,
            "profile": profile,
        }

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users"

        # Make the request.
        content = self.power_bi_session.make_request(
            method="post", endpoint=endpoint, json_payload=payload
        )

        return content

    def create_datasource(
        self,
        gateway_id: str,
        connection_details: str,
        credential_details: dict | CredentialDetails,
        data_source_name: str,
        data_source_type: str | Enum,
    ) -> dict:
        """Creates a new data source on the specified on-premises gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        connection_details : str
            The connection details of the data source.

        credential_details : dict | CredentialDetails
            The credential details of the data source.

        data_source_name : str
            The data source name.

        data_source_type : str | Enum
            The data source type.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.create_datasource(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    connection_details="{\"server\":\"MyServer\",\"database\":\"MyDatabase\"}",
                    data_source_name="Sample Datasource",
                    data_source_type="SQL",
                    credential_details={
                        "credentialType": "Windows",
                        "credentials": "AB....EF==",
                        "encryptedConnection": "Encrypted",
                        "encryptionAlgorithm": "RSA-OAEP",
                        "privacyLevel": "None"
                    }
                )
        """

        if not isinstance(data_source_type, str):
            data_source_type = data_source_type.value

        if not isinstance(credential_details, dict):
            credential_details = credential_details.to_dict()

        # Define the payload.
        payload = {
            "dataSourceType": data_source_type,
            "connectionDetails": connection_details,
            "credentialDetails": credential_details,
            "datasourceName": data_source_name,
        }

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources"

        # Make the request.
        content = self.power_bi_session.make_request(
            method="post", endpoint=endpoint, json_payload=payload
        )

        return content

    def delete_datasource(self, gateway_id: str, datasource_id: str) -> None:
        """Deletes a data source from the specified on-premises gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.delete_datasource(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}"

        # Make the request.
        content = self.power_bi_session.make_request(method="delete", endpoint=endpoint)

        return content

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
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        email_address : str
            The email address of the user.

        profile_id : str, optional
            The service principal profile ID to delete.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.delete_datasource_user(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012",
                    email_address="jon.doe@email.com"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users/{email_address}"

        # Define the parameters.
        if profile_id is not None:
            params = {"profileId": profile_id}
        else:
            params = None

        # Make the request.
        content = self.power_bi_session.make_request(
            method="delete", endpoint=endpoint, params=params
        )

        return content

    def get_datasource(self, gateway_id: str, datasource_id: str) -> dict:
        """Returns the specified data source from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def get_datasource_status(self, gateway_id: str, datasource_id: str) -> dict:
        """Checks the connectivity status of the specified data source from
        the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource_status(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/status"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def get_datasource_users(self, gateway_id: str, datasource_id: str) -> dict:
        """Returns a list of users who have access to the specified data source.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasource_users(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}/users"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def get_datasources(self, gateway_id: str) -> dict:
        """Returns a list of data sources from the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_datasources(
                    gateway_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def get_gateways(self) -> dict:
        """Returns a list of gateways for which the user is an admin.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_gateways()
        """

        # Define the endpoint.
        endpoint = "myorg/gateways"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def get_gateway(self, gateway_id: str) -> dict:
        """Returns the specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.get_gateway(
                    gateway_id="12345678-1234-1234-1234-123456789012"
                )
        """

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}"

        # Make the request.
        content = self.power_bi_session.make_request(method="get", endpoint=endpoint)

        return content

    def update_datasource(
        self,
        gateway_id: str,
        datasource_id: str,
        credential_details: dict | CredentialDetails = None,
    ) -> dict:
        """Updates the credentials of the specified data source from the
        specified gateway.

        ### Parameters
        ----
        gateway_id : str
            The gateway ID. When using a gateway cluster, the gateway ID refers to
            the primary (first) gateway in the cluster. In such cases, gateway ID
            is similar to gateway cluster ID.

        datasource_id : str
            The data source ID.

        credential_details : dict | CredentialDetails
            The credential details of the data source.

        ### Usage
        ----
            >>> gateways_service = power_bi_client.gateways()
            >>> gateways_service.update_datasource(
                    gateway_id="12345678-1234-1234-1234-123456789012",
                    datasource_id="12345678-1234-1234-1234-123456789012",
                    credential_details={
                        "credentialType": "Windows",
                        "credentials": "AB....EF==",
                        "encryptedConnection": "Encrypted",
                        "encryptionAlgorithm": "RSA-OAEP",
                        "privacyLevel": "None"
                    }
                )
        """

        if not isinstance(credential_details, dict):
            credential_details = credential_details.to_dict()

        # Define the payload.
        payload = {
            "credentialDetails": credential_details,
        }

        # Define the endpoint.
        endpoint = f"myorg/gateways/{gateway_id}/datasources/{datasource_id}"

        # Make the request.
        content = self.power_bi_session.make_request(
            method="patch", endpoint=endpoint, json_payload=payload
        )

        return content
