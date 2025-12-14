""""Module for the PowerBi `Capacities` service."""

from enum import Enum
from typing import Dict
from powerbi.session import PowerBiSession


class Capacities:
    """Class for the `Capacities` service."""

    def __init__(self, session: object) -> None:
        """Initializes the `Capacities` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def get_capacities(self) -> Dict:
        """Returns a list of capacities the user has access to.

        ### Returns
        ----
        Dict
            A collection of `Capacities` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_capacities()
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get", endpoint="myorg/capacities"
        )

        return content

    def get_workloads(self, capacity_id: str) -> Dict:
        """Returns the current state of the specified capacity workloads, if a
        workload is enabled also returns the maximum memory percentage that
        the workload can consume.

        ### Parameters
        ----
        capacity_id: str
            The capacity Id.

        ### Returns
        ----
        Dict
            A collection of `Workload` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_workloads(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413'
            )
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/capacities/{capacity_id}/Workloads"
        )

        return content

    def get_workload(self, capacity_id: str, workload_name: str) -> Dict:
        """Returns the current state of the specified capacity workloads, if a
        workload is enabled also returns the maximum memory percentage that
        the workload can consume.

        ### Parameters
        ----
        capacity_id: str
            The capacity Id.

        workload_name: str
            The name of the workload.

        ### Returns
        ----
        Dict
            A collection of `Workload` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_workload(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413',
                workload_name='my-workload'
            )
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/capacities/{capacity_id}/Workloads/{workload_name}",
        )

        return content

    def get_refreshables(
        self, top: int = 10, expand: str = None, filter: str = None, skip: int = None
    ) -> Dict:
        """Returns a list of refreshables for all capacities of which the user has access to.

        ### Parameters
        ----
        top: int (optional, Default=10)
            Returns only the first n results.

        expand: str (optional, Default=None)
            Expands related entities inline, receives a comma-separated list of
            data types. Supported: capacities and groups.

        filter: str (optional, Default=None)
            Filters the results based on a boolean condition.

        skip: int (optional, Default=None)
            Skips the first n results. Use with top to fetch results
            beyond the first 1000.

        ### Returns
        ----
        Dict
            A collection of `Refreshable` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_refreshables(
                top=10
            )
        """

        params = {"$expand": expand, "$filter": filter, "$top": top, "$skip": skip}

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get", endpoint="myorg/capacities/refreshables", params=params
        )

        return content

    def get_refreshables_for_capacity(
        self,
        capacity_id: str,
        top: int = 10,
        expand: str = None,
        filter: str = None,
        skip: int = None,
    ) -> Dict:
        """Returns a list of refreshables for the specified capacity the user has access to.

        ### Parameters
        ----
        capacity_id: str
            The capacity id.

        top: int (optional, Default=10)
            Returns only the first n results.

        expand: str (optional, Default=None)
            Expands related entities inline, receives a comma-separated list of
            data types. Supported: capacities and groups.

        filter: str (optional, Default=None)
            Filters the results based on a boolean condition.

        skip: int (optional, Default=None)
            Skips the first n results. Use with top to fetch results
            beyond the first 1000.

        ### Returns
        ----
        Dict
            A collection of `Refreshable` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_refreshables_for_capacity(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413',
                top=10
            )
        """

        params = {"$expand": expand, "$filter": filter, "$top": top, "$skip": skip}

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/capacities/{capacity_id}/refreshables",
            params=params,
        )

        return content

    def get_refreshable_for_capacity(
        self,
        capacity_id: str,
        refreshable_id: str,
        expand: str = None,
    ) -> Dict:
        """Returns the specified refreshable for the specified capacity
        that the user has access to.

        ### Parameters
        ----
        capacity_id: str
            The capacity id.

        refreshable_id: str
            The refreshable id.

        expand: str (optional, Default=None)
            Expands related entities inline, receives a comma-separated
            list of data types. Supported: `capacities` and `groups`.

        ### Returns
        ----
        Dict
            A collection of `Refreshable` resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.get_refreshable_for_capacity(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413',
                refreshable_id='my-refreshable',
                expand='capacities'
            )
        """

        if expand is None:
            params = {}
        else:
            params = {"$expand": expand}

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/capacities/{capacity_id}/refreshables/{refreshable_id}",
            params=params,
        )

        return content

    def groups_assign_my_workspace_to_capacity(
        self,
        capacity_id: str,
    ) -> None:
        """Assigns My workspace to the specified capacity.

        ### Parameters
        ----
        capacity_id: str
            The capacity id.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.groups_assign_my_workspace_to_capacity(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413'
            )
        """

        body = {"capacityId": capacity_id}

        # Make the request.
        content = self.power_bi_session.make_request(
            method="post", endpoint="/myorg/AssignToCapacity", json_payload=body
        )

        return content

    def groups_assign_to_capacity(
        self,
        group_id: str,
        capacity_id: str,
    ) -> None:
        """Assigns the specified workspace to the specified capacity.

        ### Parameters
        ----
        group_id: str
            The workspace id.

        capacity_id: str
            The capacity id.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.groups_assign_to_capacity(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413'
            )
        """

        body = {"capacityId": capacity_id}

        # Make the request.
        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"/myorg/groups/{group_id}/AssignToCapacity",
            json_payload=body,
        )

        return content

    def groups_capacity_assignment_status(self, group_id: str) -> dict:
        """Gets the status of the assignment-to-capacity operation for the
        specified workspace.

        ### Parameters
        ----
        group_id: str
            The workspace id.

        ### Returns
        ----
        dict
            A collection of `CapacityAssignmentStatus`
            resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.groups_capacity_assignment_status(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
            )
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"/myorg/groups/{group_id}/CapacityAssignmentStatus",
        )

        return content

    def groups_capacity_assignment_status_my_workspace(self) -> dict:
        """Gets the status of the My workspace assignment-to-capacity
        operation.

        ### Returns
        ----
        dict
            A collection of `CapacityAssignmentStatus`
            resources.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.groups_capacity_assignment_status_my_workspace()
        """

        # Make the request.
        content = self.power_bi_session.make_request(
            method="get",
            endpoint="/myorg/CapacityAssignmentStatus",
        )

        return content

    def patch_workload(
        self,
        capacity_id: str,
        workload_name: str,
        state: str | Enum,
        max_memory_percentage_set_by_user: int = None,
    ) -> None:
        """Changes the state of a specific workload to Enabled or Disabled.
        When enabling a workload, specify the percentage of maximum
        memory that the workload can consume.

        ### Parameters
        ----
        capacity_id: str
            The capacity Id.

        workload_name: str
            The name of the workload.

        state: str | Enum
            The state of the workload. Can be either
            `Enabled` or `Disabled`.

        max_memory_percentage_set_by_user: int (optional, Default=None)
            The percentage of maximum memory that the
            workload can consume.

        ### Usage
        ----
            >>> capacities_service = power_bi_client.capacities()
            >>> capacities_service.patch_workload(
                capacity_id='890D018E-4B64-4BB1-97E5-BD5490373413',
                workload_name='my-workload',
                state='Enabled',
                max_memory_percentage_set_by_user=50
            )
        """

        # Make sure percentage is between 0 and 100.
        if max_memory_percentage_set_by_user is not None:
            if (
                max_memory_percentage_set_by_user < 0
                or max_memory_percentage_set_by_user > 100
            ):
                raise ValueError(
                    "max_memory_percentage_set_by_user must be between 0 and 100."
                )

        # Check if enum is passed.
        if isinstance(state, Enum):
            state = state.value

        body = {
            "state": state,
            "maxMemoryPercentageSetByUser": max_memory_percentage_set_by_user,
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method="patch",
            endpoint=f"/myorg/capacities/{capacity_id}/Workloads/{workload_name}",
            json_payload=body,
        )

        return content
