from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient
from powerbi.enums import ExportFileFormats

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

# Initialize the `Reports` service.
reports_service = power_bi_client.reports()

# Grab all the reports in our workspace.
pprint(reports_service.get_reports())

# Grab all the reports from a specific workspace.
pprint(
    reports_service.get_group_reports(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
    )
)

# Grab a specific report from our workspace.
pprint(
    reports_service.get_report(
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
    )
)

# Grab a specific report from a specific workspace.
pprint(
    reports_service.get_group_report(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
    )
)

# Grab the pages from a specific report.
pprint(
    reports_service.get_pages(
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
    )
)

# Grab the pages from a specific report in a specific workspace.
pprint(
    reports_service.get_group_pages(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
    )
)

# Grab a specific page from a specific report.
pprint(
    reports_service.get_page(
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
        page_name='ReportSection'
    )
)

# Grab a specific page from a specific report in a specific workspace.
pprint(
    reports_service.get_group_page(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
        page_name='ReportSection'
    )
)

# Clone a specific report.
pprint(
    reports_service.clone_report(
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
        name='MyNewReport'
    )
)

# Clone the same report but this time from a specific workspace.
pprint(
    reports_service.clone_group_report(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
        report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
        name='MyOtherNewReport'
    )
)


# Delete a specific report.
pprint(
    reports_service.delete_report(
        report_id='c19c7599-7f92-4d11-b384-c9ae33368304'
    )
)

# Delete a specific report from a specific workspace.
pprint(
    reports_service.delete_group_report(
        group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
        report_id='f0ca06d0-4a40-4329-823d-6184d9a3f468',
    )
)

# Export a report from "My Workspace".
my_report_content = reports_service.export_report(
    report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
)

with open(file='my_report_export.pbix', mode='wb+') as power_bi_file:
    power_bi_file.write(my_report_content)


# Export a report from a specific workspace.
my_report_content = reports_service.export_group_report(
    group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
    report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
)


with open(file='my_group_report_export.pbix', mode='wb+') as power_bi_file:
    power_bi_file.write(my_report_content)

pprint(
    reports_service.get_datasources(
        report_id='cd5fd3b0-e806-4e38-a02b-ff13ef594c09'
    )
)


my_report_content = reports_service.export_to_file(
    report_id='cd5fd3b0-e806-4e38-a02b-ff13ef594c09',
    file_format=ExportFileFormats.Pdf
)

pprint(my_report_content)

with open(file='my_group_report_export.pdf', mode='wb+') as power_bi_file:
    power_bi_file.write(my_report_content)
