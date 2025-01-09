"""Demonstrates how to use the `PowerBiClient` class."""

from configparser import ConfigParser
from powerbi.client import PowerBiClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("config/config.ini")

# Get the specified credentials.
client_id = config.get("power_bi_api", "client_id")
redirect_uri = config.get("power_bi_api", "redirect_uri")
client_secret = config.get("power_bi_api", "client_secret")

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `Dashboards` service.
dashboard_service = power_bi_client.dashboards()
