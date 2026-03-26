"""Microsoft PowerBi `PushDatasets` Service."""

import json

from typing import Dict
from typing import Union
from powerbi.utils import Dataset
from powerbi.utils import Table
from powerbi.utils import PowerBiEncoder
from powerbi.session import PowerBiSession


class PushDatasets:

    """Microsoft PowerBi `PushDatasets` Service."""

    def __init__(self, session: PowerBiSession) -> None:
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

    def _build_endpoint(self, path: str, group_id: str = None) -> str:
        if group_id:
            return f"myorg/groups/{group_id}/{path}"
        return f"myorg/{path}"

    def get_tables(self, dataset_id: str, group_id: str = None) -> Dict:
        """Returns a list of tables within the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID you want to query.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> push_datasets_service.get_tables(
                dataset_id='8c2765d5-96f7-4f79-a5b4-3a07e367ad8e',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/tables", group_id
            ),
        )

        return content

    def post_dataset(
        self,
        dataset: Union[dict, Dataset],
        default_retention_policy: str = None,
        group_id: str = None,
    ) -> Dict:
        """Creates a new dataset.

        ### Parameters
        ----
        dataset : Union[dict, Dataset]
            The dataset you want to post.

        default_retention_policy : str (optional, Default=None)
            The default retention policy.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> push_datasets_service.post_dataset(
                dataset={},
                default_retention_policy='basicFIFO',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        if isinstance(dataset, Dataset):

            dataset = json.dumps(
                obj=dataset.prep_for_post(), indent=4, cls=PowerBiEncoder
            )

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets?defaultRetentionPolicy={default_retention_policy}",
                group_id,
            ),
            data=dataset,
        )

        return content

    def post_dataset_rows(
        self, dataset_id: str, table_name: str, rows: list, group_id: str = None
    ) -> None:
        """Adds new data rows to the specified table within the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to post rows to.

        rows : list
            An array of data rows pushed to a dataset table.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/tables/{table_name}/rows", group_id
            ),
            json_payload=rows,
        )

        return content

    def put_dataset(
        self,
        dataset_id: str,
        table_name: str,
        table: Union[Table, dict],
        group_id: str = None,
    ) -> Dict:
        """Updates the metadata and schema for the specified table within the
        specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        table_name : str
            The name of the table you want to update.

        table : Union[Table, dict]
            The table information you want updated, can
            be a `Table` object.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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

            del table["rows"]

            table = json.dumps(obj=table, indent=4, cls=PowerBiEncoder)

        content = self.power_bi_session.make_request(
            method="put",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/tables/{table_name}", group_id
            ),
            data=table,
        )

        return content

    def delete_dataset_rows(
        self, dataset_id: str, table_name: str, group_id: str = None
    ) -> None:
        """Deletes all rows from the specified table within the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset id

        table_name: str
            The dataset table name you want to delete rows from.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> push_datasets_service = power_bi_client.push_datasets()
            >>> push_datasets_service.delete_dataset_rows(
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table'
            )
            >>> push_datasets_service.delete_dataset_rows(
                dataset_id='8ea21119-fb8f-4592-b2b8-141b824a2b7e',
                table_name='sales_table',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/tables/{table_name}/rows", group_id
            ),
        )

        return content
