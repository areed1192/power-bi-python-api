"""Demonstrates how to use the `Gateways` service."""

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
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `Gateways` service.
gateways_service = power_bi_client.gateways()

# Get all Gateways the user is an admin for.
pprint(gateways_service.get_gateways())

# Get a specific Gateway by ID.
GATEWAY_ID = "12345678-1234-1234-1234-123456789012"
pprint(gateways_service.get_gateway(gateway_id=GATEWAY_ID))

# Get all Data Sources from a Gateway.
pprint(gateways_service.get_datasources(gateway_id=GATEWAY_ID))

# Get a specific Data Source from a Gateway.
DATASOURCE_ID = "12345678-1234-1234-1234-123456789012"
pprint(
    gateways_service.get_datasource(
        gateway_id=GATEWAY_ID,
        datasource_id=DATASOURCE_ID,
    )
)

# Check the connectivity status of a Data Source.
pprint(
    gateways_service.get_datasource_status(
        gateway_id=GATEWAY_ID,
        datasource_id=DATASOURCE_ID,
    )
)

# Get the users who have access to a Data Source.
pprint(
    gateways_service.get_datasource_users(
        gateway_id=GATEWAY_ID,
        datasource_id=DATASOURCE_ID,
    )
)
