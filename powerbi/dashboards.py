"""Module for the `Dashboards` service."""

from typing import Dict
from powerbi.session import PowerBiSession


class Dashboards:
    """Class for the `Dashboards` service."""

    def __init__(self, session: PowerBiSession) -> None:
        """Initializes the `Dashboards` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def _build_endpoint(self, path: str, group_id: str = None) -> str:
        if group_id:
            return f"myorg/groups/{group_id}/{path}"
        return f"myorg/{path}"

    def add_dashboard(self, name: str, group_id: str = None) -> Dict:
        """Creates a new empty dashboard.

        ### Parameters
        ----
        name : str
            The name of the new dashboard.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            A `Dashboard` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.add_dashboard(name='my_new_dashboard')
            >>> dashboard_service.add_dashboard(
                name='my_new_dashboard',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        payload = {"name": name}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint("dashboards", group_id),
            json_payload=payload,
        )

        return content

    def get_dashboards(self, group_id: str = None) -> Dict:
        """Returns a list of dashboards.

        ### Parameters
        ----
        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_dashboards()
            >>> dashboard_service.get_dashboards(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint("dashboards", group_id),
        )

        return content

    def get_dashboard(self, dashboard_id: str, group_id: str = None) -> Dict:
        """Returns the specified dashboard.

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `Dashboard` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_dashboard(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8'
            )
            >>> dashboard_service.get_dashboard(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"dashboards/{dashboard_id}", group_id),
        )

        return content

    def get_tiles(self, dashboard_id: str, group_id: str = None) -> Dict:
        """Returns a list of tiles within the specified dashboard.

        ### Overview
        ----
        Note: All tile types are supported except for "model tiles", which include
        datasets and live tiles that contain an entire report page.

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A collection of `Tile` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_tiles(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8'
            )
            >>> dashboard_service.get_tiles(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"dashboards/{dashboard_id}/tiles", group_id
            ),
        )

        return content

    def get_tile(
        self, dashboard_id: str, tile_id: str, group_id: str = None
    ) -> Dict:
        """Returns the specified tile within the specified dashboard.

        ### Overview
        ----
        Note: All tile types are supported except for "model tiles", which include
        datasets and live tiles that contain an entire report page.

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

        tile_id: str
            The tile id you want to query.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `Tile` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_tile(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70'
            )
            >>> dashboard_service.get_tile(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"dashboards/{dashboard_id}/tiles/{tile_id}", group_id
            ),
        )

        return content

    def clone_tile(
        self,
        dashboard_id: str,
        tile_id: str,
        target_dashboard_id: str,
        position_conflict_action: str = "tail",
        target_model_id: str = None,
        target_report_id: str = None,
        target_workspace_id: str = None,
        group_id: str = None,
    ) -> Dict:
        """Clones the specified tile from the specified dashboard.

        ### Overview
        ----
        If target report id and target dataset are not specified, the following can occur:
        When a tile clone is performed within the same workspace, the report and dataset
        links will be cloned from the source tile. When cloning a tile within a different
        workspace, report and dataset links will be rested, and the tile will be broken.

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

        tile_id: str
            The tile id you want to query.

        target_dashboard_id : str
            The target dashboard id.

        position_conflict_action : str (optional, Default='tail')
            Optional parameter for specifying the action in case of
            position conflict.

        target_model_id : str (optional, Default=None)
            When cloning a tile linked to a dataset, pass the target
            model id to rebind the new tile to a different dataset.

        target_report_id : str (optional, Default=None)
            When cloning a tile linked to a report, pass the target
            report id to rebind the new tile to a different report.

        target_workspace_id : str (optional, Default=None)
            Specifices the target workspace id. Empty Guid
            (00000000-0000-0000-0000-000000000000) indicates 'My Workspace'.
            If not provided, tile will be cloned within the same workspace
            as the source tile.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        -------
        Dict
            A `Tile` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.clone_tile(
                dashboard_id='1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70',
                target_dashboard_id='86cb0a0e-612d-4822-9a29-d83478e21199'
            )
        """

        payload = {
            "targetDashboardId": target_dashboard_id,
            "positionConflictAction": position_conflict_action,
            "targetModelId": target_model_id,
            "targetReportId": target_report_id,
            "targetWorkspaceId": target_workspace_id,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"dashboards/{dashboard_id}/tiles/{tile_id}/Clone", group_id
            ),
            json_payload=payload,
        )

        return content
