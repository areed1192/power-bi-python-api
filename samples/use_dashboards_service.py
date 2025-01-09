"""Demonstrates how to use the `Dashboards` service."""

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

# Initialize the `Dashboards` service.
dashboard_service = power_bi_client.dashboards()

# Add a dashboard to our Workspace.
dashboard_service.add_dashboard(name="tradingRobot")

# Get all the dashboards in our Org.
pprint(dashboard_service.get_dashboards())

# Grab all the dashboards for a specific workspace.
pprint(
    dashboard_service.get_dashboard(dashboard_id="bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8")
)

# Add a dashboard to a specific workspace.
pprint(
    dashboard_service.add_dashboard_in_group(
        name="my_new_dashboard", group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# Grab all the dashboards for a specific workspace.
pprint(
    dashboard_service.get_group_dashboards(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# Grab a specific dashboard from a specific workspace.
pprint(
    dashboard_service.get_group_dashboard(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
    )
)

# Grab all the tiles from a dashboard.
pprint(dashboard_service.get_tiles(dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358"))

# Grab all the tiles from a specific dashboard from a specific workspace.
pprint(
    dashboard_service.get_group_tiles(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
    )
)

# Grab a specific tile from a specific dashboard.
pprint(
    dashboard_service.get_tile(
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
        tile_id="093bfb85-828e-4705-bcf8-0126dd2d5d70",
    )
)

# Grab a specific tile from a specific workspace and a specific workspace..
pprint(
    dashboard_service.get_group_tile(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
        tile_id="093bfb85-828e-4705-bcf8-0126dd2d5d70",
    )
)

# Clone a specific tile.
pprint(
    dashboard_service.clone_tile(
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
        tile_id="093bfb85-828e-4705-bcf8-0126dd2d5d70",
        target_dashboard_id="86cb0a0e-612d-4822-9a29-d83478e21199",
    )
)

# Clone a specific tile from a specific workspace.
pprint(
    dashboard_service.clone_group_tile(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        dashboard_id="1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358",
        tile_id="093bfb85-828e-4705-bcf8-0126dd2d5d70",
        target_dashboard_id="86cb0a0e-612d-4822-9a29-d83478e21199",
    )
)
