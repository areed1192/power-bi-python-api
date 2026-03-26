"""Module for the Power BI `Datasets` service."""

from typing import Dict
from powerbi.session import PowerBiSession


class Datasets:
    """Class for the `Datasets` service."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Datasets` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def _build_endpoint(self, path: str, group_id: str = None) -> str:
        if group_id:
            return f"myorg/groups/{group_id}/{path}"
        return f"myorg/{path}"

    def get_datasets(self, group_id: str = None) -> Dict:
        """Returns a list of datasets.

        ### Parameters
        ----
        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Dataset` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_datasets()
            >>> datasets_service.get_datasets(group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48')
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint("datasets", group_id),
        )

        return content

    def update_refresh_schedule(
        self, dataset_id: str, refresh_schedule: dict, group_id: str = None
    ) -> None:
        """Updates the refresh schedule for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        refresh_schedule : dict
            The refresh schedule. Should contain a `value` key with
            the schedule configuration.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.update_refresh_schedule(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    refresh_schedule={'value': {'enabled': True}}
                )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            json_payload=refresh_schedule,
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshSchedule", group_id
            ),
        )

        return content

    def bind_to_gateway(
        self,
        dataset_id: str,
        gateway_object_id: str,
        datasource_object_ids: list = None,
        group_id: str = None,
    ) -> None:
        """Binds a dataset to a specified gateway.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset to bind.

        gateway_object_id : str
            The ID of the gateway to bind the dataset to. When using a gateway cluster,
            this refers to the primary gateway.

        datasource_object_ids : list, (optional, default=None)
            A list of unique identifiers for the data sources in the gateway.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.bind_to_gateway(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934'
                )
            >>> dataset_service.bind_to_gateway(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934',
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        payload = {"gatewayObjectId": gateway_object_id}

        if datasource_object_ids:
            payload["datasourceObjectIds"] = datasource_object_ids

        response = self.power_bi_session.make_request(
            method="post",
            json_payload=payload,
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.BindToGateway", group_id
            ),
        )

        return response

    def cancel_refresh(
        self, dataset_id: str, refresh_id: str, group_id: str = None
    ) -> None:
        """Cancels the specified refresh operation for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset.

        refresh_id : str
            The ID of the refresh operation to cancel.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.cancel_refresh(
                    dataset_id='f7fc6510-e151-42a3-850b-d0805a391db0',
                    refresh_id='87f31ef7-1e3a-4006-9b0b-191693e79e9e'
                )
            >>> dataset_service.cancel_refresh(
                    dataset_id='f7fc6510-e151-42a3-850b-d0805a391db0',
                    refresh_id='87f31ef7-1e3a-4006-9b0b-191693e79e9e',
                    group_id='fdb91b8f-0a9b-44c1-b6c0-0cb185c6ebfb'
                )
        """

        response = self.power_bi_session.make_request(
            method="delete",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshes/{refresh_id}", group_id
            ),
        )

        return response

    def delete_dataset(self, dataset_id: str, group_id: str = None) -> None:
        """Deletes the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The ID of the dataset to delete.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> dataset_service = power_bi_client.datasets()
            >>> dataset_service.delete_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
            >>> dataset_service.delete_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        response = self.power_bi_session.make_request(
            method="delete",
            endpoint=self._build_endpoint(f"datasets/{dataset_id}", group_id),
        )

        return response

    # ------------------------------------------------------------------
    # GET operations
    # ------------------------------------------------------------------

    def get_dataset(self, dataset_id: str, group_id: str = None) -> Dict:
        """Returns the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `Dataset` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"datasets/{dataset_id}", group_id),
        )

        return content

    def get_datasources(self, dataset_id: str, group_id: str = None) -> Dict:
        """Returns a list of data sources for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Datasource` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_datasources(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/datasources", group_id
            ),
        )

        return content

    def get_dataset_users(self, dataset_id: str, group_id: str = None) -> Dict:
        """Returns a list of principals that have access to the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `DatasetUserAccess` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_dataset_users(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/users", group_id
            ),
        )

        return content

    def get_dataset_to_dataflows_links_in_group(self, group_id: str) -> Dict:
        """Returns a list of upstream dataflows for datasets from the
        specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        ### Returns
        -------
        Dict
            A collection of dataset-to-dataflow link resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_dataset_to_dataflows_links_in_group(
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/groups/{group_id}/datasets/upstreamDataflows",
        )

        return content

    def get_gateway_datasources(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Returns a list of gateway data sources for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of gateway `Datasource` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_gateway_datasources(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.GetBoundGatewayDatasources",
                group_id,
            ),
        )

        return content

    def get_parameters(self, dataset_id: str, group_id: str = None) -> Dict:
        """Returns a list of parameters for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `MashupParameter` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_parameters(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/parameters", group_id
            ),
        )

        return content

    def get_refresh_history(
        self, dataset_id: str, top: int = None, group_id: str = None
    ) -> Dict:
        """Returns the refresh history for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        top : int (optional, Default=None)
            The requested number of entries in the refresh history.
            If not provided, the default is the last available 60 entries.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Refresh` history entries.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_refresh_history(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    top=5
                )
        """

        params = {}
        if top is not None:
            params["$top"] = top

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshes", group_id
            ),
            params=params if params else None,
        )

        return content

    def get_refresh_execution_details(
        self, dataset_id: str, refresh_id: str, group_id: str = None
    ) -> Dict:
        """Returns execution details of a refresh operation for the
        specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        refresh_id : str
            The refresh ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `DatasetRefreshDetail` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_refresh_execution_details(
                    dataset_id='f7fc6510-e151-42a3-850b-d0805a391db0',
                    refresh_id='87f31ef7-1e3a-4006-9b0b-191693e79e9e'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshes/{refresh_id}", group_id
            ),
        )

        return content

    def get_refresh_schedule(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Returns the refresh schedule for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `RefreshSchedule` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_refresh_schedule(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshSchedule", group_id
            ),
        )

        return content

    def get_direct_query_refresh_schedule(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Returns the refresh schedule for a specified DirectQuery or
        LiveConnection dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `DirectQueryRefreshSchedule` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_direct_query_refresh_schedule(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/directQueryRefreshSchedule", group_id
            ),
        )

        return content

    def get_query_scale_out_sync_status(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Returns the query scale-out sync status for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `DatasetQueryScaleOutSyncStatus` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.get_query_scale_out_sync_status(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/queryScaleOut/syncStatus", group_id
            ),
        )

        return content

    def discover_gateways(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Returns a list of gateways that the specified dataset can be
        bound to.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Gateway` resources.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.discover_gateways(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.DiscoverGateways", group_id
            ),
        )

        return content

    # ------------------------------------------------------------------
    # POST operations
    # ------------------------------------------------------------------

    def refresh_dataset(
        self,
        dataset_id: str,
        notify_option: str = None,
        refresh_type: str = None,
        commit_mode: str = None,
        objects: list = None,
        apply_refresh_policy: bool = None,
        effective_date: str = None,
        max_parallelism: int = None,
        retry_count: int = None,
        timeout: str = None,
        group_id: str = None,
    ) -> None:
        """Triggers a refresh for the specified dataset.

        For a basic refresh, provide `notify_option`. For an enhanced
        refresh, provide one or more of the other parameters and omit
        `notify_option`.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        notify_option : str (optional, Default=None)
            Mail notification option. Options: NoNotification,
            MailOnFailure, MailOnCompletion. Required for basic
            refresh on shared capacities.

        refresh_type : str (optional, Default=None)
            The type of processing: Full, ClearValues, Calculate,
            DataOnly, Automatic, Defragment.

        commit_mode : str (optional, Default=None)
            Transactional or PartialBatch.

        objects : list (optional, Default=None)
            An array of dicts with 'table' and optional 'partition'
            keys specifying objects to refresh.

        apply_refresh_policy : bool (optional, Default=None)
            Whether to apply the incremental refresh policy.

        effective_date : str (optional, Default=None)
            ISO 8601 datetime to override the current date for
            incremental refresh policy.

        max_parallelism : int (optional, Default=None)
            Maximum threads for parallel processing commands.

        retry_count : int (optional, Default=None)
            Number of retry attempts before failing.

        timeout : str (optional, Default=None)
            Timeout per refresh attempt in HH:MM:SS format.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> # Basic refresh
            >>> datasets_service.refresh_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    notify_option='MailOnFailure'
                )
            >>> # Enhanced refresh of specific objects
            >>> datasets_service.refresh_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    refresh_type='Full',
                    commit_mode='Transactional',
                    objects=[{'table': 'Customer', 'partition': 'Recent'}]
                )
        """

        body = {}

        field_map = {
            "notifyOption": notify_option,
            "type": refresh_type,
            "commitMode": commit_mode,
            "objects": objects,
            "applyRefreshPolicy": apply_refresh_policy,
            "effectiveDate": effective_date,
            "maxParallelism": max_parallelism,
            "retryCount": retry_count,
            "timeout": timeout,
        }

        for key, value in field_map.items():
            if value is not None:
                body[key] = value

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/refreshes", group_id
            ),
            json_payload=body if body else None,
        )

        return content

    def execute_queries(
        self,
        dataset_id: str,
        query: str,
        impersonated_user_name: str = None,
        include_nulls: bool = None,
        group_id: str = None,
    ) -> Dict:
        """Executes a DAX query against the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        query : str
            The DAX query to execute.

        impersonated_user_name : str (optional, Default=None)
            The UPN of a user to impersonate. Ignored if the model
            is not RLS enabled.

        include_nulls : bool (optional, Default=None)
            Whether null (blank) values should be included in the
            result set. Defaults to false if unspecified.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `DatasetExecuteQueriesResponse` with query results.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.execute_queries(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    query='EVALUATE VALUES(MyTable)'
                )
        """

        body = {"queries": [{"query": query}]}

        if impersonated_user_name:
            body["impersonatedUserName"] = impersonated_user_name

        if include_nulls is not None:
            body["serializerSettings"] = {"includeNulls": include_nulls}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/executeQueries", group_id
            ),
            json_payload=body,
        )

        return content

    def post_dataset_user(
        self,
        dataset_id: str,
        identifier: str,
        principal_type: str,
        access_right: str,
        group_id: str = None,
    ) -> None:
        """Grants the specified user's permissions to the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        identifier : str
            For principal type User, provide the UPN. Otherwise
            provide the object ID of the principal.

        principal_type : str
            The principal type: User, Group, App, or None.

        access_right : str
            The access right to grant: Read, ReadReshare,
            ReadExplore, or ReadReshareExplore.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.post_dataset_user(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    identifier='john@contoso.com',
                    principal_type='User',
                    access_right='Read'
                )
        """

        body = {
            "identifier": identifier,
            "principalType": principal_type,
            "datasetUserAccessRight": access_right,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/users", group_id
            ),
            json_payload=body,
        )

        return content

    def update_datasources(
        self, dataset_id: str, update_details: list, group_id: str = None
    ) -> None:
        """Updates the data sources of the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        update_details : list
            A list of data source connection update request dicts.
            Each dict should contain `connectionDetails` and optionally
            `datasourceSelector`. See the API docs for the full schema.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.update_datasources(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    update_details=[{
                        'datasourceSelector': {
                            'datasourceType': 'Sql',
                            'connectionDetails': {
                                'server': 'Old-Server',
                                'database': 'Old-DB'
                            }
                        },
                        'connectionDetails': {
                            'server': 'New-Server',
                            'database': 'New-DB'
                        }
                    }]
                )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.UpdateDatasources", group_id
            ),
            json_payload={"updateDetails": update_details},
        )

        return content

    def update_parameters(
        self, dataset_id: str, update_details: list, group_id: str = None
    ) -> None:
        """Updates the parameter values for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        update_details : list
            A list of dicts with 'name' and 'newValue' keys for each
            parameter to update.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.update_parameters(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    update_details=[
                        {'name': 'DatabaseName', 'newValue': 'NewDB'},
                        {'name': 'MaxId', 'newValue': '5678'}
                    ]
                )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.UpdateParameters", group_id
            ),
            json_payload={"updateDetails": update_details},
        )

        return content

    def set_all_dataset_connections(
        self, dataset_id: str, connection_string: str, group_id: str = None
    ) -> None:
        """Updates all connections for the specified dataset.

        .. deprecated::
            This API is deprecated. Use `update_parameters` for SQL,
            Azure Synapse, OData, and SharePoint data sources, or
            `update_datasources` for other data sources.

        Only supports SQL DirectQuery datasets.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        connection_string : str
            The dataset connection string.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.set_all_dataset_connections(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    connection_string='data source=server;initial catalog=db'
                )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/Default.SetAllConnections", group_id
            ),
            json_payload={"connectionString": connection_string},
        )

        return content

    def take_over_in_group(self, dataset_id: str, group_id: str) -> None:
        """Transfers ownership of the specified dataset to the current
        authorized user.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str
            The workspace id.

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.take_over_in_group(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    group_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=(
                f"myorg/groups/{group_id}/datasets/"
                f"{dataset_id}/Default.TakeOver"
            ),
        )

        return content

    def trigger_query_scale_out_sync(
        self, dataset_id: str, group_id: str = None
    ) -> Dict:
        """Triggers a query scale-out sync of read-only replicas for
        the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `DatasetQueryScaleOutSyncStatus` resource.

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.trigger_query_scale_out_sync(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
                )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/queryScaleOut/sync", group_id
            ),
        )

        return content

    # ------------------------------------------------------------------
    # PUT operations
    # ------------------------------------------------------------------

    def put_dataset_user(
        self,
        dataset_id: str,
        identifier: str,
        principal_type: str,
        access_right: str,
        group_id: str = None,
    ) -> None:
        """Updates the existing permissions of the specified user for the
        specified dataset. Can also remove all permissions by setting
        access_right to 'None'.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        identifier : str
            For principal type User, provide the UPN. Otherwise
            provide the object ID of the principal.

        principal_type : str
            The principal type: User, Group, App, or None.

        access_right : str
            The access right: None, Read, ReadWrite, ReadReshare,
            ReadWriteReshare, ReadExplore, ReadReshareExplore,
            ReadWriteExplore, or ReadWriteReshareExplore.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.put_dataset_user(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    identifier='john@contoso.com',
                    principal_type='User',
                    access_right='Read'
                )
        """

        body = {
            "identifier": identifier,
            "principalType": principal_type,
            "datasetUserAccessRight": access_right,
        }

        content = self.power_bi_session.make_request(
            method="put",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/users", group_id
            ),
            json_payload=body,
        )

        return content

    # ------------------------------------------------------------------
    # PATCH operations
    # ------------------------------------------------------------------

    def update_dataset(
        self, dataset_id: str, update_request: dict, group_id: str = None
    ) -> None:
        """Updates the properties for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        update_request : dict
            The update request body. Can contain `targetStorageMode`
            (str) and/or `queryScaleOutSettings` (dict with
            `autoSyncReadOnlyReplicas` and `maxReadOnlyReplicas`).

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.update_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    update_request={'targetStorageMode': 'PremiumFiles'}
                )
            >>> datasets_service.update_dataset(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    update_request={
                        'queryScaleOutSettings': {
                            'autoSyncReadOnlyReplicas': False,
                            'maxReadOnlyReplicas': -1
                        }
                    }
                )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=self._build_endpoint(f"datasets/{dataset_id}", group_id),
            json_payload=update_request,
        )

        return content

    def update_direct_query_refresh_schedule(
        self, dataset_id: str, refresh_schedule: dict, group_id: str = None
    ) -> None:
        """Updates the refresh schedule for a specified DirectQuery or
        LiveConnection dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        refresh_schedule : dict
            The refresh schedule configuration. Should contain a `value`
            key with the schedule details.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        None

        ### Usage
        ----
            >>> datasets_service = power_bi_client.datasets()
            >>> datasets_service.update_direct_query_refresh_schedule(
                    dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                    refresh_schedule={
                        'value': {'frequency': 15, 'enabled': True}
                    }
                )
        """

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=self._build_endpoint(
                f"datasets/{dataset_id}/directQueryRefreshSchedule",
                group_id,
            ),
            json_payload=refresh_schedule,
        )

        return content
