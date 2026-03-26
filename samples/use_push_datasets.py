"""Demonstrates how to use the `PushDatasets` service."""

from pprint import pprint
from configparser import ConfigParser

from powerbi.utils import Table
from powerbi.utils import Column
from powerbi.utils import Dataset
from powerbi.enums import ColumnDataTypes
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

# Initialize the `PushDatasets` service.
push_datasets_service = power_bi_client.push_datasets()

# Define workspace IDs.
dev_group_id = "f78705a2-bead-4a5c-ba57-166794b05c78"
prod_group_id = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"

# ---------------------------------------------------------------
# GET: Pull the tables from a Dataset in the Prod workspace.
# ---------------------------------------------------------------
pprint(
    push_datasets_service.get_tables(
        dataset_id="8ea21119-fb8f-4592-b2b8-141b824a2b7e",
        group_id=prod_group_id,
    )
)

# ---------------------------------------------------------------
# POST: Build and create a new Dataset in the Dev workspace.
# ---------------------------------------------------------------

# Create a new Table Object.
table_sales = Table(name="sales_table")

# Create columns.
name_column = Column(name="partner_name", data_type=ColumnDataTypes.STRING)
sales_column = Column(name="partner_sales", data_type=ColumnDataTypes.DECIMAL)

# Add the columns to the table.
table_sales.add_column(column=name_column)
table_sales.add_column(column=sales_column)

# Define a new dataset.
new_dataset = Dataset(name="sales_dataset", tables=[])
new_dataset.default_mode = "Push"

# Add the Sales table to it.
new_dataset.add_table(table=table_sales)

# Post the dataset to the Dev workspace with FIFO retention.
pprint(
    push_datasets_service.post_dataset(
        dataset=new_dataset,
        default_retention_policy="basicFIFO",
        group_id=dev_group_id,
    )
)

# ---------------------------------------------------------------
# POST ROWS: Add data rows to the new dataset in the Dev workspace.
# ---------------------------------------------------------------
new_rows = [
    {"partner_name": "Alex Reed", "partner_sales": 1000.30},
    {"partner_name": "John Reed", "partner_sales": 2000.30},
    {"partner_name": "James Reed", "partner_sales": 5000.30},
]

push_datasets_service.post_dataset_rows(
    dataset_id="8ea21119-fb8f-4592-b2b8-141b824a2b7e",
    table_name="sales_table",
    rows=new_rows,
    group_id=dev_group_id,
)

# ---------------------------------------------------------------
# PUT: Update the table schema in the Dev workspace.
# ---------------------------------------------------------------
new_table_sales = Table(name="sales_table")

name_column = Column(name="partner_name", data_type=ColumnDataTypes.STRING)
sales_column = Column(name="partner_sales", data_type=ColumnDataTypes.DECIMAL)
location_column = Column(name="partner_location", data_type=ColumnDataTypes.STRING)
location_column.data_category = "Location"

new_table_sales.add_column(column=name_column)
new_table_sales.add_column(column=sales_column)
new_table_sales.add_column(column=location_column)

pprint(
    push_datasets_service.put_dataset(
        dataset_id="8ea21119-fb8f-4592-b2b8-141b824a2b7e",
        table_name="sales_table",
        table=new_table_sales,
        group_id=dev_group_id,
    )
)

# Post the updated rows.
new_rows = [
    {
        "partner_name": "Alex Reed",
        "partner_sales": 1000.30,
        "partner_location": "Great Falls, VA",
    },
    {
        "partner_name": "John Reed",
        "partner_sales": 2000.30,
        "partner_location": "Houston, TX",
    },
    {
        "partner_name": "James Reed",
        "partner_sales": 5000.30,
        "partner_location": "San Diego, CA",
    },
]

push_datasets_service.post_dataset_rows(
    dataset_id="8ea21119-fb8f-4592-b2b8-141b824a2b7e",
    table_name="sales_table",
    rows=new_rows,
    group_id=dev_group_id,
)

# ---------------------------------------------------------------
# DELETE ROWS: Clear all rows from the table in the Dev workspace.
# ---------------------------------------------------------------
push_datasets_service.delete_dataset_rows(
    dataset_id="8ea21119-fb8f-4592-b2b8-141b824a2b7e",
    table_name="sales_table",
    group_id=dev_group_id,
)
