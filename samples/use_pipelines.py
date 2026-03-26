"""Demonstrates how to use the `Pipelines` service."""

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

# Initialize the `Pipelines` service.
pipeline_service = power_bi_client.pipelines()

# Get all the Pipelines a User has access to.
pprint(pipeline_service.get_pipelines())

# Grab a specific pipeline (with stages expanded).
pprint(
    pipeline_service.get_pipeline(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445", expand_stages=True
    )
)

# Grab a specific pipeline (without stages expanded).
pprint(
    pipeline_service.get_pipeline(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445", expand_stages=False
    )
)

# Get the stages of a deployment pipeline.
pprint(
    pipeline_service.get_pipeline_stages(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445"
    )
)

# Grab a specific pipeline's operations (up to 20 most recent).
pprint(
    pipeline_service.get_pipeline_operations(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445"
    )
)

# Get the details of a specific deploy operation.
pprint(
    pipeline_service.get_pipeline_operation(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445",
        operation_id="89ed21f0-6034-467b-a1dc-b59411af2cc5",
    )
)

# Get the Stage Artifacts for the Development stage (0).
pprint(
    pipeline_service.get_pipeline_stage_artifacts(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445", stage_order=0
    )
)

# Get the users of a deployment pipeline.
pprint(
    pipeline_service.get_pipeline_users(
        pipeline_id="a1a5f0aa-5b6c-472f-ba3d-41c22fd01445"
    )
)
