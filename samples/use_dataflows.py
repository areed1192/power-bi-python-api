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

# Initialize the `Dataflows` service.
dataflows_service = power_bi_client.dataflows()

# Define the Groups.
group_id = [
    "1c118f15-4e44-4cde-8608-28ae3c588766",
    "f4cb914f-4750-4003-8dda-492439851168",
]

# Define the Refresh Schedule.
refresh_schedule = {
    "value": {
        "days": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ],
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
            "16:00"
        ],
        "enabled": True,
        "localTimeZoneId": "Pacific Standard Time",
        "notifyOption": "MailOnFailure",
    }
}

# Loop through the groups.
for group in group_id:

    # Get all the dataflows in a group.
    dataflows = dataflows_service.get_dataflows(group_id=group)

    # Get the list of dataflows.
    list_of_dataflows = dataflows["value"]

    # Grab the ID.
    for dataflow in list_of_dataflows:

        dataflow_id = dataflow["objectId"]

        response = dataflows_service.update_refresh_schedule(
            group_id=group,
            dataflow_id=dataflow_id,
            refresh_schedule=refresh_schedule
        )

        pprint(response)

    # pprint(list_of_dataflows.keys())
    # pprint(
    #     dataflows_service.get_dataflows(group_id=group)
    # )
