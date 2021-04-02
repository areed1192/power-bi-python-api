import json

from typing import Dict
from typing import Union
from powerbi.utils import Dataset
from powerbi.utils import Table
from powerbi.utils import PowerBiEncoder
from powerbi.session import PowerBiSession


class PushDatasets():

    def __init__(self, session: object) -> None:
        """Initializes the `PushDatasets` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def get_tables(self, dataset_id: str) -> Dict:
        """Returns a list of tables tables within the specified dataset from
        "My Workspace".

        ### Parameters
        ----
        dataset_id : str
            The dataset ID you want to query.

        ### Returns
        ----
        Dict
            A collection of `Tables` resources.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.get_tables(
                dataset_id='8c2765d5-96f7-4f79-a5b4-3a07e367ad8e'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/datasets/{dataset_id}/tables',
        )

        return content

    def get_group_tables(self, group_id: str, dataset_id: str) -> Dict:
        """Returns a list of tables tables within the specified dataset from
        the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dataset_id : str
            The dataset ID you want to query.

        ### Returns
        ----
        Dict
            A collection of `Tables` resources.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.get_group_tables(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dataset_id='8c2765d5-96f7-4f79-a5b4-3a07e367ad8e'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset_id}/tables',
        )

        return content

    def post_dataset(self, dataset: Union[dict, Dataset], default_retention_policy: str = None) -> Dict:
        """Creates a new dataset on "My Workspace".

        ### Parameters
        ----
        dataset : Union[dict, Dataset]
            The dataset you want to post.

        default_retention_policy : str (optional, Default=None)
            The default retention policy.

        ### Returns
        ----
        Dict
            A datset resource with the id.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_dataset(
                dataset={},
                default_retention_policy='basicFIFO'
            )
        """

        if isinstance(dataset, Dataset):

            dataset = json.dumps(
                obj=dataset._prep_for_post(),
                indent=4,
                cls=PowerBiEncoder
            )

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/datasets?defaultRetentionPolicy={default_retention_policy}',
            data=dataset
        )

        return content

    def post_group_dataset(self, group_id: str, dataset: Union[dict, Dataset], default_retention_policy: str = None) -> Dict:
        """Creates a new dataset in the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataset : Union[dict, Dataset]
            The dataset you want to post.

        default_retention_policy : str (optional, Default=None)
            The default retention policy.

        ### Returns
        ----
        Dict
            A datset resource with the id.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_group_dataset(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dataset={},
                default_retention_policy='basicFIFO'
            )
        """

        if isinstance(dataset, Dataset):

            dataset = json.dumps(
                obj=dataset._prep_for_post(),
                indent=4,
                cls=PowerBiEncoder
            )

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/datasets?defaultRetentionPolicy={default_retention_policy}',
            data=dataset
        )

        return content

    def post_dataset_rows(self, dataset_id: str, table_name: str, rows: list) -> None:
        """Adds new data rows to the specified table within the specified
        dataset from "My Workspace".

        ### Parameters
        ----
        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to post rows
            to.

        rows : list
            An array of data rows pushed to a dataset table.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_dataset_rows(
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table',
                rows=[
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
            )
        """

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/datasets/{dataset_id}/tables/{table_name}/rows',
            json_payload=rows
        )

        return content

    def post_group_dataset_rows(self, group_id: str, dataset_id: str, table_name: str, rows: list) -> None:
        """Adds new data rows to the specified table, within the specified dataset, 
        from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to post rows
            to.

        rows : list
            An array of data rows pushed to a dataset table.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_group_dataset_rows(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table',
                rows=[
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
            )
        """

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset_id}/tables/{table_name}/rows',
            json_payload=rows
        )

        return content

    def put_dataset(self, dataset_id: str, table_name: str, table: Union[Table, dict]) -> Dict:
        """Updates the metadata and schema for the specified table within the
        specified dataset from "My Workspace".

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        table_name : str
            The name of the table you want to update.

        table : Union[Table, dict]
            The table information you want updated, can
            be a `Table` object.

        ### Returns
        ----
        Dict
            A `Table` object.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.put_dataset(
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table',
                table=new_table_sales
            )
        """

        if isinstance(table, Table):

            del table['rows']

            table = json.dumps(
                obj=table,
                indent=4,
                cls=PowerBiEncoder
            )

        content = self.power_bi_session.make_request(
            method='put',
            endpoint=f'myorg/datasets/{dataset_id}/tables/{table_name}',
            data=table
        )

        return content

    def put_group_dataset(self, group_id: str, dataset_id: str, table_name: str, table: Union[Table, dict]) -> Dict:
        """Updates the metadata and schema for the specified table within the
        specified dataset from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataset_id : str
            The dataset ID.

        table_name : str
            The name of the table you want to update.

        table : Union[Table, dict]
            The table information you want updated, can
            be a `Table` object.

        ### Returns
        ----
        Dict
            A `Table` object.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.put_group_dataset(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table',
                table=new_table_sales
            )
        """

        if isinstance(table, Table):

            del table['rows']

            table = json.dumps(
                obj=table,
                indent=4,
                cls=PowerBiEncoder
            )

        content = self.power_bi_session.make_request(
            method='put',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset_id}/tables/{table_name}',
            data=table
        )

        return content

    def delete_dataset_rows(self, dataset_id: str, table_name: str) -> None:
        """Delets All rows from the specified table within the specified
        dataset from "My Workspace".

        ### Parameters
        ----
        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to post rows
            to.

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_dataset_rows(
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table'
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/datasets/{dataset_id}/tables/{table_name}/rows'
        )

        return content

    def delete_group_dataset_rows(self, group_id: str, dataset_id: str, table_name: str) -> None:
        """Deletes all the data rows from the specified table, within the specified dataset, 
        from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to post rows
            to..

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.post_group_dataset_rows(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table'
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset_id}/tables/{table_name}/rows'
        )

        return content
