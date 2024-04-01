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
    # You need to make sure you request this permission, but you can't have it
    # with the `.default` scope.
    scope=["https://analysis.windows.net/powerbi/api/Pipeline.ReadWrite.All"],
    redirect_uri=redirect_uri,
    credentials="config/power_bi_state.jsonc",
)

# Initialize the `Datasets` service.
datasets_service = power_bi_client.datasets()

# Define the Groups.
group_id = [
    "1c118f15-4e44-4cde-8608-28ae3c588766",
    "f4cb914f-4750-4003-8dda-492439851168",
]

# Define the Refresh Schedule.

refresh_schedules = {
    "non-core-dimensions": {
        "value": {
            "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "times": [
                "06:30",
                "07:30",
                "08:30",
                "09:30",
                "10:30",
                "11:30",
                "13:30",
                "14:30",
                "15:30",
                "16:30",
            ],
            "enabled": True,
            "localTimeZoneId": "Pacific Standard Time",
            "notifyOption": "MailOnFailure",
        }
    },
    "core-dimensions": {
        "value": {
            "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "times": [
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
            ],
            "enabled": True,
            "localTimeZoneId": "Pacific Standard Time",
            "notifyOption": "MailOnFailure",
        }
    }
}


# Loop through the groups.
for group in group_id:

    # Get all the dataflows in a group.
    datasets = datasets_service.get_datasets_in_group(group_id=group)

    # Get the list of dataflows.
    list_of_datasets = datasets["value"]

    # Grab the ID.
    for dataset in list_of_datasets:

        pprint(dataset)

        dataset_id = dataset["id"]

        response = datasets_service.update_refresh_schedule_in_group(
            group_id=group, dataset_id=dataset_id, refresh_schedule=refresh_schedule
        )

        # pprint(response)
