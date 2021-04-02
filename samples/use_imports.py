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

# Initialize the `Imports` service.
imports_service = power_bi_client.imports()

# # Create a temporary upload location.
# pprint(
#     imports_service.create_temporary_upload_location()
# )


# Get all the Imports from my workspace.
pprint(
    imports_service.get_imports()
)

# Query a specific Import from my workspace.
pprint(
    imports_service.get_import(
        import_id='e40f7c73-84d1-4cf5-a696-5850a5ec8ad3'
    )
)
