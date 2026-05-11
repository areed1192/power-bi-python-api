"""Demonstrates how to use the `Admin` service."""

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
capacity_id = config.get("power_bi_api", "capacity_id")
group_id = config.get("power_bi_api", "group_id")

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=["https://analysis.windows.net/powerbi/api/.default"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `Admin` service.
admin_service = power_bi_client.admin()

# ================================================================== #
#                         Activity Events                             #
# ================================================================== #

# Get activity events for a specific UTC day.
pprint(
    admin_service.get_activity_events(
        start_date_time="'2026-05-11T00:00:00.000Z'",
        end_date_time="'2026-05-11T23:59:59.000Z'",
    )
)

# ================================================================== #
#                        Encryption Keys                              #
# ================================================================== #

# Get all tenant encryption keys.
pprint(admin_service.get_encryption_keys())

# ================================================================== #
#                          Capacities                                 #
# ================================================================== #

# Get all capacities for the organization.
pprint(admin_service.get_capacities())

# Get capacities with expanded tenant key info.
pprint(admin_service.get_capacities(expand="tenantKey"))

# Get users for a specific capacity.
pprint(
    admin_service.get_capacity_users(
        capacity_id=capacity_id
    )
)

# ================================================================== #
#                         Refreshables                                #
# ================================================================== #

# Get a list of refreshables for the organization (top 20).
pprint(admin_service.get_refreshables(top=20))

# Get refreshables with expanded capacity and group info.
pprint(
    admin_service.get_refreshables(
        top=50,
        expand="capacity,group",
    )
)

# Get refreshables filtered by average duration greater than 30 minutes.
pprint(
    admin_service.get_refreshables(
        top=100,
        filter_by="averageDuration gt 1800",
    )
)

# Get refreshables for a specific capacity.
pprint(
    admin_service.get_refreshables_for_capacity(
        capacity_id=capacity_id,
        top=10,
    )
)

# ================================================================== #
#                             Apps                                    #
# ================================================================== #

# Get all apps for the organization.
pprint(admin_service.get_apps(top=100))

# Get users for a specific app.
pprint(
    admin_service.get_app_users(app_id="f089354e-8366-4e18-aea3-4cb4a3a50b48")
)

# ================================================================== #
#                          Dashboards                                 #
# ================================================================== #

# Get all dashboards for the organization.
pprint(admin_service.get_dashboards(top=100))

# Get dashboards with tiles expanded.
pprint(admin_service.get_dashboards(expand="tiles", top=50))

# Get dashboards in a specific workspace.
pprint(
    admin_service.get_dashboards_in_group(
        group_id=group_id
    )
)

# Get users for a specific dashboard.
pprint(
    admin_service.get_dashboard_users(
        dashboard_id="4668133c-ae3f-42fb-ad7c-214a8623280c"
    )
)

# Get tiles for a specific dashboard.
pprint(
    admin_service.get_tiles(
        dashboard_id="4668133c-ae3f-42fb-ad7c-214a8623280c"
    )
)

# Get subscriptions for a specific dashboard.
pprint(
    admin_service.get_dashboard_subscriptions(
        dashboard_id="4668133c-ae3f-42fb-ad7c-214a8623280c"
    )
)

# ================================================================== #
#                           Dataflows                                 #
# ================================================================== #

# Get all dataflows for the organization.
pprint(admin_service.get_dataflows(top=100))

# Get dataflows in a specific workspace.
pprint(
    admin_service.get_dataflows_in_group(
        group_id=group_id
    )
)

# Get data sources for a specific dataflow.
pprint(
    admin_service.get_dataflow_datasources(
        dataflow_id="928228ba-008d-4fd9-864a-92d2752ee5ce"
    )
)

# Get users for a specific dataflow.
pprint(
    admin_service.get_dataflow_users(
        dataflow_id="928228ba-008d-4fd9-864a-92d2752ee5ce"
    )
)

# Get upstream dataflows for a dataflow in a workspace.
pprint(
    admin_service.get_upstream_dataflows_in_group(
        group_id=group_id,
        dataflow_id="928228ba-008d-4fd9-864a-92d2752ee5ce",
    )
)

# ================================================================== #
#                           Datasets                                  #
# ================================================================== #

# Get all datasets for the organization.
pprint(admin_service.get_datasets(top=100))

# Get datasets in a specific workspace.
pprint(
    admin_service.get_datasets_in_group(
        group_id=group_id
    )
)

# Get users for a specific dataset.
pprint(
    admin_service.get_dataset_users(
        dataset_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    )
)

# Get data sources for a specific dataset.
pprint(
    admin_service.get_datasources(
        dataset_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    )
)

# Get dataset-to-dataflow links in a workspace.
pprint(
    admin_service.get_dataset_to_dataflows_links_in_group(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# ================================================================== #
#                            Groups                                   #
# ================================================================== #

# Get all workspaces for the organization (top 100).
pprint(admin_service.get_groups(top=100))

# Get workspaces with users expanded.
pprint(admin_service.get_groups(top=100, expand="users"))

# Get deleted workspaces.
pprint(
    admin_service.get_groups(
        top=100,
        filter_by="state eq 'Deleted'",
    )
)

# Get a specific workspace.
pprint(
    admin_service.get_group(group_id="f78705a2-bead-4a5c-ba57-166794b05c78")
)

# Get users for a specific workspace.
pprint(
    admin_service.get_group_users(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# Get unused artifacts in a workspace.
pprint(
    admin_service.get_unused_artifacts(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# Add a user to a workspace as Admin.
pprint(
    admin_service.add_group_user(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        user_details={
            "emailAddress": "john@contoso.com",
            "groupUserAccessRight": "Admin",
        },
    )
)

# Delete a user from a workspace.
pprint(
    admin_service.delete_group_user(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        user="john@contoso.com",
    )
)

# Restore a deleted workspace.
pprint(
    admin_service.restore_deleted_group(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        email_address="john@contoso.com",
        name="Restored Workspace",
    )
)

# Update a workspace's properties.
pprint(
    admin_service.update_group(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
        group_properties={
            "name": "Updated Sales Results",
            "description": "Refreshed sales numbers",
        },
    )
)

# ================================================================== #
#                           Imports                                   #
# ================================================================== #

# Get all imports for the organization.
pprint(admin_service.get_imports(top=100))

# ================================================================== #
#                     Information Protection                          #
# ================================================================== #

# Set sensitivity labels on Power BI items.
pprint(
    admin_service.set_labels(
        label_details={
            "artifacts": {
                "reports": [{"id": "fe472f5e-636e-4c10-a1c6-7e9edc0b542c"}],
                "dashboards": [{"id": "fe472f5e-636e-4c10-a1c6-7e9edc0b542a"}],
            },
            "labelId": "fe472f5e-636e-4c10-a1c6-7e9edc0b542p",
        }
    )
)

# Remove sensitivity labels from Power BI items.
pprint(
    admin_service.remove_labels(
        artifacts={
            "reports": [{"id": "fe472f5e-636e-4c10-a1c6-7e9edc0b542c"}],
            "dashboards": [{"id": "fe472f5e-636e-4c10-a1c6-7e9edc0b542a"}],
        }
    )
)

# ================================================================== #
#                          Pipelines                                  #
# ================================================================== #

# Get all deployment pipelines for the organization.
pprint(admin_service.get_pipelines(top=100))

# Get users for a specific pipeline.
pprint(
    admin_service.get_pipeline_users(
        pipeline_id="a5ded933-57b7-4f46-b072-ed4c1f9d5824"
    )
)

# ================================================================== #
#                           Profiles                                  #
# ================================================================== #

# Get all service principal profiles.
pprint(admin_service.get_profiles(top=100))

# ================================================================== #
#                           Reports                                   #
# ================================================================== #

# Get all reports for the organization.
pprint(admin_service.get_reports(top=100))

# Get reports in a specific workspace.
pprint(
    admin_service.get_reports_in_group(
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
    )
)

# Get users for a specific report.
pprint(
    admin_service.get_report_users(
        report_id="5DBA60B0-D9A7-42AE-B12C-6D9D51E7739A"
    )
)

# Get subscriptions for a specific report.
pprint(
    admin_service.get_report_subscriptions(
        report_id="5DBA60B0-D9A7-42AE-B12C-6D9D51E7739A"
    )
)

# ================================================================== #
#                            Users                                    #
# ================================================================== #

# Get a list of Power BI items a user has access to.
pprint(
    admin_service.get_user_artifact_access(
        user_id="f089354e-8366-4e18-aea3-4cb4a3a50b48"
    )
)

# Filter artifact access by type.
pprint(
    admin_service.get_user_artifact_access(
        user_id="f089354e-8366-4e18-aea3-4cb4a3a50b48",
        artifact_types="Report,Dashboard",
    )
)

# Get subscriptions for a specific user.
pprint(
    admin_service.get_user_subscriptions(
        user_id="f089354e-8366-4e18-aea3-4cb4a3a50b48"
    )
)

# ================================================================== #
#                    Widely Shared Artifacts                          #
# ================================================================== #

# Get reports shared to the whole organization via links.
pprint(admin_service.get_links_shared_to_whole_organization())

# Get items published to web.
pprint(admin_service.get_published_to_web())

# ================================================================== #
#                       Workspace Info                                #
# ================================================================== #

# Get modified workspaces since a specific date.
pprint(
    admin_service.get_modified_workspaces(
        modified_since="2024-06-01T00:00:00.0000000Z",
        exclude_personal_workspaces=True,
    )
)

# Initiate a workspace scan.
scan_response = admin_service.post_workspace_info(
    workspaces=[
        "d507422c-8d6d-4361-ac7a-30074a8cd0a1",
        "67b7e93a-3fb3-493c-9e41-2c5051008f24",
    ],
    lineage=True,
    datasource_details=True,
    dataset_schema=True,
)
pprint(scan_response)

# Check scan status using the scan ID from the response above.
scan_id = scan_response.get("id")
if scan_id:
    pprint(admin_service.get_scan_status(scan_id=scan_id))

    # Get the scan result (only after status is "Succeeded").
    pprint(admin_service.get_scan_result(scan_id=scan_id))
