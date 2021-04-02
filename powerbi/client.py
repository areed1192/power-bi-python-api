
from typing import List

from powerbi.session import PowerBiSession
from powerbi.auth import PowerBiAuth
from powerbi.dashboards import Dashboards
from powerbi.groups import Groups
from powerbi.users import Users
from powerbi.template_apps import TemplateApps
from powerbi.dataflow_storage_account import DataflowStorageAccount
from powerbi.push_datasets import PushDatasets


class PowerBiClient():

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        scope: List[str],
        account_type: str = 'common',
        credentials: str = None
    ):
        """Initializes the Graph Client.

        ### Parameters
        ----
        client_id : str
            The application Client ID assigned when
            creating a new Microsoft App.

        client_secret : str
            The application Client Secret assigned when
            creating a new Microsoft App.

        redirect_uri : str
            The application Redirect URI assigned when
            creating a new Microsoft App.

        scope : List[str]
            The list of scopes you want the application
            to have access to.

        account_type : str (optional, Default='common')
            The account type you're application wants to
            authenticate as.

        credentials : str (optional, Default=None)
            The file path to your local credential file.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
        """

        self.credentials = credentials
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_type = account_type
        self.redirect_uri = redirect_uri
        self.scope = scope

        self.power_bi_auth_client = PowerBiAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
            account_type=self.account_type,
            credentials=self.credentials
        )

        self.power_bi_auth_client.login()

        self.power_bi_session = PowerBiSession(
            client=self.power_bi_auth_client
        )

    def dashboards(self) -> Dashboards:
        """Used to access the `Dashboards` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `Dashboards` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> dashboard_service = power_bi_client.dashboards()
        """

        # Grab the Dashboards Object for the session.
        object = Dashboards(session=self.power_bi_session)

        return object

    def groups(self) -> Groups:
        """Used to access the `Groups` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `Groups` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> groups_service = power_bi_client.groups()
        """

        # Grab the Groups Object for the session.
        object = Groups(session=self.power_bi_session)

        return object

    def users(self) -> Users:
        """Used to access the `Users` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `Users` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> users_service = power_bi_client.users()
        """

        # Grab the Users Object for the session.
        object = Users(session=self.power_bi_session)

        return object

    def template_apps(self) -> TemplateApps:
        """Used to access the `TemplateApps` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `TemplateApps` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> template_apps_service = power_bi_client.template_apps()
        """

        # Grab the TemplateApps Object for the session.
        object = TemplateApps(session=self.power_bi_session)

        return object

    def dataflow_storage_account(self) -> DataflowStorageAccount:
        """Used to access the `DataflowStorageAccount` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `DataflowStorageAccount` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> dataflow_storage_service = power_bi_client.dataflow_storage_accounts()
        """

        # Grab the DataflowStorageAccount Object for the session.
        object = DataflowStorageAccount(session=self.power_bi_session)

        return object

    def push_datasets(self) -> PushDatasets:
        """Used to access the `PushDatasets` Services and metadata.

        ### Returns
        ---
        Dashboards:
            The `PushDatasets` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> push_datasets_service = power_bi_client.push_datasets()
        """

        # Grab the PushDatasets Object for the session.
        object = PushDatasets(session=self.power_bi_session)

        return object
