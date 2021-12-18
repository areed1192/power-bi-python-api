from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
client_id = config.get('power_bi_api', 'client_id')
redirect_uri = config.get('power_bi_api', 'redirect_uri')
client_secret = config.get('power_bi_api', 'client_secret')

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Grab my dashboard service.
dashboard_service = power_bi_client.dashboards()

pprint(
    dashboard_service.get_dashboards()
)

pprint(
    dashboard_service.add_dashboard_in_group(
        name='my-new-dashboard-for-video',
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
    )
)

pprint(
    dashboard_service.get_tiles(
        dashboard_id='c2af8b76-c2f7-478a-b905-38905763b4a6'
    )
)

pprint(
    dashboard_service.clone_tile(
        dashboard_id='c2af8b76-c2f7-478a-b905-38905763b4a6',
        tile_id='fb69f2e1-f0dd-459a-9148-befa6bb8386e',
        target_dashboard_id='4837cfe3-741d-43fa-8a2f-423fc08f6f3f'
    )
)
