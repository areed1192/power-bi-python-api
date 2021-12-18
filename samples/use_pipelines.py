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
    # You need to make sure you request this permission, but you can't have it
    # with the `.default` scope.
    scope=[
        'https://analysis.windows.net/powerbi/api/Pipeline.ReadWrite.All'
    ],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Initialize the `Pipelines` service.
pipeline_service = power_bi_client.pipelines()

# Get all the Pipelines a User has access to.
pprint(
    pipeline_service.get_pipelines()
)

# Grab a specific pipeline.
pprint(
    pipeline_service.get_pipeline(
        pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
        expand_stages=True
    )
)

# Grab a specific pipeline's operations.
pprint(
    pipeline_service.get_pipeline_operations(
        pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357'
    )
)

# Get the Stage Artifacts for the Development Pipeline (1)
pprint(
    pipeline_service.get_pipeline_stage_artifacts(
        pipeline_id='a6ffe4a2-0b24-4b87-a83c-dc8e7f7a3357',
        stage_order=0
    )
)
