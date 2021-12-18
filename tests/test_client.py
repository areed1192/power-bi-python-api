import unittest

from unittest import TestCase
from configparser import ConfigParser

from powerbi.client import PowerBiClient
from powerbi.auth import PowerBiAuth
from powerbi.session import PowerBiSession
from powerbi.dashboards import Dashboards
from powerbi.groups import Groups
from powerbi.template_apps import TemplateApps
from powerbi.users import Users
from powerbi.dataflow_storage_account import DataflowStorageAccount
from powerbi.push_datasets import PushDatasets
from powerbi.available_features import AvailableFeatures
from powerbi.capacities import Capacities
from powerbi.reports import Reports
from powerbi.apps import Apps


class TestPowerBiSession(TestCase):

    """Will perform a unit test for the `PowerBiClient` object."""

    def setUp(self) -> None:
        """Set up the `PowerBiClient` object."""

        # Initialize the Parser.
        config = ConfigParser()

        # Read the file.
        config.read('config/config.ini')

        # Get the specified credentials.
        client_id = config.get('power_bi_api', 'client_id')
        redirect_uri = config.get('power_bi_api', 'redirect_uri')
        client_secret = config.get('power_bi_api', 'client_secret')

        # Initialize the Client.
        self.power_bi_client = PowerBiClient(
            client_id=client_id,
            client_secret=client_secret,
            scope=['https://analysis.windows.net/powerbi/api/.default'],
            redirect_uri=redirect_uri,
            credentials='config/power_bi_state.jsonc'
        )

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `PowerBiClient` object"""

        self.assertIsInstance(self.power_bi_client, PowerBiClient)

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `PowerBiSession` object"""

        self.assertIsInstance(
            self.power_bi_client.power_bi_session,
            PowerBiSession
        )

    def test_creates_instance_of_auth(self):
        """Create an instance and make sure it's a `PowerBiAuth` object"""

        self.assertIsInstance(
            self.power_bi_client.power_bi_auth_client,
            PowerBiAuth
        )

    def test_creates_instance_of_apps(self):
        """Create an instance and make sure it's a `Apps` object"""

        self.assertIsInstance(
            self.power_bi_client.apps(),
            Apps
        )

    def test_creates_instance_of_dashboards(self):
        """Create an instance and make sure it's a `Dashboards` object"""

        self.assertIsInstance(
            self.power_bi_client.dashboards(),
            Dashboards
        )

    def test_creates_instance_of_groups(self):
        """Create an instance and make sure it's a `Groups` object"""

        self.assertIsInstance(
            self.power_bi_client.groups(),
            Groups
        )

    def test_creates_instance_of_users(self):
        """Create an instance and make sure it's a `Users` object"""

        self.assertIsInstance(
            self.power_bi_client.users(),
            Users
        )

    def test_creates_instance_of_template_apps(self):
        """Create an instance and make sure it's a `TemplateApps` object"""

        self.assertIsInstance(
            self.power_bi_client.template_apps(),
            TemplateApps
        )

    def test_creates_instance_of_dataflow_storage_account(self):
        """Create an instance and make sure it's a `DataflowStorageAccount` object"""

        self.assertIsInstance(
            self.power_bi_client.dataflow_storage_account(),
            DataflowStorageAccount
        )

    def test_creates_instance_of_push_datasets(self):
        """Create an instance and make sure it's a `PushDatasets` object"""

        self.assertIsInstance(
            self.power_bi_client.push_datasets(),
            PushDatasets
        )

    def test_creates_instance_of_available_features(self):
        """Create an instance and make sure it's a `AvailableFeatures` object"""

        self.assertIsInstance(
            self.power_bi_client.available_features(),
            AvailableFeatures
        )

    def test_creates_instance_of_capacities(self):
        """Create an instance and make sure it's a `Capacities` object"""

        self.assertIsInstance(
            self.power_bi_client.capactities(),
            Capacities
        )

    def test_creates_instance_of_reports(self):
        """Create an instance and make sure it's a `Capacities` object"""

        self.assertIsInstance(
            self.power_bi_client.reports(),
            Reports
        )

    def tearDown(self) -> None:
        """Teardown the `PowerBiClient` object."""

        del self.power_bi_client


if __name__ == '__main__':
    unittest.main()
