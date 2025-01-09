"""Demonstrates how to use the `Capacities` service."""

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

# Initialize the `Capacities` service.
capacities_service = power_bi_client.capactities()

# Get a list of the User's available capacities.
pprint(capacities_service.get_capacities())

# Get a list of the User's available capacities.
pprint(
    capacities_service.get_workloads(capacity_id="890D018E-4B64-4BB1-97E5-BD5490373413")
)

# Grab a specific workload from a capacity.
pprint(
    capacities_service.get_workload(
        capacity_id="890D018E-4B64-4BB1-97E5-BD5490373413", workload_name="my-workload"
    )
)

# Grab a specific workload from a capacity.
pprint(capacities_service.get_refreshables())

# Get refreshables for a specific capacity.
pprint(
    capacities_service.get_refreshables_for_capacity(
        capacity_id="890D018E-4B64-4BB1-97E5-BD5490373413".lower(), top=10
    )
)
