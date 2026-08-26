"""Demonstrates how to use the `CopyJobs` service.

Copy Jobs are a Microsoft Fabric resource, not a Power BI resource, so this
client must be authenticated with a Fabric-compatible scope instead of the
default Power BI scope.
"""

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

# Initialize the Client with a Fabric-compatible scope.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=["https://api.fabric.microsoft.com/.default"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `CopyJobs` service.
copy_jobs_service = power_bi_client.copy_jobs()

workspace_id = "cfafbeb1-8037-4d0c-896e-a46fb27ff229"

# Get all the Copy Jobs in a workspace.
pprint(copy_jobs_service.get_copy_jobs(workspace_id=workspace_id))

# Create a new Copy Job.
new_copy_job = copy_jobs_service.create_copy_job(
    workspace_id=workspace_id,
    display_name="CopyJob 1",
    description="Created from the python-power-bi sample.",
)
pprint(new_copy_job)

copy_job_id = new_copy_job.get("id")

# Get a specific Copy Job.
pprint(
    copy_jobs_service.get_copy_job(workspace_id=workspace_id, copy_job_id=copy_job_id)
)

# Update the Copy Job's display name.
pprint(
    copy_jobs_service.update_copy_job(
        workspace_id=workspace_id,
        copy_job_id=copy_job_id,
        display_name="CopyJob 1 (renamed)",
    )
)

# Get the Copy Job's definition.
pprint(
    copy_jobs_service.get_copy_job_definition(
        workspace_id=workspace_id, copy_job_id=copy_job_id
    )
)

# Reset all entities in the Copy Job so the next run performs a full copy.
pprint(
    copy_jobs_service.reset_copy_job(
        workspace_id=workspace_id,
        copy_job_id=copy_job_id,
        reset_all_copy_job_entities=True,
    )
)

# Delete the Copy Job.
pprint(
    copy_jobs_service.delete_copy_job(
        workspace_id=workspace_id, copy_job_id=copy_job_id
    )
)
