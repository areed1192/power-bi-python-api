"""Used to demonstrate the usage of the `Datasets` service."""

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
group_id = config.get("power_bi_api", "group_id")

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)


# Initialize the `Datasets` service.
datasets_service = power_bi_client.datasets()

# Get all datasets from "My Workspace".
pprint(datasets_service.get_datasets())

# Get all datasets from a specific workspace.
pprint(datasets_service.get_datasets(group_id=group_id))

# Get a specific dataset by ID.
pprint(datasets_service.get_dataset(dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"))

# Get the data sources for a dataset.
pprint(
    datasets_service.get_datasources(dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f")
)

# Get the users who have access to a dataset.
pprint(
    datasets_service.get_dataset_users(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
    )
)

# Get upstream dataflow links for datasets in a workspace.
pprint(
    datasets_service.get_dataset_to_dataflows_links_in_group(
        group_id=group_id
    )
)

# Get gateway data sources for a dataset.
pprint(
    datasets_service.get_gateway_datasources(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
    )
)

# Get parameters for a dataset.
pprint(datasets_service.get_parameters(dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"))

# Get the refresh history for a dataset (last 5 entries).
pprint(
    datasets_service.get_refresh_history(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f", top=5
    )
)

# Get execution details for a specific refresh operation.
pprint(
    datasets_service.get_refresh_execution_details(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f",
        refresh_id="9113c335-decf-4d0d-afac-4d2bc8898a65",
    )
)

# Get the refresh schedule for a dataset.
pprint(
    datasets_service.get_refresh_schedule(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
    )
)

# # Get the DirectQuery/LiveConnection refresh schedule for a dataset.
# pprint(
#     datasets_service.get_direct_query_refresh_schedule(
#         dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
#     )
# )

# Get the query scale-out sync status for a dataset.
pprint(
    datasets_service.get_query_scale_out_sync_status(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
    )
)

# Discover gateways a dataset can be bound to.
pprint(
    datasets_service.discover_gateways(
        dataset_id="93bbf792-4aca-47eb-bb16-37d9cfcd708f"
    )
)
