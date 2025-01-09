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

# Initialize the `Groups` service.
groups_service = power_bi_client.groups()

# Grab all the Groups.
all_groups = groups_service.get_groups()

# List all the groups.
pprint(
    groups_service.get_groups()
)

# Loop through the Groups.
for group in all_groups['value']:

    group_id = group.get("id", None)
    group_name = group.get("name", None)
    default_data_storage_format = group.get("defaultDatasetStorageFormat", None)

    # Print the Group ID and Name.
    print(f"Group ID: {group_id}")
    print(f"Group Name: {group_name}")
    print("*" * 50)
