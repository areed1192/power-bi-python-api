"""Module for the `Dataflows` service."""

from enum import Enum

from powerbi.session import PowerBiSession


class Dataflows:
    """Class for the `Dataflows` service."""

    def __init__(self, session: object) -> None:
        """Initializes the `Dataflows` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> groups_service = power_bi_client.dataflow()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def get_dataflows(self, group_id: str) -> dict:
        """Returns a list of all dataflows from the
        specified workspace.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        ### Returns
        -------
        Dict
            A collection of `Dataflow` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflows(
                group_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/groups/{group_id}/dataflows"
        )

        return content

    def get_dataflow(self, group_id: str, dataflow_id: str) -> dict:
        """Exports the specified dataflow definition to a JSON file.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Returns
        -------
        Dict
            A collection of `Dataflow` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflow(
                group_id=''
                dataflow_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}"
        )

        return content

    def get_dataflow_transactions(self, group_id: str, dataflow_id: str) -> dict:
        """Returns a list of transactions for the specified dataflow.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Returns
        -------
        Dict
            A collection of `DataflowTransactions` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflow_transactions(
                group_id=''
                dataflow_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/transactions",
        )

        return content

    def get_dataflow_datasources(self, group_id: str, dataflow_id: str) -> dict:
        """Returns a list of data sources for the specified dataflow.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Returns
        -------
        Dict
            A collection of `Datasource` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflow_datasources(
                group_id=''
                dataflow_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/datasources",
        )

        return content

    def delete_dataflow(self, group_id: str, dataflow_id: str) -> None:
        """Deletes a dataflow from Power BI data prep storage, including
        its definition file and model.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.delete_dataflow(
                group_id=''
                dataflow_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="delete", endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}"
        )

        return content

    def update_refresh_schedule(
        self, group_id: str, dataflow_id: str, refresh_schedule: dict
    ) -> None:
        """Creates or updates the refresh schedule for a specified dataflow.

        ### Parameters
        ----
        group_id : str
            The group ID.

        dataflow_id : str
            The dataflow ID.

        refresh_schedule : dict
            The refresh schedule.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_dataflows(
                group_id='',
                dataflow_id='',
                refresh_schedule={}
            )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            json_payload=refresh_schedule,
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/refreshSchedule",
        )

        return content

    def get_upstream_dataflows_in_group(self, group_id: str, dataflow_id: str) -> dict:
        """Returns a list of upstream dataflows in the specified workspace.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Returns
        -------
        dict
            A collection of `DependentDataflows` resources.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.get_upstream_dataflows_in_group(
                group_id=''
                dataflow_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/upstreamDataflows",
        )

        return content

    def refresh_dataflow(
        self,
        group_id: str,
        dataflow_id: str,
        notify_option: str | Enum,
        process_type: str = None,
    ) -> None:
        """Triggers a refresh for the specified dataflow.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        notify_option : str | Enum
            Mail notification options.

        process_type : str
            Type of refresh process to use.

        ### Returns
        -------
        dict
            A `DataflowTransactionStatus` resource.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.refresh_dataflow(
                group_id=''
                dataflow_id='',
                notify_option='MailOnFailure'
            )
        """

        if process_type:
            params = {"processType": process_type}
        else:
            params = {}

        # Check if the notify option is an enum.
        if isinstance(notify_option, Enum):
            notify_option = notify_option.value

        body = {"notifyOption": notify_option}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}/refreshes",
            params=params,
            json_payload=body,
        )

        return content

    def cancel_dataflow_transaction(self, group_id: str, transaction_id: str) -> None:
        """Attempts to cancel the specified transactions.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        transaction_id : str
            The transaction ID.

        ### Returns
        -------
        dict
            A `DataflowTransactionStatus` resource.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.cancel_dataflow_transaction(
                group_id=''
                transaction_id=''
            )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/groups/{group_id}/dataflowTransactions/{transaction_id}/cancel",
        )

        return content

    def update_dataflow(
        self,
        group_id: str,
        dataflow_id: str,
        allow_native_queries: bool = None,
        compute_engine_behavior: str | Enum = None,
        description: str = None,
        name: str = None,
    ) -> None:
        """Updates dataflow properties, capabilities and settings.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dataflow_id : str
            The dataflow ID.

        allow_native_queries : bool
            Whether to allow native queries.

        compute_engine_behavior : str | Enum
            The behavior of the compute engine.

        description : str
            The new description for the dataflow.

        name : str
            The new name for the dataflow.

        ### Usage
        ----
            >>> dataflows_service = power_bi_client.dataflows()
            >>> dataflows_service.update_dataflow(
                group_id=''
                dataflow_id='',
                allow_native_queries=True,
                compute_engine_behavior='computeOptimized',
                description='',
                name=''
            )
        """

        if compute_engine_behavior and isinstance(compute_engine_behavior, Enum):
            compute_engine_behavior = compute_engine_behavior.value

        body = {
            "allowNativeQueries": allow_native_queries,
            "computeEngineBehavior": compute_engine_behavior,
            "description": description,
            "name": name,
        }

        content = self.power_bi_session.make_request(
            method="patch",
            json_payload=body,
            endpoint=f"myorg/groups/{group_id}/dataflows/{dataflow_id}",
        )

        return content
