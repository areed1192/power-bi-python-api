"""Demonstrates how to use the `Admin` service."""

from pprint import pprint
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
    scope=[
        "https://analysis.windows.net/powerbi/api/.default"
    ],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `Admin` service.
admin_service = power_bi_client.admin()

# Get a list of refreshables for the organization (top 20).
pprint(admin_service.get_refreshables(top=20))

# Get refreshables with expanded capacity and group info.
pprint(
    admin_service.get_refreshables(
        top=50,
        expand="capacity,group",
    )
)

# Get refreshables filtered by average duration greater than 30 minutes (1800 seconds).
pprint(
    admin_service.get_refreshables(
        top=100,
        filter_by="averageDuration gt 1800",
    )
)

# Get refreshables with pagination (skip the first 100 results).
pprint(
    admin_service.get_refreshables(
        top=100,
        skip=100,
    )
)
