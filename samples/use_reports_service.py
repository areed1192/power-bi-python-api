"""Demonstrates how to use the `Reports` service."""

from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient
from powerbi.enums import ExportFileFormats

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

# Initialize the `Reports` service.
reports_service = power_bi_client.reports()

# Grab all the reports in our workspace.
pprint(reports_service.get_reports())

# Grab all the reports from a specific workspace.
pprint(
    reports_service.get_reports(group_id="f78705a2-bead-4a5c-ba57-166794b05c78")
)

# Grab a specific report from our workspace.
pprint(reports_service.get_report(report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082"))

# Grab a specific report from a specific workspace.
pprint(
    reports_service.get_report(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Grab the pages from a specific report.
pprint(reports_service.get_pages(report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082"))

# Grab the pages from a specific report in a specific workspace.
pprint(
    reports_service.get_pages(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Grab a specific page from a specific report.
pprint(
    reports_service.get_page(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082", page_name="ReportSection"
    )
)

# Grab a specific page from a specific report in a specific workspace.
pprint(
    reports_service.get_page(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
        page_name="ReportSection",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Clone a specific report.
pprint(
    reports_service.clone_report(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082", name="MyNewReport"
    )
)

# Clone the same report but this time from a specific workspace.
pprint(
    reports_service.clone_report(
        report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
        name="MyOtherNewReport",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)


# Delete a specific report.
pprint(reports_service.delete_report(report_id="c19c7599-7f92-4d11-b384-c9ae33368304"))

# Delete a specific report from a specific workspace.
pprint(
    reports_service.delete_report(
        report_id="f0ca06d0-4a40-4329-823d-6184d9a3f468",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Export a report from "My Workspace".
my_report_content = reports_service.export_report(
    report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082"
)

with open(file="my_report_export.pbix", mode="wb+") as power_bi_file:
    power_bi_file.write(my_report_content)


# Export a report from a specific workspace.
my_report_content = reports_service.export_report(
    report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)


with open(file="my_group_report_export.pbix", mode="wb+") as power_bi_file:
    power_bi_file.write(my_report_content)

# Grab datasources from a report in "My Workspace".
pprint(
    reports_service.get_datasources(report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09")
)

# Grab datasources from a report in a specific workspace.
pprint(
    reports_service.get_datasources(
        report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Export a report to a file format from "My Workspace".
my_report_content = reports_service.export_to_file(
    report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09", file_format=ExportFileFormats.PDF
)

pprint(my_report_content)

# Export a report to a file format from a specific workspace.
my_report_content = reports_service.export_to_file(
    report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
    file_format=ExportFileFormats.PDF,
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)

pprint(my_report_content)

# Get the export to file status for a report in "My Workspace".
pprint(
    reports_service.get_export_to_file_status(
        report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
        export_id="Mi9C5419i....PS4=",
    )
)

# Get the export to file status for a report in a specific workspace.
pprint(
    reports_service.get_export_to_file_status(
        report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
        export_id="Mi9C5419i....PS4=",
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Get the exported file from "My Workspace".
file_content = reports_service.get_file_of_export_to_file(
    report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
    export_id="Mi9C5419i....PS4=",
)

with open(file="my_exported_report.pdf", mode="wb+") as power_bi_file:
    power_bi_file.write(file_content)

# Get the exported file from a specific workspace.
file_content = reports_service.get_file_of_export_to_file(
    report_id="cd5fd3b0-e806-4e38-a02b-ff13ef594c09",
    export_id="Mi9C5419i....PS4=",
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)

with open(file="my_group_exported_report.pdf", mode="wb+") as power_bi_file:
    power_bi_file.write(file_content)

# Update report content in "My Workspace".
pprint(
    reports_service.update_report_content(
        report_id="f0ca06d0-4a40-4329-823d-6184d9a3f468",
        request_body={
            "sourceReport": {
                "sourceReportId": "8e4d5880-81d6-4804-ab97-054665050799",
                "sourceWorkspaceId": "2f42a406-a075-4a15-bbf2-97ef958c94cb",
            },
            "sourceType": "ExistingReport",
        },
    )
)

# Update report content in a specific workspace.
pprint(
    reports_service.update_report_content(
        report_id="f0ca06d0-4a40-4329-823d-6184d9a3f468",
        request_body={
            "sourceReport": {
                "sourceReportId": "8e4d5880-81d6-4804-ab97-054665050799",
                "sourceWorkspaceId": "2f42a406-a075-4a15-bbf2-97ef958c94cb",
            },
            "sourceType": "ExistingReport",
        },
        group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    )
)

# Bind a paginated report to a gateway.
reports_service.bind_to_gateway(
    report_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
    gateway_object_id="1f69e798-5852-4fdd-ab01-33bb14b6e934",
    bind_details=[
        {
            "dataSourceName": "DataSource1",
            "dataSourceObjectId": "dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb",
        }
    ],
)

# Bind a paginated report to a gateway in a specific workspace.
reports_service.bind_to_gateway(
    report_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
    gateway_object_id="1f69e798-5852-4fdd-ab01-33bb14b6e934",
    bind_details=[
        {
            "dataSourceName": "DataSource1",
            "dataSourceObjectId": "dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb",
        }
    ],
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)

# Rebind a report to a different dataset.
reports_service.rebind_report(
    report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
    dataset_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
)

# Rebind a report to a different dataset in a specific workspace.
reports_service.rebind_report(
    report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
    dataset_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)

# Take over a paginated report's data sources in a specific workspace.
reports_service.take_over_in_group(
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
    report_id="cec3fab1-2fc2-424e-8d36-d6180ef05082",
)

# Update data sources of a paginated report.
reports_service.update_datasources(
    report_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
    update_details=[
        {
            "datasourceName": "SqlDatasource",
            "connectionDetails": {
                "server": "New-Sql-Server",
                "database": "New-Sql-Database",
            },
        }
    ],
)

# Update data sources of a paginated report in a specific workspace.
reports_service.update_datasources(
    report_id="cfafbeb1-8037-4d0c-896e-a46fb27ff229",
    update_details=[
        {
            "datasourceName": "SqlDatasource",
            "connectionDetails": {
                "server": "New-Sql-Server",
                "database": "New-Sql-Database",
            },
        }
    ],
    group_id="f78705a2-bead-4a5c-ba57-166794b05c78",
)
