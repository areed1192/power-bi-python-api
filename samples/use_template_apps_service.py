"""Demonstrates how to use the `TemplateApps` service."""

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

# Initialize the `TemplateApps` service.
template_apps_service = power_bi_client.template_apps()

# Create an Install Ticket.
pprint(
    template_apps_service.create_install_ticket(
        app_id="91ce06d1-d81b-4ea0-bc6d-2ce3dd2f8e87",
        owner_tenant_id="d43e3248-3d83-44aa-a94d-c836bd7f9b79",
        package_key="g632bb64...OfsoqT56xEM=",
        config={"configuration": {"param1": "value1", "param2": "value2"}},
    )
)
