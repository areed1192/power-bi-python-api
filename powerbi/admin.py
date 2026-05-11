"""Module for the Power BI `Admin` service."""

from __future__ import annotations

from powerbi.session import PowerBiSession


class Admin:
    """Class for the `Admin` service."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Admin` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> admin_service = power_bi_client.admin()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    # ------------------------------------------------------------------ #
    #                         Activity Events                             #
    # ------------------------------------------------------------------ #

    def get_activity_events(
        self,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        continuation_token: str | None = None,
        filter_by: str | None = None,
    ) -> dict:
        """Returns a list of audit activity events for a tenant.

        Provide either a continuation token or both a start and end date
        time. ``start_date_time`` and ``end_date_time`` must be in the same
        UTC day, within the last 28 days, and should be wrapped in single
        quotes.

        ### Parameters
        ----
        start_date_time : str (optional)
            Start date and time in ISO 8601 compliant UTC format.

        end_date_time : str (optional)
            End date and time in ISO 8601 compliant UTC format.

        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        filter_by : str (optional)
            Filters the results based on a boolean condition, using
            'Activity', 'UserId', or both. Supports only 'eq' and 'and'.

        ### Returns
        ----
        dict
            A collection of ``ActivityEventResponse`` resources.

        ### Usage
        ----
            >>> admin_service = power_bi_client.admin()
            >>> admin_service.get_activity_events(
                    start_date_time="'2024-01-01T00:00:00.000Z'",
                    end_date_time="'2024-01-01T23:59:59.000Z'"
                )
        """

        params = {
            "startDateTime": start_date_time,
            "endDateTime": end_date_time,
            "continuationToken": continuation_token,
            "$filter": filter_by,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/activityevents",
            params=params,
        )

        return content

    # ------------------------------------------------------------------ #
    #                       Encryption Keys                               #
    # ------------------------------------------------------------------ #

    def add_encryption_key(
        self,
        name: str,
        key_vault_key_identifier: str,
        activate: bool = False,
        is_default: bool = False,
    ) -> dict:
        """Adds an encryption key for Power BI workspaces assigned to a capacity.

        ### Parameters
        ----
        name : str
            The name of the encryption key.

        key_vault_key_identifier : str
            The URI that uniquely specifies an encryption key in Azure Key Vault.

        activate : bool (optional, Default=False)
            Whether to activate any inactivated capacities and use this key.

        is_default : bool (optional, Default=False)
            Whether the key is the default key for the entire tenant.

        ### Returns
        ----
        dict
            A ``TenantKey`` resource.
        """

        body = {
            "name": name,
            "keyVaultKeyIdentifier": key_vault_key_identifier,
            "activate": activate,
            "isDefault": is_default,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/tenantKeys",
            json_payload=body,
        )

        return content

    def get_encryption_keys(self) -> dict:
        """Returns the encryption keys for the tenant.

        ### Returns
        ----
        dict
            A collection of ``TenantKey`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/tenantKeys",
        )

        return content

    def rotate_encryption_key(
        self,
        tenant_key_id: str,
        key_vault_key_identifier: str,
    ) -> dict:
        """Rotates the encryption key for Power BI workspaces assigned to a capacity.

        ### Parameters
        ----
        tenant_key_id : str
            The tenant key ID.

        key_vault_key_identifier : str
            The URI that uniquely specifies the encryption key in Azure Key Vault.

        ### Returns
        ----
        dict
            A ``TenantKey`` resource.
        """

        body = {"keyVaultKeyIdentifier": key_vault_key_identifier}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/admin/tenantKeys/{tenant_key_id}/Default.Rotate",
            json_payload=body,
        )

        return content

    # ------------------------------------------------------------------ #
    #                          Capacities                                 #
    # ------------------------------------------------------------------ #

    def get_capacities(self, expand: str | None = None) -> dict:
        """Returns a list of capacities for the organization.

        ### Parameters
        ----
        expand : str (optional)
            Expands related entities inline. Supports ``tenantKey``.

        ### Returns
        ----
        dict
            A collection of ``Capacity`` resources.
        """

        params = {"$expand": expand}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/capacities",
            params=params,
        )

        return content

    def patch_capacity(self, capacity_id: str, tenant_key_id: str) -> dict:
        """Changes specific capacity information. Currently only supports
        changing the capacity's encryption key.

        ### Parameters
        ----
        capacity_id : str
            The capacity ID.

        tenant_key_id : str
            The ID of the encryption key.

        ### Returns
        ----
        dict
            Response from the API.
        """

        body = {"tenantKeyId": tenant_key_id}

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=f"myorg/admin/capacities/{capacity_id}",
            json_payload=body,
        )

        return content

    def get_capacity_users(self, capacity_id: str) -> dict:
        """Returns a list of users that have access to the specified capacity.

        ### Parameters
        ----
        capacity_id : str
            The capacity ID.

        ### Returns
        ----
        dict
            A collection of ``CapacityUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/capacities/{capacity_id}/users",
        )

        return content

    def assign_workspaces_to_capacity(
        self, capacity_migration_assignments: list[dict]
    ) -> dict:
        """Assigns the specified workspaces to the specified Premium capacity.

        ### Parameters
        ----
        capacity_migration_assignments : list[dict]
            A list of assignment contracts. Each dict should contain
            ``targetCapacityObjectId`` (str) and ``workspacesToAssign``
            (list[str]).

        ### Returns
        ----
        dict
            Response from the API.
        """

        body = {
            "capacityMigrationAssignments": capacity_migration_assignments,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/capacities/AssignWorkspaces",
            json_payload=body,
        )

        return content

    def unassign_workspaces_from_capacity(
        self, workspaces_to_unassign: list[str]
    ) -> dict:
        """Unassigns the specified workspaces from capacity.

        ### Parameters
        ----
        workspaces_to_unassign : list[str]
            The workspace IDs to migrate to shared capacity.

        ### Returns
        ----
        dict
            Response from the API.
        """

        body = {"workspacesToUnassign": workspaces_to_unassign}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/capacities/UnassignWorkspaces",
            json_payload=body,
        )

        return content

    # ------------------------------------------------------------------ #
    #                         Refreshables                                #
    # ------------------------------------------------------------------ #

    def get_refreshables(
        self,
        top: int,
        expand: str | None = None,
        filter_by: str | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of refreshables for the organization within a capacity.

        Power BI retains a seven-day refresh history for each dataset, up to
        a maximum of sixty refreshes.

        ### Parameters
        ----
        top : int
            Returns only the first n results. Required.

        expand : str (optional)
            Accepts a comma-separated list of data types, which will be
            expanded inline in the response. Supports ``capacity``
            and ``group``.

        filter_by : str (optional)
            Returns a subset of results based on an OData filter query
            parameter condition.

        skip : int (optional)
            Skips the first n results. Use with top to fetch results
            beyond the first 1000.

        ### Returns
        ----
        dict
            A collection of ``Refreshable`` resources.

        ### Usage
        ----
            >>> admin_service = power_bi_client.admin()
            >>> admin_service.get_refreshables(top=20)
        """

        params = {
            "$top": top,
            "$expand": expand,
            "$filter": filter_by,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/capacities/refreshables",
            params=params,
        )

        return content

    def get_refreshables_for_capacity(
        self,
        capacity_id: str,
        top: int,
        expand: str | None = None,
        filter_by: str | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of refreshables for the specified capacity.

        ### Parameters
        ----
        capacity_id : str
            The capacity ID.

        top : int
            Returns only the first n results. Required.

        expand : str (optional)
            Accepts a comma-separated list of data types.

        filter_by : str (optional)
            OData filter query parameter condition.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``Refreshable`` resources.
        """

        params = {
            "$top": top,
            "$expand": expand,
            "$filter": filter_by,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/capacities/{capacity_id}/refreshables",
            params=params,
        )

        return content

    def get_refreshable_for_capacity(
        self,
        capacity_id: str,
        refreshable_id: str,
        expand: str | None = None,
    ) -> dict:
        """Returns the specified refreshable for the specified capacity.

        ### Parameters
        ----
        capacity_id : str
            The capacity ID.

        refreshable_id : str
            The refreshable ID.

        expand : str (optional)
            Expands related entities inline.

        ### Returns
        ----
        dict
            A ``Refreshable`` resource.
        """

        params = {"$expand": expand}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/capacities/{capacity_id}/refreshables/{refreshable_id}",
            params=params,
        )

        return content

    # ------------------------------------------------------------------ #
    #                             Apps                                    #
    # ------------------------------------------------------------------ #

    def get_apps(self, top: int, skip: int | None = None) -> dict:
        """Returns a list of apps in the organization.

        ### Parameters
        ----
        top : int
            The requested number of apps. Required.

        skip : int (optional)
            The number of entries to skip.

        ### Returns
        ----
        dict
            A collection of ``AdminApp`` resources.
        """

        params = {"$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/apps",
            params=params,
        )

        return content

    def get_app_users(self, app_id: str) -> dict:
        """Returns a list of users that have access to the specified app.

        ### Parameters
        ----
        app_id : str
            The app ID.

        ### Returns
        ----
        dict
            A collection of ``AppUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/apps/{app_id}/users",
        )

        return content

    # ------------------------------------------------------------------ #
    #                          Dashboards                                 #
    # ------------------------------------------------------------------ #

    def get_dashboards(
        self,
        expand: str | None = None,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of dashboards for the organization.

        ### Parameters
        ----
        expand : str (optional)
            Accepts a comma-separated list of data types. Supports ``tiles``.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDashboard`` resources.
        """

        params = {
            "$expand": expand,
            "$filter": filter_by,
            "$top": top,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/dashboards",
            params=params,
        )

        return content

    def get_dashboards_in_group(
        self,
        group_id: str,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of dashboards from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDashboard`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/dashboards",
            params=params,
        )

        return content

    def get_dashboard_subscriptions(self, dashboard_id: str) -> dict:
        """Returns a list of dashboard subscriptions along with subscriber
        details. This is a preview API call.

        ### Parameters
        ----
        dashboard_id : str
            The dashboard ID.

        ### Returns
        ----
        dict
            A collection of ``Subscription`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dashboards/{dashboard_id}/subscriptions",
        )

        return content

    def get_dashboard_users(self, dashboard_id: str) -> dict:
        """Returns a list of users that have access to the specified dashboard.

        ### Parameters
        ----
        dashboard_id : str
            The dashboard ID.

        ### Returns
        ----
        dict
            A collection of ``DashboardUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dashboards/{dashboard_id}/users",
        )

        return content

    def get_tiles(self, dashboard_id: str) -> dict:
        """Returns a list of tiles within the specified dashboard.

        ### Parameters
        ----
        dashboard_id : str
            The dashboard ID.

        ### Returns
        ----
        dict
            A collection of ``AdminTile`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dashboards/{dashboard_id}/tiles",
        )

        return content

    # ------------------------------------------------------------------ #
    #                           Dataflows                                 #
    # ------------------------------------------------------------------ #

    def get_dataflows(
        self,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of dataflows for the organization.

        ### Parameters
        ----
        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDataflow`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/dataflows",
            params=params,
        )

        return content

    def get_dataflows_in_group(
        self,
        group_id: str,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of dataflows from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDataflow`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/dataflows",
            params=params,
        )

        return content

    def export_dataflow(self, dataflow_id: str) -> dict:
        """Exports the definition for the specified dataflow to a JSON file.

        ### Parameters
        ----
        dataflow_id : str
            The dataflow ID.

        ### Returns
        ----
        dict
            The dataflow definition (model.json).
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dataflows/{dataflow_id}/export",
        )

        return content

    def get_dataflow_datasources(self, dataflow_id: str) -> dict:
        """Returns a list of data sources for the specified dataflow.

        ### Parameters
        ----
        dataflow_id : str
            The dataflow ID.

        ### Returns
        ----
        dict
            A collection of ``Datasource`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dataflows/{dataflow_id}/datasources",
        )

        return content

    def get_dataflow_users(self, dataflow_id: str) -> dict:
        """Returns a list of users that have access to the specified dataflow.

        ### Parameters
        ----
        dataflow_id : str
            The dataflow ID.

        ### Returns
        ----
        dict
            A collection of ``DataflowUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/dataflows/{dataflow_id}/users",
        )

        return content

    def get_upstream_dataflows_in_group(
        self, group_id: str, dataflow_id: str
    ) -> dict:
        """Returns a list of upstream dataflows for the specified dataflow.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataflow_id : str
            The dataflow ID.

        ### Returns
        ----
        dict
            A collection of ``DependentDataflow`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/dataflows/{dataflow_id}/upstreamDataflows",
        )

        return content

    # ------------------------------------------------------------------ #
    #                           Datasets                                  #
    # ------------------------------------------------------------------ #

    def get_datasets(
        self,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of datasets for the organization.

        ### Parameters
        ----
        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDataset`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/datasets",
            params=params,
        )

        return content

    def get_datasets_in_group(
        self,
        group_id: str,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of datasets from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminDataset`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/datasets",
            params=params,
        )

        return content

    def get_dataset_to_dataflows_links_in_group(self, group_id: str) -> dict:
        """Returns a list of upstream dataflows for datasets from the
        specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        ### Returns
        ----
        dict
            A collection of upstream dataflow links.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/datasets/upstreamDataflows",
        )

        return content

    def get_dataset_users(self, dataset_id: str) -> dict:
        """Returns a list of users that have access to the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        ### Returns
        ----
        dict
            A collection of ``DatasetUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/datasets/{dataset_id}/users",
        )

        return content

    def get_datasources(self, dataset_id: str) -> dict:
        """Returns a list of data sources for the specified dataset.

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        ### Returns
        ----
        dict
            A collection of ``Datasource`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/datasets/{dataset_id}/datasources",
        )

        return content

    # ------------------------------------------------------------------ #
    #                            Groups                                   #
    # ------------------------------------------------------------------ #

    def get_groups(
        self,
        top: int,
        expand: str | None = None,
        filter_by: str | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of workspaces for the organization.

        ### Parameters
        ----
        top : int
            Returns only the first n results (1-5000). Required.

        expand : str (optional)
            Accepts a comma-separated list of data types. Supports
            ``users``, ``reports``, ``dashboards``, ``datasets``,
            ``dataflows``, and ``workbooks``.

        filter_by : str (optional)
            OData filter query parameter condition.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminGroup`` resources.
        """

        params = {
            "$top": top,
            "$expand": expand,
            "$filter": filter_by,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/groups",
            params=params,
        )

        return content

    def get_group(
        self, group_id: str, expand: str | None = None
    ) -> dict:
        """Returns a workspace for the organization.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        expand : str (optional)
            Expands related entities inline.

        ### Returns
        ----
        dict
            An ``AdminGroup`` resource.
        """

        params = {"$expand": expand}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}",
            params=params,
        )

        return content

    def get_group_users(self, group_id: str) -> dict:
        """Returns a list of users that have access to the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        ### Returns
        ----
        dict
            A collection of ``GroupUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/users",
        )

        return content

    def get_unused_artifacts(
        self,
        group_id: str,
        continuation_token: str | None = None,
    ) -> dict:
        """Returns a list of datasets, reports, and dashboards that have not
        been used within 30 days for the specified workspace. Preview API.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        ### Returns
        ----
        dict
            A collection of unused artifact resources.
        """

        params = {"continuationToken": continuation_token}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/unusedArtifacts",
            params=params,
        )

        return content

    def add_group_user(self, group_id: str, user_details: dict) -> dict:
        """Grants user permissions to the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        user_details : dict
            A dict containing user details. Must include
            ``groupUserAccessRight``, ``identifier``, and ``principalType``.

        ### Returns
        ----
        dict
            Response from the API.
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/admin/groups/{group_id}/users",
            json_payload=user_details,
        )

        return content

    def delete_group_user(
        self,
        group_id: str,
        user: str,
        profile_id: str | None = None,
        is_group: bool | None = None,
    ) -> dict:
        """Removes user permissions from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        user : str
            The user principal name (UPN) or group/app object ID.

        profile_id : str (optional)
            The service principal profile ID to delete.

        is_group : bool (optional)
            Whether the given user is a group. Required when user is a group.

        ### Returns
        ----
        dict
            Response from the API.
        """

        params = {"profileId": profile_id, "isGroup": is_group}

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/admin/groups/{group_id}/users/{user}",
            params=params,
        )

        return content

    def restore_deleted_group(
        self,
        group_id: str,
        email_address: str,
        name: str | None = None,
    ) -> dict:
        """Restores a deleted workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        email_address : str
            The email address of the owner of the group to be restored.

        name : str (optional)
            The name of the group to be restored.

        ### Returns
        ----
        dict
            Response from the API.
        """

        body = {"emailAddress": email_address, "name": name}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/admin/groups/{group_id}/restore",
            json_payload=body,
        )

        return content

    def update_group(self, group_id: str, group_properties: dict) -> dict:
        """Updates the properties of the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        group_properties : dict
            A dict of properties to update. May include ``name``,
            ``description``, ``defaultDatasetStorageFormat``,
            ``logAnalyticsWorkspace``, etc.

        ### Returns
        ----
        dict
            Response from the API.
        """

        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=f"myorg/admin/groups/{group_id}",
            json_payload=group_properties,
        )

        return content

    # ------------------------------------------------------------------ #
    #                           Imports                                   #
    # ------------------------------------------------------------------ #

    def get_imports(
        self,
        expand: str | None = None,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of imports for the organization.

        ### Parameters
        ----
        expand : str (optional)
            Expands related entities inline.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``Import`` resources.
        """

        params = {
            "$expand": expand,
            "$filter": filter_by,
            "$top": top,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/imports",
            params=params,
        )

        return content

    # ------------------------------------------------------------------ #
    #                     Information Protection                          #
    # ------------------------------------------------------------------ #

    def set_labels(self, label_details: dict) -> dict:
        """Sets sensitivity labels on Power BI items by item ID.

        ### Parameters
        ----
        label_details : dict
            A dict containing ``labelId`` (str), ``artifacts`` (dict with
            lists of dashboard/report/dataset/dataflow IDs), and optionally
            ``assignmentMethod`` and ``delegatedUser``.

        ### Returns
        ----
        dict
            An ``InformationProtectionChangeLabelResponse`` resource.
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/informationprotection/setLabels",
            json_payload=label_details,
        )

        return content

    def remove_labels(self, artifacts: dict) -> dict:
        """Removes sensitivity labels from Power BI items by item ID.

        ### Parameters
        ----
        artifacts : dict
            A dict with lists of item IDs keyed by type (``dashboards``,
            ``reports``, ``datasets``, ``dataflows``). Each entry is a
            list of dicts with an ``id`` key.

        ### Returns
        ----
        dict
            An ``InformationProtectionChangeLabelResponse`` resource.
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/informationprotection/removeLabels",
            json_payload=artifacts,
        )

        return content

    # ------------------------------------------------------------------ #
    #                          Pipelines                                  #
    # ------------------------------------------------------------------ #

    def get_pipelines(
        self,
        expand: str | None = None,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of deployment pipelines for the organization.

        ### Parameters
        ----
        expand : str (optional)
            Expands related entities inline.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminPipeline`` resources.
        """

        params = {
            "$expand": expand,
            "$filter": filter_by,
            "$top": top,
            "$skip": skip,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/pipelines",
            params=params,
        )

        return content

    def get_pipeline_users(self, pipeline_id: str) -> dict:
        """Returns a list of users that have access to a specified
        deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        ### Returns
        ----
        dict
            A collection of ``PipelineUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/pipelines/{pipeline_id}/users",
        )

        return content

    def delete_pipeline_user(
        self, pipeline_id: str, identifier: str
    ) -> dict:
        """Removes user permissions from a specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        identifier : str
            The user principal name (UPN) or object ID of the user to remove.

        ### Returns
        ----
        dict
            Response from the API.
        """

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/admin/pipelines/{pipeline_id}/users/{identifier}",
        )

        return content

    def update_pipeline_user(
        self, pipeline_id: str, user_details: dict
    ) -> dict:
        """Grants user permissions to a specified deployment pipeline.

        ### Parameters
        ----
        pipeline_id : str
            The deployment pipeline ID.

        user_details : dict
            A dict containing user details including ``identifier``,
            ``principalType``, and ``accessRight``.

        ### Returns
        ----
        dict
            Response from the API.
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/admin/pipelines/{pipeline_id}/users",
            json_payload=user_details,
        )

        return content

    # ------------------------------------------------------------------ #
    #                           Profiles                                  #
    # ------------------------------------------------------------------ #

    def get_profiles(
        self,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of service principal profiles for the organization.

        ### Parameters
        ----
        filter_by : str (optional)
            Filters results based on a boolean condition using 'id',
            'displayName', or 'servicePrincipalId'.

        top : int (optional)
            Returns only the first n results (1-5000).

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminServicePrincipalProfile`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/profiles",
            params=params,
        )

        return content

    def delete_profile(self, profile_id: str) -> dict:
        """Deletes the specified service principal profile.

        ### Parameters
        ----
        profile_id : str
            The service principal profile ID.

        ### Returns
        ----
        dict
            Response from the API.
        """

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=f"myorg/admin/profiles/{profile_id}",
        )

        return content

    # ------------------------------------------------------------------ #
    #                           Reports                                   #
    # ------------------------------------------------------------------ #

    def get_reports(
        self,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of reports for the organization.

        ### Parameters
        ----
        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminReport`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/reports",
            params=params,
        )

        return content

    def get_reports_in_group(
        self,
        group_id: str,
        filter_by: str | None = None,
        top: int | None = None,
        skip: int | None = None,
    ) -> dict:
        """Returns a list of reports from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        filter_by : str (optional)
            OData filter query parameter condition.

        top : int (optional)
            Returns only the first n results.

        skip : int (optional)
            Skips the first n results.

        ### Returns
        ----
        dict
            A collection of ``AdminReport`` resources.
        """

        params = {"$filter": filter_by, "$top": top, "$skip": skip}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/groups/{group_id}/reports",
            params=params,
        )

        return content

    def get_report_subscriptions(self, report_id: str) -> dict:
        """Returns a list of report subscriptions along with subscriber
        details. This is a preview API call.

        ### Parameters
        ----
        report_id : str
            The report ID.

        ### Returns
        ----
        dict
            A collection of ``Subscription`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/reports/{report_id}/subscriptions",
        )

        return content

    def get_report_users(self, report_id: str) -> dict:
        """Returns a list of users that have access to the specified report.

        ### Parameters
        ----
        report_id : str
            The report ID.

        ### Returns
        ----
        dict
            A collection of ``ReportUser`` resources.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/reports/{report_id}/users",
        )

        return content

    # ------------------------------------------------------------------ #
    #                            Users                                    #
    # ------------------------------------------------------------------ #

    def get_user_artifact_access(
        self,
        user_id: str,
        continuation_token: str | None = None,
        artifact_types: str | None = None,
    ) -> dict:
        """Returns a list of Power BI items that the specified user has
        access to.

        ### Parameters
        ----
        user_id : str
            The graph ID or user principal name (UPN) of the user.

        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        artifact_types : str (optional)
            Comma-separated list of artifact types.

        ### Returns
        ----
        dict
            An ``ArtifactAccessResponse`` resource.
        """

        params = {
            "continuationToken": continuation_token,
            "artifactTypes": artifact_types,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/users/{user_id}/artifactAccess",
            params=params,
        )

        return content

    def get_user_subscriptions(
        self,
        user_id: str,
        continuation_token: str | None = None,
    ) -> dict:
        """Returns a list of subscriptions for the specified user. Preview API.

        ### Parameters
        ----
        user_id : str
            The graph ID or user principal name (UPN) of the user.

        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        ### Returns
        ----
        dict
            A ``SubscriptionsByUserResponse`` resource.
        """

        params = {"continuationToken": continuation_token}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/users/{user_id}/subscriptions",
            params=params,
        )

        return content

    # ------------------------------------------------------------------ #
    #                    Widely Shared Artifacts                          #
    # ------------------------------------------------------------------ #

    def get_links_shared_to_whole_organization(
        self, continuation_token: str | None = None
    ) -> dict:
        """Returns a list of Power BI reports that are shared with the
        whole organization through links.

        ### Parameters
        ----
        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        ### Returns
        ----
        dict
            An ``ArtifactAccessResponse`` resource.
        """

        params = {"continuationToken": continuation_token}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/widelySharedArtifacts/linksSharedToWholeOrganization",
            params=params,
        )

        return content

    def get_published_to_web(
        self, continuation_token: str | None = None
    ) -> dict:
        """Returns a list of Power BI items that are published to the web.

        ### Parameters
        ----
        continuation_token : str (optional)
            Token required to get the next chunk of the result set.

        ### Returns
        ----
        dict
            An ``ArtifactAccessResponse`` resource.
        """

        params = {"continuationToken": continuation_token}

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/widelySharedArtifacts/publishedToWeb",
            params=params,
        )

        return content

    # ------------------------------------------------------------------ #
    #                       Workspace Info                                #
    # ------------------------------------------------------------------ #

    def get_modified_workspaces(
        self,
        modified_since: str | None = None,
        exclude_personal_workspaces: bool | None = None,
        exclude_inactive_workspaces: bool | None = None,
    ) -> dict:
        """Gets a list of workspace IDs in the organization.

        If ``modified_since`` is set, only IDs of workspaces changed after
        that date-time are returned. The date-time must be in ISO 8601
        compliant UTC format and between 30 minutes and 30 days prior to
        the current time.

        ### Parameters
        ----
        modified_since : str (optional)
            Last modified date in ISO 8601 compliant UTC format.

        exclude_personal_workspaces : bool (optional)
            Whether to exclude personal workspaces.

        exclude_inactive_workspaces : bool (optional)
            Whether to exclude inactive workspaces.

        ### Returns
        ----
        dict
            A list of ``ModifiedWorkspace`` resources.
        """

        params = {
            "modifiedSince": modified_since,
            "excludePersonalWorkspaces": exclude_personal_workspaces,
            "excludeInActiveWorkspaces": exclude_inactive_workspaces,
        }

        content = self.power_bi_session.make_request(
            method="get",
            endpoint="myorg/admin/workspaces/modified",
            params=params,
        )

        return content

    def post_workspace_info(
        self,
        workspaces: list[str],
        lineage: bool | None = None,
        datasource_details: bool | None = None,
        dataset_schema: bool | None = None,
        dataset_expressions: bool | None = None,
        get_artifact_users: bool | None = None,
    ) -> dict:
        """Initiates a call to receive metadata for the requested list of
        workspaces.

        ### Parameters
        ----
        workspaces : list[str]
            The workspace IDs to scan (1 to 100).

        lineage : bool (optional)
            Whether to return lineage info.

        datasource_details : bool (optional)
            Whether to return data source details.

        dataset_schema : bool (optional)
            Whether to return dataset schema (tables, columns, measures).

        dataset_expressions : bool (optional)
            Whether to return dataset expressions (DAX and Mashup queries).

        get_artifact_users : bool (optional)
            Whether to return user details for Power BI items.

        ### Returns
        ----
        dict
            A ``ScanRequest`` resource.
        """

        params = {
            "lineage": lineage,
            "datasourceDetails": datasource_details,
            "datasetSchema": dataset_schema,
            "datasetExpressions": dataset_expressions,
            "getArtifactUsers": get_artifact_users,
        }

        body = {"workspaces": workspaces}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint="myorg/admin/workspaces/getInfo",
            params=params,
            json_payload=body,
        )

        return content

    def get_scan_status(self, scan_id: str) -> dict:
        """Gets the scan status for the specified scan.

        ### Parameters
        ----
        scan_id : str
            The scan ID from a PostWorkspaceInfo call.

        ### Returns
        ----
        dict
            A ``ScanRequest`` resource.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/workspaces/scanStatus/{scan_id}",
        )

        return content

    def get_scan_result(self, scan_id: str) -> dict:
        """Gets the scan result for the specified scan.

        Only call this after a successful ``get_scan_status`` call. The
        scan result will remain available for 24 hours.

        ### Parameters
        ----
        scan_id : str
            The scan ID from a PostWorkspaceInfo call.

        ### Returns
        ----
        dict
            A ``WorkspaceInfoResponse`` resource.
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/admin/workspaces/scanResult/{scan_id}",
        )

        return content
