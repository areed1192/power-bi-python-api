from typing import Dict
from powerbi.session import PowerBiSession


class Capacities():

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
            method='get',
            endpoint='myorg/capacities'
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
            method='get',
            endpoint=f'myorg/capacities/{capacity_id}/Workloads'
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
            method='get',
            endpoint=f'myorg/capacities/{capacity_id}/Workloads/{workload_name}'
        )

        return content

    def get_refreshables(self, top: int = 10, expand: str = None, filter: str = None, skip: int = None) -> Dict:
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

        params = {
            '$expand': expand,
            '$filter': filter,
            '$top': top,
            '$skip': skip
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/capacities/refreshables',
            params=params
        )

        return content

    def get_refreshables_for_capacity(self, capacity_id: str, top: int = 10, expand: str = None, filter: str = None, skip: int = None) -> Dict:
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

        params = {
            '$expand': expand,
            '$filter': filter,
            '$top': top,
            '$skip': skip
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/capacities/{capacity_id}/refreshables',
            params=params
        )

        return content
