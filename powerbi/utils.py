import json
from datetime import datetime
from datetime import date
from typing import Union
from enum import Enum

# https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/entity-data-model-primitive-data-types
# https://docs.microsoft.com/en-us/power-bi/developer/automation/api-dataset-properties#data-type-restrictions
# https://docs.microsoft.com/en-us/analysis-services/multidimensional-models/mdx/mdx-cell-properties-format-string-contents?view=asallproducts-allversions


class PowerBiEncoder(json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        json.JSONEncoder.__init__(self, *args, **kwargs)

    def default(self, obj):
        if isinstance(obj, Columns):
            return obj.columns
        elif isinstance(obj, Measures):
            return obj.measures
        if isinstance(obj, Column):
            return obj.column
        elif isinstance(obj, Measure):
            return obj.measure
        elif isinstance(obj, Dataset):
            return obj.push_dataset
        elif isinstance(obj, Tables):
            return obj.tables
        elif isinstance(obj, Table):
            return obj.table
        elif isinstance(obj, Relationships):
            return obj.relationships
        elif isinstance(obj, Relationship):
            return obj.relationship


class Column():

    """
    ### Overview
    ----
    Represents a column inside of a `PowerBiTable`
    object.
    """

    def __init__(self, name: str, data_type: Union[str, Enum]) -> None:
        """Initializes a new `Column` object.

        ### Parameters
        ----
        name : str
            The column name.

        data_type : Union[str, Enum]
            One of the allowed data types.
        """

        if isinstance(data_type, Enum):
            data_type = data_type.value

        self.column = {
            'name': name,
            'dataType': data_type,
            'dataCategory': '',
            'formatString': '',
            'isHidden': False,
            'sortByColumn': '',
            'summarizeBy': ''
        }

    @property
    def name(self) -> str:
        """The column name.

        ### Returns
        ----
        str :
            The column name.
        """
        return self.column.get('name', None)

    @name.setter
    def name(self, name: str) -> None:
        """Sets the column name.

        ### Parameters
        ----
        name : str
            The name you want the column to be.
        """

        self.column.update({'name': name})

    @property
    def data_type(self) -> str:
        """Returns the data type of column.

        ### Returns
        ----
        str :
            One of the allowed data types.
        """
        return self.column.get('dataType', None)

    @data_type.setter
    def data_type(self, data_type: Union[str, Enum]) -> None:
        """Sets the column data type.

        ### Parameters
        ----
        data_type : Union[str, Enum]
            One of the allowed data types.
        """

        if isinstance(data_type, Enum):
            data_type = data_type.value

        self.column.update({'dataType': data_type})

    @property
    def format_string(self) -> str:
        """Returns the format string of the column.

        ### Returns
        ----
        str :
            The format of the column as specified in
            FORMAT_STRING.
        """
        return self.column.get('formatString', None)

    @format_string.setter
    def format_string(self, format_string: str) -> None:
        """Sets the optional format of the column.

        ### Parameters
        ----
        format_string : str
            The format of the column as specified in FORMAT_STRING.
        """

        self.column.update({'formatString': format_string})

    @property
    def data_category(self) -> str:
        """Returns the data category of the column,
        if any is specified.

        ### Returns
        ----
        str :
            String value to be used for the data category
            which describes the data within this column.
        """
        return self.column.get('dataCategory', None)

    @data_category.setter
    def data_category(self, data_category: str) -> None:
        """Sets the data category of the column.

        ### Parameters
        ----
        data_category : str
            Value to be used for the data category which
            describes the data within this column. Some
            common values include: `[Address, City, Continent,
            Country, Image, ImageUrl, Latitude, Longitude,
            Organization, Place, PostalCode, StateOrProvince,
            WebUrl]`
        """

        self.column.update({'dataCategory': data_category})

    @property
    def is_hidden(self) -> bool:
        """Returns the property indicating if the column
        is hidden from view.

        ### Returns
        ----
        bool :
            If `True` the column is hidden, `False`
            otherwise.
        """
        return self.column.get('isHidden', None)

    @is_hidden.setter
    def is_hidden(self, is_hidden: bool) -> None:
        """Sets the `isHidden` property of the column.

        ### Parameters
        ----
        is_hidden : bool
            Property indicating if the column is hidden from view.
            Default is `False`.
        """

        self.column.update({'isHidden': is_hidden})

    @property
    def sort_by_column(self) -> str:
        """Returns the property indicating the column
        that the table is ordered by.

        ### Returns
        ----
        str :
            String name of a column in the same table to be
            used to order the current column.
        """
        return self.column.get('sortByColumn', None)

    @sort_by_column.setter
    def sort_by_column(self, sort_by_column: str) -> None:
        """Sets the `sortByColumn` property of the column.

        ### Parameters
        ----
        sort_by_column : str
            String name of a column in the same table to be
            used to order the current column.
        """

        self.column.update({'sortByColumn': sort_by_column})

    @property
    def summarize_by(self) -> str:
        """Returns the property indicating how the column
        is aggregated.

        ### Returns
        ----
        str :
            Aggregate Function to use for summarizing this
            column.
        """
        return self.column.get('summarizeBy', None)

    @summarize_by.setter
    def summarize_by(self, summarize_by: Union[str, Enum]) -> None:
        """Sets the `summarizeBy` property of the column.

        ### Parameters
        ----
        summarize_by : Union[str, Enum]
            Aggregate Function to use for summarizing this
            column.
        """

        if isinstance(summarize_by, Enum):
            summarize_by = summarize_by.value

        self.column.update({'summarizeBy': summarize_by})

    def to_dict(self) -> dict:
        """Returns the column properties.

        ### Returns
        ----
        dict
            A dictionary containing each of the column
            properties.
        """
        return self.column


class Measure():

    """
    ### Overview
    ----
    Represents a `Measure` inside of a `PowerBiColumn`
    object.
    """

    def __init__(self, name: str, expression: str) -> None:
        """Initializes a new `Measure` object.

        ### Parameters
        -----
        name : str
            The measure name.

        expression : str
            A valid DAX expression.
        """

        self.measure = {
            'name': name,
            'expression': expression,
            'formatString': '',
            'isHidden': False,
        }

    @property
    def name(self) -> str:
        """The measure name.

        ### Returns
        ----
        str :
            The measure name.
        """
        return self.measure.get('name', None)

    @name.setter
    def name(self, name: str) -> None:
        """Sets the measure name.

        ### Parameters
        ----
        name : str
            The name you want the measure to be.
        """

        self.measure.update({'name': name})

    @property
    def expression(self) -> str:
        """Returns the measure DAX expression.

        ### Returns
        ----
        str :
            A valid DAX expression.
        """
        return self.measure.get('dataType', None)

    @expression.setter
    def expression(self, expression: str) -> None:
        """Sets the measure DAX expression.

        ### Parameters
        ----
        expression : str
            A valid DAX expression.
        """

        self.measure.update({'expression': expression})

    @property
    def format_string(self) -> str:
        """Returns the format string of the measure.

        ### Returns
        ----
        str :
            The format of the measure as specified in
            FORMAT_STRING.
        """
        return self.measure.get('formatString', None)

    @format_string.setter
    def format_string(self, format_string: str) -> None:
        """Sets the optional format of the measure.

        ### Parameters
        ----
        format_string : str
            The format of the measure as specified in
            FORMAT_STRING.
        """

        self.measure.update({'formatString': format_string})

    @property
    def is_hidden(self) -> bool:
        """Returns the property indicating if the measure
        is hidden from client tools.

        ### Returns
        ----
        bool :
            If `True` the measure is hidden, `False`
            otherwise.
        """
        return self.measure.get('isHidden', None)

    @is_hidden.setter
    def is_hidden(self, is_hidden: bool) -> None:
        """Sets the `isHidden` property of the column.

        ### Parameters
        ----
        is_hidden : bool
            Property indicating if the measure is hidden from
            client tools. Default is `False`.
        """

        self.measure.update({'isHidden': is_hidden})

    def to_dict(self) -> dict:
        """Returns the measure properties.

        ### Returns
        ----
        dict
            A dictionary containing each of the measure
            properties.
        """

        return self.measure

    def to_json(self) -> str:
        """Returns the measure properties as
        a JSON formatted string.

        ### Returns
        ----
        str
            A string that contains the measure
            properties.
        """
        return json.dumps(obj=self.measure, indent=4)


class Relationship():

    """
    ### Overview
    ----
    Represents a `Relationship` inside of a `PowerBiModel`
    object.
    """

    def __init__(self, name: str, from_table: str, to_table: str, from_column: str, to_column: str) -> None:
        """Initializes a new `Relationship` object.

        ### Parameters
        -----
        name : str
            The measure name.

        expression : str
            A valid DAX expression.
        """

        self.relationship = {
            'name': name,
            'fromColumn': from_column,
            'toColumn': to_column,
            'fromTable': from_table,
            'toTable': to_table,
            'crossFilteringBehavior': 'OneDirection'
        }

    @property
    def name(self) -> str:
        """The relationship name.

        ### Returns
        ----
        str :
            The relationship name.
        """
        return self.relationship.get('name', None)

    @name.setter
    def name(self, name: str) -> None:
        """Sets the relationship name.

        ### Parameters
        ----
        name : str
            The name you want the relationship
            to be.
        """

        self.relationship.update({'name': name})

    @property
    def from_table(self) -> str:
        """Returns the `fromTable` property.

        ### Returns
        ----
        str :
            Name of the foreign key table.
        """
        return self.relationship.get('fromTable', None)

    @from_table.setter
    def from_table(self, from_table: str) -> None:
        """Sets the `fromTable` propery.

        ### Parameters
        ----
        from_table : str
            Name of the foreign key table.
        """

        self.relationship.update({'fromTable': from_table})

    @property
    def to_table(self) -> str:
        """Returns the `toTable` property.

        ### Returns
        ----
        str :
            Name of the primary key table.
        """
        return self.relationship.get('toTable', None)

    @to_table.setter
    def to_table(self, to_table: str) -> None:
        """Sets the `toTable` propery.

        ### Parameters
        ----
        to_table : str
            Name of the primary key table.
        """

        self.relationship.update({'toTable': to_table})

    @property
    def from_column(self) -> str:
        """Returns the `toColumn` property.

        ### Returns
        ----
        str :
            Name of the foreign key column.
        """
        return self.relationship.get('fromColumn', None)

    @from_column.setter
    def from_column(self, from_column: str) -> None:
        """Sets the `fromColumn` propery.

        ### Parameters
        ----
        from_column : str
            Name of the foreign key column.
        """

        self.relationship.update({'fromColumn': from_column})

    @property
    def to_column(self) -> str:
        """Returns the `toColumn` property.

        ### Returns
        ----
        str :
            Name of the primary key column.
        """
        return self.relationship.get('toColumn', None)

    @to_column.setter
    def to_column(self, to_column: str) -> None:
        """Sets the `toColumn` propery.

        ### Parameters
        ----
        to_column : str
            Name of the primary key column.
        """

        self.relationship.update({'toColumn': to_column})

    @property
    def cross_filtering_behavior(self) -> str:
        """Returns the `crossFilteringBehavior` property.

        ### Returns
        ----
        str :
            The filter direction of the relationship: [`OneDirection`,
            `BothDirections`, `Automatic`].
        """
        return self.relationship.get('crossFilteringBehavior', None)

    @cross_filtering_behavior.setter
    def cross_filtering_behavior(self, cross_filtering_behavior: str = 'OneDirection') -> None:
        """Sets the `crossFilteringBehavior` propery.

        ### Parameters
        ----
        cross_filtering_behavior : str (optional, Default='OneDirection')
            The filter direction of the relationship: [`OneDirection`,
            `BothDirections`, `Automatic`].
        """

        self.relationship.update(
            {'crossFilteringBehavior': cross_filtering_behavior})

    def to_dict(self) -> dict:
        """Returns the relationship properties.

        ### Returns
        ----
        dict
            A dictionary containing each of the relationship
            properties.
        """

        return self.relationship


class Columns():

    """
    ### Overview
    ----
    Represents a collection of `Column` objects
    that are found inside of a `PowerBiTable` object.
    """

    def __init__(self) -> None:
        self.columns = []

    def __setitem__(self, index: int, data: Column) -> None:
        self.columns.append(data)

    def __getitem__(self, index: int) -> Column:
        return self.columns[index]

    def __delitem__(self, index: int) -> None:
        del self.columns[index]

    def __len__(self) -> int:
        return len(self.columns)


class Measures():

    """
    ### Overview
    ----
    Represents a collection of `Measure` objects
    that are found inside of a `PowerBiTable` object.
    """

    def __init__(self) -> None:
        self.measures = []

    def __setitem__(self, index: int, data: Column) -> None:
        self.measures[index] = data

    def __getitem__(self, index: int) -> Column:
        return self.measures[index]

    def __delitem__(self, index: int) -> None:
        del self.measures[index]

    def __len__(self) -> int:
        return len(self.measures)


class Relationships():

    """
    ### Overview
    ----
    Represents a collection of `Relationship` objects
    that are found inside of a `PowerBiDataset` object.
    """

    def __init__(self) -> None:
        self.relationships = []

    def __setitem__(self, index: int, data: Column) -> None:
        self.relationships[index] = data

    def __getitem__(self, index: int) -> Column:
        return self.relationships[index]

    def __delitem__(self, index: int) -> None:
        del self.relationships[index]

    def __len__(self) -> int:
        return len(self.relationships)


class Tables():

    """
    ### Overview
    ----
    Represents a collection of `Table` objects
    that are found inside of a `PowerBiDataset`
    object.
    """

    def __init__(self) -> None:
        self.tables = []

    def __setitem__(self, index: int, data: Column) -> None:
        self.tables.append(data)

    def __getitem__(self, index: int) -> Column:
        return self.tables[index]

    def __delitem__(self, index: int) -> None:
        del self.tables[index]

    def __len__(self) -> int:
        return len(self.tables)


class Table():

    """
    ### Overview
    ----
    Represents a Table inside of a PowerBi
    dataset.
    """

    def __init__(self, name: str) -> None:
        """Initializes the `Table` object.

        ### Parameters
        ----
        name : str
            User defined name of the table.
            It is also used as the identifier
            of the table.
        """

        self._columns = Columns()
        self._measures = Measures()

        self.table = {
            'name': name,
            'columns': self._columns,
            'measures': self._measures,
            'rows': []
        }

    def __repr__(self) -> str:
        """Represents the string representation of the
        table object.

        ### Returns
        ----
        str
            A JSON formatted string.
        """

        return json.dumps(obj=self.table, indent=4, cls=PowerBiEncoder)

    @property
    def name(self) -> str:
        """The table name.

        ### Returns
        ----
        str : 
            User defined name of the table.
            It is also used as the identifier
            of the table.
        """
        return self.table.get('name', None)

    @name.setter
    def name(self, name: str) -> None:
        """Sets the table name.

        ### Parameters
        ----
        name : str
            User defined name of the table.
            It is also used as the identifier
            of the table.
        """

        self.table.update({'name': name})

    @property
    def columns(self) -> str:
        """Gets the `columns` property.

        ### Returns
        ----
        str : 
            Collection of `Column` objects.
        """

        return self._columns

    def add_column(self, column: Column) -> None:
        """Adds a new `Column` to the `Columns`
        collection.

        ### Parameters
        ----
        column : Column
            A `Column` object with the properties
            set.
        """

        self._columns[len(self._columns)] = column

    def get_column(self, index: int) -> Column:
        """Gets a `Column` from the `Columns`
        collection.

        ### Parameters
        ----
        index : int
            The index of the column you want
            to return from the collection.

        ### Returns
        ----
        Column :
            A `PowerBiColumn` object.
        """

        return self._columns[index]

    def del_column(self, index: int) -> None:
        """Deletes a `Column` to the `Columns`
        collection.

        ### Parameters
        ----
        index : int
            The index of the column you want
            to delete from the collection.
        """

        del self._columns[index]

    @property
    def measures(self) -> str:
        """Gets the `measures` property.

        ### Returns
        ----
        str : 
            Collection of `measure` objects.
        """

        return self._measures

    @property
    def add_measure(self, measure: Measure) -> None:
        """Adds a column to the `measures` collection.

        ### Parameters
        ----
        measure : measure 
            A `Measure` object with the properties
            set.
        """

        measures = self.table.get('measures', [])
        measures.append(measure)

    def del_measure(self, index: int = 0) -> None:
        """Deletes a `Measure` in the `measures` collection.

        ### Parameters
        ----
        index : int (optional=, Default=0) 
            The index of the `Measure` object
            that you wish to delete.
        """

        measures = self.table.get('measures', [])
        measures.pop(index)

    def get_measure(self, index: int = 0) -> Column:
        """Gets a `Measure` in the `measures` collection by
        indexing it.

        ### Parameters
        ----
        index : int (optional=, Default=0) 
            The index of the `Measure` object
            that you wish to get.
        """

        return self.table.get('measures', [])[index]

    @property
    def rows(self) -> str:
        """Gets the `rows` property.

        ### Returns
        ----
        str :
            Collection of `row` objects.
        """

        return self.table.get('rows', [])

    @property
    def add_row(self, row: dict) -> None:
        """Adds a `Row` object to the `rows` collection.

        ### Parameters
        ----
        row : dict
            A `Row` object with the properties
            set.
        """

        rows = self.table.get('rows', [])
        rows.append(row)

    def del_row(self, index: int = 0) -> None:
        """Deletes a `Row` in the `rows` collection.

        ### Parameters
        ----
        index : int (optional=, Default=0)
            The index of the `Row` object
            that you wish to delete.
        """

        rows = self.table.get('rows', [])
        rows.pop(index)

    def get_row(self, index: int = 0) -> dict:
        """Gets a `Row` in the `rows` collection by
        indexing it.

        ### Parameters
        ----
        index : int (optional=, Default=0)
            The index of the `Row` object
            that you wish to get.
        """

        return self.table.get('rows', [])[index]


class Dataset():

    """
    ### Overview
    ----
    Represents a `PowerBiDataset` object with
    different tables, relationships, and data
    sources.
    """

    def __init__(self, name: str, tables: Tables = []) -> None:
        """Initializes the `Dataset` object.

        ### Parameters
        ----
        name : str
            User defined name of the dataset.
            It is also used as the identifier
            of the dataset.

        tables : object
            A collection of `Table` objects
            you want to be part of the dataset.
        """

        if len(tables) == 0:
            self._tables = Tables()
        else:
            self._tables = tables

        self._relationships = Relationships()

        self.push_dataset = {
            'name': name,
            'tables': self._tables,
            'datasources': [],
            'defaultMode': '',
            'relationships': self._relationships
        }

    def __repr__(self) -> str:
        """Represents the string representation of the
        table object.

        ### Returns
        ----
        str
            A JSON formatted string.
        """

        return json.dumps(obj=self.push_dataset, indent=4, cls=PowerBiEncoder)

    @property
    def name(self) -> str:
        """The dataset name.

        ### Returns
        ----
        str : 
            The dataset name.
        """
        return self.push_dataset.get('name', None)

    @name.setter
    def name(self, name: str) -> None:
        """Sets the dataset name.

        ### Parameters
        ----
        name : str
            The name you want the dataset to be.
        """

        self.push_dataset.update({'name': name})

    @property
    def default_mode(self) -> str:
        """Gets the `defaultMode` property.

        ### Returns
        ----
        str : 
            The dataset mode or type.
        """
        return self.push_dataset.get('defaultMode', None)

    @default_mode.setter
    def default_mode(self, default_mode: str) -> None:
        """Sets the `defaultMode` property.

        ### Parameters
        ----
        default_mode : str
            The dataset mode or type.
        """

        self.push_dataset.update({'defaultMode': default_mode})

    @property
    def tables(self) -> Tables:
        """Returns the `Tables` collection from
        the dataset.

        ### Returns
        ----
        Tables
            [description]
        """
        return self._tables

    def add_table(self, table: Table) -> None:
        """Adds a new `Table` object to the `Tables`
        collection.

        ### Parameters
        ----
        table : Table
            A table object with the properties set.
        """

        self._tables[len(self._tables)] = table

    def del_table(self, index: int) -> None:
        """Deletes a `Table` to the `Tables`
        collection.

        ### Parameters
        ----
        index : int
            The index of the table you want
            to delete from the collection.
        """

        del self._tables[index]

    def get_table(self, index: int) -> Table:
        """Gets a `Table` to the `Tables`
        collection.

        ### Parameters
        ----
        index : int
            The index of the table you want
            to get from the collection.
        """

        return self._tables[index]

    @property
    def relationships(self) -> Relationship:
        pass

    def add_relationship(self) -> None:
        pass

    def del_relationship(self, index: int) -> None:
        pass

    def get_relationship(self, index: int) -> Relationship:
        pass

    @property
    def data_sources(self) -> object:
        pass

    def add_data_source(self) -> None:
        pass

    def del_data_source(self, index: int) -> None:
        pass

    def get_data_source(self, index: int) -> object:
        pass
