from typing import Dict
from powerbi.session import PowerBiSession


class DataflowStorageAccount():

    def __init__(self, session: object) -> None:
        """Initializes the `DataflowStorageAccount` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> dataflow_storage_service = power_bi_client.dataflow_storage_account()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = 'myorg/dataflowStorageAccounts'

    def get_dataflow_storage_accounts(self) -> Dict:
        """Returns a list of dataflow storage accounts the user
        has access to.

        ### Returns
        ----
        Dict
            A collection of `DataflowStorageAccount` resources.

        ### Usage
        ----
            >>> dataflow_storage_service = power_bi_client.dataflow_storage_account()
            >>> dataflow_storage_service.get_dataflow_storage_accounts()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint='myorg/dataflowStorageAccounts'
        )

        return content

    def assign_to_dataflow_storage_account(self, group_id: str, dataflow_storage_id: str) -> Dict:
        """Assigns the specified workspace to the specified dataflow storage
        account.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dataflow_storage_id : str
            The Power BI dataflow storage account id. To unassign the specified workspace
            from a Power BI dataflow storage account, an empty GUID (00000000-0000-0000-0000-000000000000)
            should be provided as dataflowStorageId.

        ### Returns
        ----
        Dict
            A collection of `DataflowStorageAccount` resources.

        ### Usage
        ----
            >>> dataflow_storage_service = power_bi_client.dataflow_storage_account()
            >>> dataflow_storage_service.assign_to_dataflow_storage_account(
                group_id='',
                dataflow_storage_id=''
            )
        """

        payload = {
            'dataflowStorageId': dataflow_storage_id
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/AssignToDataflowStorage',
            json_payload=payload
        )

        return content
