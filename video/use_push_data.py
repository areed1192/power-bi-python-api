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
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Initialize the PushDatasets service.
push_dataset_service = power_bi_client.push_datasets()

from powerbi.utils import Table
from powerbi.utils import Column
from powerbi.utils import Dataset
from powerbi.enums import ColumnDataTypes


# Create a new table object.
table_sales_info = Table(name='sales_table_info')

# Create a new column for our partner name.
name_column = Column(name='partner_name', data_type=ColumnDataTypes.String)
sale_column = Column(name='partner_sales', data_type=ColumnDataTypes.Decimal)

# Add the columns to the table.
table_sales_info.add_column(column=name_column)
table_sales_info.add_column(column=sale_column)

# Define a new dataset.
new_dataset = Dataset(name='sales_info_dataset')
new_dataset.default_mode = 'Push'

# Add the table to the dataset.
new_dataset.add_table(table=table_sales_info)

# # print the new dataset.
# pprint(
#     push_dataset_service.post_dataset(
#         dataset=new_dataset
#     )
# )

dataset_id = '23e36697-9ae8-4774-b243-0a83d9713e28'

# Define some fake data.
new_rows = [
    {
        'partner_name': 'Alex Reed',
        'partner_sales': 1000.30
    },
    {
        'partner_name': 'John Reed',
        'partner_sales': 2000.30
    },
    {
        'partner_name': 'James Reed',
        'partner_sales': 5000.30
    }
]

pprint(
push_dataset_service.post_dataset_rows(
    dataset_id=dataset_id,
    table_name='sales_table_info',
    rows=new_rows
))