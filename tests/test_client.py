import unittest

from unittest import TestCase
from configparser import ConfigParser

from powerbi.client import PowerBiClient
from powerbi.auth import PowerBiAuth
from powerbi.session import PowerBiSession
from powerbi.dashboards import Dashboards
from powerbi.groups import Groups


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

    def tearDown(self) -> None:
        """Teardown the `PowerBiClient` object."""

        del self.power_bi_client


if __name__ == '__main__':
    unittest.main()
