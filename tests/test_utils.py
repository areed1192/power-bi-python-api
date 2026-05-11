"""Tests for utility classes in powerbi/utils.py."""

import json
from enum import Enum

import pytest

from powerbi.utils import (
    enum_to_value,
    PowerBiEncoder,
    Column,
    Measure,
    Relationship,
    Columns,
    Measures,
    Relationships,
    Tables,
    DataSources,
    Table,
    Dataset,
    DataSource,
    CredentialDetails,
)


# ---------------------------------------------------------------------------
# enum_to_value
# ---------------------------------------------------------------------------

class _FakeEnum(Enum):
    FOO = "foo_val"


class TestEnumToValue:
    def test_converts_enum(self):
        assert enum_to_value(_FakeEnum.FOO) == "foo_val"

    def test_passes_through_string(self):
        assert enum_to_value("plain") == "plain"


# ---------------------------------------------------------------------------
# Column
# ---------------------------------------------------------------------------

class TestColumn:
    def test_init_with_string_type(self):
        col = Column(name="Sales", data_type="Int64")
        assert col.name == "Sales"
        assert col.data_type == "Int64"

    def test_init_with_enum_type(self):
        col = Column(name="Price", data_type=_FakeEnum.FOO)
        assert col.data_type == "foo_val"

    def test_default_properties(self):
        col = Column(name="X", data_type="String")
        assert col.is_hidden is False
        assert col.format_string == ""
        assert col.data_category == ""
        assert col.sort_by_column is None
        assert col.summarize_by is None

    def test_property_setters(self):
        col = Column(name="X", data_type="String")
        col.name = "Y"
        col.data_type = "Double"
        col.format_string = "#,##0"
        col.data_category = "City"
        col.is_hidden = True
        col.sort_by_column = "SortCol"
        col.summarize_by = "Sum"

        assert col.name == "Y"
        assert col.data_type == "Double"
        assert col.format_string == "#,##0"
        assert col.data_category == "City"
        assert col.is_hidden is True
        assert col.sort_by_column == "SortCol"
        assert col.summarize_by == "Sum"

    def test_summarize_by_enum(self):
        col = Column(name="X", data_type="Int64")
        col.summarize_by = _FakeEnum.FOO
        assert col.summarize_by == "foo_val"

    def test_to_dict(self):
        col = Column(name="ID", data_type="Int64")
        d = col.to_dict()
        assert d["name"] == "ID"
        assert d["dataType"] == "Int64"

    def test_to_json(self):
        col = Column(name="ID", data_type="Int64")
        parsed = json.loads(col.to_json())
        assert parsed["name"] == "ID"


# ---------------------------------------------------------------------------
# Measure
# ---------------------------------------------------------------------------

class TestMeasure:
    def test_init(self):
        m = Measure(name="Total", expression="SUM(Sales[Amount])")
        assert m.name == "Total"
        assert m.expression == "SUM(Sales[Amount])"

    def test_default_properties(self):
        m = Measure(name="M", expression="1")
        assert m.format_string == ""
        assert m.is_hidden is False

    def test_property_setters(self):
        m = Measure(name="M", expression="1")
        m.name = "M2"
        m.expression = "2+2"
        m.format_string = "#,##0"
        m.is_hidden = True

        assert m.name == "M2"
        assert m.expression == "2+2"
        assert m.format_string == "#,##0"
        assert m.is_hidden is True

    def test_to_dict(self):
        m = Measure(name="M", expression="1")
        d = m.to_dict()
        assert d["name"] == "M"
        assert d["expression"] == "1"

    def test_to_json(self):
        m = Measure(name="M", expression="1")
        parsed = json.loads(m.to_json())
        assert parsed["name"] == "M"


# ---------------------------------------------------------------------------
# Relationship
# ---------------------------------------------------------------------------

class TestRelationship:
    def test_init(self):
        r = Relationship(
            name="R1",
            from_table="Orders",
            to_table="Products",
            from_column="ProductID",
            to_column="ID",
        )
        assert r.name == "R1"
        assert r.from_table == "Orders"
        assert r.to_table == "Products"
        assert r.from_column == "ProductID"
        assert r.to_column == "ID"
        assert r.cross_filtering_behavior == "OneDirection"

    def test_property_setters(self):
        r = Relationship("R", "A", "B", "C", "D")
        r.name = "R2"
        r.from_table = "T1"
        r.to_table = "T2"
        r.from_column = "C1"
        r.to_column = "C2"
        r.cross_filtering_behavior = "BothDirections"

        assert r.name == "R2"
        assert r.from_table == "T1"
        assert r.to_table == "T2"
        assert r.from_column == "C1"
        assert r.to_column == "C2"
        assert r.cross_filtering_behavior == "BothDirections"

    def test_to_dict(self):
        r = Relationship("R", "A", "B", "C", "D")
        d = r.to_dict()
        assert d["name"] == "R"
        assert d["fromTable"] == "A"


# ---------------------------------------------------------------------------
# Collection classes
# ---------------------------------------------------------------------------

class TestColumns:
    def test_append_and_len(self):
        cols = Columns()
        cols[0] = Column("A", "String")
        cols[1] = Column("B", "Int64")
        assert len(cols) == 2

    def test_getitem(self):
        cols = Columns()
        col = Column("A", "String")
        cols[0] = col
        assert cols[0] is col

    def test_delitem(self):
        cols = Columns()
        cols[0] = Column("A", "String")
        del cols[0]
        assert len(cols) == 0

    def test_iter(self):
        cols = Columns()
        cols[0] = Column("A", "String")
        cols[1] = Column("B", "Int64")
        names = [c.name for c in cols]
        assert names == ["A", "B"]


class TestMeasures:
    def test_append_and_len(self):
        ms = Measures()
        ms[0] = Measure("M1", "1")
        assert len(ms) == 1

    def test_iter(self):
        ms = Measures()
        ms[0] = Measure("M1", "1")
        ms[1] = Measure("M2", "2")
        names = [m.name for m in ms]
        assert names == ["M1", "M2"]


class TestRelationships:
    def test_append_and_len(self):
        rs = Relationships()
        rs[0] = Relationship("R1", "A", "B", "C", "D")
        assert len(rs) == 1

    def test_delitem(self):
        rs = Relationships()
        rs[0] = Relationship("R1", "A", "B", "C", "D")
        del rs[0]
        assert len(rs) == 0


class TestTables:
    def test_append_and_len(self):
        ts = Tables()
        ts[0] = Table("T1")
        assert len(ts) == 1


class TestDataSources:
    def test_append_and_len(self):
        ds = DataSources()
        ds[0] = DataSource("Sql")
        assert len(ds) == 1


# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------

class TestTable:
    def test_init(self):
        t = Table(name="Sales")
        assert t.name == "Sales"
        assert len(t.columns) == 0
        assert len(t.rows) == 0

    def test_name_setter(self):
        t = Table("A")
        t.name = "B"
        assert t.name == "B"

    def test_add_and_get_column(self):
        t = Table("T")
        col = Column("C1", "String")
        t.add_column(col)
        assert t.get_column(0) is col
        assert len(t.columns) == 1

    def test_del_column(self):
        t = Table("T")
        t.add_column(Column("C1", "String"))
        t.del_column(0)
        assert len(t.columns) == 0

    def test_add_and_get_measure(self):
        t = Table("T")
        m = Measure("M1", "1")
        t.add_measure(m)
        assert t.get_measure(0) is m

    def test_add_row_dict(self):
        t = Table("T")
        t.add_row({"col1": "val1"})
        assert t.rows == [{"col1": "val1"}]

    def test_add_row_list(self):
        t = Table("T")
        t.add_row([{"a": 1}, {"a": 2}])
        assert len(t.rows) == 2

    def test_del_row(self):
        t = Table("T")
        t.add_row({"a": 1})
        t.add_row({"a": 2})
        t.del_row(0)
        assert len(t.rows) == 1

    def test_get_row(self):
        t = Table("T")
        t.add_row({"a": 1})
        assert t.get_row(0) == {"a": 1}

    def test_to_dict(self):
        t = Table("T")
        t.add_column(Column("C1", "String"))
        d = t.to_dict()
        assert d["name"] == "T"
        assert len(d["columns"]) == 1

    def test_to_json(self):
        t = Table("T")
        parsed = json.loads(t.to_json())
        assert parsed["name"] == "T"

    def test_repr(self):
        t = Table("T")
        r = repr(t)
        assert "T" in r


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class TestDataset:
    def _make_table(self):
        t = Table("Sales")
        t.add_column(Column("ID", "Int64"))
        t.add_row({"ID": 1})
        return t

    def test_init_with_empty_tables(self):
        tables = Tables()
        ds = Dataset(name="DS", tables=tables)
        assert ds.name == "DS"
        assert len(ds.tables) == 0

    def test_init_with_populated_tables(self):
        tables = Tables()
        tables[0] = self._make_table()
        ds = Dataset(name="DS", tables=tables)
        assert len(ds.tables) == 1

    def test_name_setter(self):
        ds = Dataset("A", Tables())
        ds.name = "B"
        assert ds.name == "B"

    def test_default_mode(self):
        ds = Dataset("DS", Tables())
        ds.default_mode = "Push"
        assert ds.default_mode == "Push"

    def test_add_and_get_table(self):
        ds = Dataset("DS", Tables())
        t = self._make_table()
        ds.add_table(t)
        assert ds.get_table(0) is t

    def test_del_table(self):
        ds = Dataset("DS", Tables())
        ds.add_table(self._make_table())
        ds.del_table(0)
        assert len(ds.tables) == 0

    def test_add_and_get_relationship(self):
        ds = Dataset("DS", Tables())
        r = Relationship("R", "A", "B", "C", "D")
        ds.add_relationship(r)
        assert ds.get_relationship(0) is r

    def test_del_relationship(self):
        ds = Dataset("DS", Tables())
        ds.add_relationship(Relationship("R", "A", "B", "C", "D"))
        ds.del_relationship(0)
        assert len(ds.relationships) == 0

    def test_add_data_source(self):
        ds = Dataset("DS", Tables())
        src = DataSource("Sql")
        ds.add_data_source(src)
        assert ds.get_data_source(0) is src

    def test_prep_for_post_removes_datasources_and_rows(self):
        tables = Tables()
        t = self._make_table()
        tables[0] = t
        ds = Dataset("DS", tables)
        ds.add_data_source(DataSource("Sql"))

        prepped = ds.prep_for_post()
        assert "datasources" not in prepped
        for tbl in prepped["tables"]:
            assert "rows" not in tbl

    def test_to_dict(self):
        ds = Dataset("DS", Tables())
        d = ds.to_dict()
        assert d["name"] == "DS"

    def test_to_json(self):
        ds = Dataset("DS", Tables())
        parsed = json.loads(ds.to_json())
        assert parsed["name"] == "DS"

    def test_repr(self):
        ds = Dataset("DS", Tables())
        assert "DS" in repr(ds)


# ---------------------------------------------------------------------------
# DataSource
# ---------------------------------------------------------------------------

class TestDataSource:
    def test_init_string(self):
        ds = DataSource("Sql")
        assert ds.data_source_type == "Sql"

    def test_init_enum(self):
        ds = DataSource(_FakeEnum.FOO)
        assert ds.data_source_type == "foo_val"

    def test_property_setters(self):
        ds = DataSource("Sql")
        ds.data_source_type = "OData"
        ds.connection_details = {"url": "https://example.com"}
        assert ds.data_source_type == "OData"
        assert ds.connection_details == {"url": "https://example.com"}

    def test_to_dict(self):
        ds = DataSource("Sql")
        d = ds.to_dict()
        assert d["datasourceType"] == "Sql"

    def test_to_json(self):
        ds = DataSource("Sql")
        parsed = json.loads(ds.to_json())
        assert parsed["datasourceType"] == "Sql"


# ---------------------------------------------------------------------------
# CredentialDetails
# ---------------------------------------------------------------------------

class TestCredentialDetails:
    def _make(self):
        return CredentialDetails(
            credential_type="Basic",
            credentials='{"credentialData":[]}',
            encrypted_connection="Encrypted",
            encryption_algorithm="None",
            privacy_level="None",
            use_caller_aad_identity=False,
            use_end_user_oauth2_credentials=False,
        )

    def test_init(self):
        cd = self._make()
        assert cd.credential_type == "Basic"
        assert cd.credentials == '{"credentialData":[]}'

    def test_to_dict(self):
        cd = self._make()
        d = cd.to_dict()
        assert d["credentialType"] == "Basic"
        assert d["encryptedConnection"] == "Encrypted"
        assert d["useCallerAADIdentity"] is False

    def test_to_json(self):
        cd = self._make()
        parsed = json.loads(cd.to_json())
        assert parsed["credentialType"] == "Basic"

    def test_enum_conversion_in_init(self):
        cd = CredentialDetails(
            credential_type=_FakeEnum.FOO,
            credentials="creds",
            encrypted_connection=_FakeEnum.FOO,
            encryption_algorithm=_FakeEnum.FOO,
            privacy_level=_FakeEnum.FOO,
            use_caller_aad_identity=False,
            use_end_user_oauth2_credentials=False,
        )
        d = cd.to_dict()
        assert d["credentialType"] == "foo_val"
        assert d["encryptedConnection"] == "foo_val"


# ---------------------------------------------------------------------------
# PowerBiEncoder
# ---------------------------------------------------------------------------

class TestPowerBiEncoder:
    def test_encodes_column(self):
        col = Column("C", "String")
        result = json.loads(json.dumps(col, cls=PowerBiEncoder))
        assert result["name"] == "C"

    def test_encodes_measure(self):
        m = Measure("M", "1")
        result = json.loads(json.dumps(m, cls=PowerBiEncoder))
        assert result["name"] == "M"

    def test_encodes_table(self):
        t = Table("T")
        t.add_column(Column("C", "String"))
        result = json.loads(json.dumps(t, cls=PowerBiEncoder))
        assert result["name"] == "T"

    def test_encodes_dataset(self):
        ds = Dataset("DS", Tables())
        result = json.loads(json.dumps(ds, cls=PowerBiEncoder))
        assert result["name"] == "DS"

    def test_encodes_relationship(self):
        r = Relationship("R", "A", "B", "C", "D")
        result = json.loads(json.dumps(r, cls=PowerBiEncoder))
        assert result["name"] == "R"

    def test_encodes_columns_collection(self):
        cols = Columns()
        cols[0] = Column("C1", "String")
        result = json.loads(json.dumps(cols, cls=PowerBiEncoder))
        assert len(result) == 1

    def test_encodes_datasource(self):
        ds = DataSource("Sql")
        result = json.loads(json.dumps(ds, cls=PowerBiEncoder))
        assert result["datasourceType"] == "Sql"

    def test_encodes_datasources_collection(self):
        dss = DataSources()
        dss[0] = DataSource("Sql")
        result = json.loads(json.dumps(dss, cls=PowerBiEncoder))
        assert len(result) == 1
