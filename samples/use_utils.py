"""Demonstrates how to use the `powerbi.utils` module."""

from powerbi.utils import Table
from powerbi.utils import Column
from powerbi.utils import Dataset
from powerbi.enums import ColumnDataTypes

# Create a new Table Object.
table_sales = Table(name="sales_table")

# Create a new column for our partner name.
name_column = Column(name="partner_name", data_type=ColumnDataTypes.STRING)

# Also create a new one for our sales numbers.
sales_column = Column(name="partner_sales", data_type=ColumnDataTypes.DECIMAL)

# Add the columns to the table.
table_sales.add_column(column=name_column)
table_sales.add_column(column=sales_column)

# Define a new dataset.
new_dataset = Dataset(name="sales_dataset", tables=[])

# Add the Sales table to it.
new_dataset.add_table(table=table_sales)

# Print the new dataset.
print(new_dataset)
print(new_dataset.to_dict())
print(table_sales.to_dict())
print(name_column.to_dict())
