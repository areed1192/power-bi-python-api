from typing import List

from powerbi.session import PowerBiSession
from powerbi.auth import PowerBiAuth
from powerbi.dashboards import Dashboards
from powerbi.groups import Groups
from powerbi.users import Users
from powerbi.template_apps import TemplateApps
from powerbi.dataflow_storage_account import DataflowStorageAccount
from powerbi.push_datasets import PushDatasets
from powerbi.imports import Imports
from powerbi.reports import Reports
from powerbi.available_features import AvailableFeatures
from powerbi.capacities import Capacities
from powerbi.pipelines import Pipelines
from powerbi.apps import Apps


class PowerBiClient:

    """
    ### Overview
    ----
    Is the main entry point to the other Power BI
    REST Services.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        scope: List[str],
        account_type: str = "common",
        credentials: str = None,
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
            credentials=self.credentials,
        )

        self.power_bi_auth_client.login()

        self.power_bi_session = PowerBiSession(client=self.power_bi_auth_client)

    def apps(self) -> Apps:
        """Used to access the `Apps` Services and metadata.

        ### Returns
        ---
        Apps :
            The `Apps` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> apps_service = power_bi_client.apps()
        """

        return Apps(session=self.power_bi_session)

    def dashboards(self) -> Dashboards:
        """Used to access the `Dashboards` Services and metadata.

        ### Returns
        ---
        Dashboards :
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

        return Dashboards(session=self.power_bi_session)

    def groups(self) -> Groups:
        """Used to access the `Groups` Services and metadata.

        ### Returns
        ---
        Groups :
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

        return Groups(session=self.power_bi_session)

    def users(self) -> Users:
        """Used to access the `Users` Services and metadata.

        ### Returns
        ---
        Users :
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

        return Users(session=self.power_bi_session)

    def template_apps(self) -> TemplateApps:
        """Used to access the `TemplateApps` Services and metadata.

        ### Returns
        ---
        TemplateApps :
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

        return TemplateApps(session=self.power_bi_session)

    def dataflow_storage_account(self) -> DataflowStorageAccount:
        """Used to access the `DataflowStorageAccount` Services and metadata.

        ### Returns
        ---
        DataflowStorageAccount :
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

        return DataflowStorageAccount(session=self.power_bi_session)

    def push_datasets(self) -> PushDatasets:
        """Used to access the `PushDatasets` Services and metadata.

        ### Returns
        ---
        PushDatasets :
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

        return PushDatasets(session=self.power_bi_session)

    def imports(self) -> Imports:
        """Used to access the `Imports` Services and metadata.

        ### Returns
        ---
        Imports:
            The `Imports` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> imports_service = power_bi_client.imports()
        """

        return Imports(session=self.power_bi_session)

    def reports(self) -> Reports:
        """Used to access the `Reports` Services and metadata.

        ### Returns
        ---
        Reports:
            The `Reports` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> reports_service = power_bi_client.reports()
        """

        return Reports(session=self.power_bi_session)

    def available_features(self) -> AvailableFeatures:
        """Used to access the `AvailableFeatures` Services and metadata.

        ### Returns
        ---
        AvailableFeatures:
            The `AvailableFeatures` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> available_features_service = power_bi_client.available_features()
        """

        return AvailableFeatures(session=self.power_bi_session)

    def capactities(self) -> Capacities:
        """Used to access the `Capacities` Services and metadata.

        ### Returns
        ---
        Capacities:
            The `Capacities` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> capacities_service = power_bi_client.capactities()
        """

        return Capacities(session=self.power_bi_session)

    def pipelines(self) -> Pipelines:
        """Used to access the `Pipelines` Services and metadata.

        ### Returns
        ---
        Pipelines:
            The `Pipelines` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(
                client_id=client_id,
                client_secret=client_secret,
                scope=['https://analysis.windows.net/powerbi/api/.default'],
                redirect_uri=redirect_uri,
                credentials='config/power_bi_state.jsonc'
            )
            >>> pipelines_service = power_bi_client.pipelines()
        """

        return Pipelines(session=self.power_bi_session)
