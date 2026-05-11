"""Module for the Power BI `Admin` service."""

from __future__ import annotations

from typing import Dict
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

    def get_refreshables(
        self,
        top: int,
        expand: str = None,
        filter_by: str = None,
        skip: int = None,
    ) -> Dict:
        """Returns a list of refreshables for the organization within a capacity.

        Power BI retains a seven-day refresh history for each dataset, up to
        a maximum of sixty refreshes.

        ### Permissions
        ----
        The user must be a Fabric administrator or authenticate using a
        service principal. Delegated permissions are supported.

        ### Required Scope
        ----
        Tenant.Read.All or Tenant.ReadWrite.All

        ### Parameters
        ----
        top : int
            Returns only the first n results. Required.

        expand : str (optional, Default=None)
            Accepts a comma-separated list of data types, which will be
            expanded inline in the response. Supports ``capacity``
            and ``group``.

        filter_by : str (optional, Default=None)
            Returns a subset of results based on an OData filter query
            parameter condition.

        skip : int (optional, Default=None)
            Skips the first n results. Use with top to fetch results
            beyond the first 1000.

        ### Returns
        ----
        Dict
            A collection of `Refreshable` resources.

        ### Usage
        ----
            >>> admin_service = power_bi_client.admin()
            >>> admin_service.get_refreshables(top=20)
            >>> admin_service.get_refreshables(
                    top=100,
                    expand='capacity,group',
                    filter_by='averageDuration gt 1800',
                    skip=0
                )
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
