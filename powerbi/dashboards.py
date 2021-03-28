from typing import Dict
from powerbi.session import PowerBiSession


class Dashboards():

    def __init__(self, session: object) -> None:
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

        # Set the endpoint.
        self.endpoint = 'myorg/dashboards'
        self.group_endpoint = 'myorg/groups/{group_id}/dashboards'

    def add_dashboard(self, name: str) -> Dict:
        """Creates a new empty dashboard on `My Workspace`.

        ### Parameters
        ----
        name : str
            The name of the new dashboard.

        ### Returns
        ----
        Dict
            A `Dashboard` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.add_dashboard(name='my_new_dashboard')
        """

        # Define the payload.
        payload = {
            'name': name
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method='post',
            endpoint=self.endpoint,
            json_payload=payload
        )

        return content

    def add_dashboard_in_group(self, name: str, group_id: str) -> Dict:
        """Creates a new empty dashboard on the specified workspace.

        ### Parameters
        ----
        name : str
            The name of the new dashboard.

        group_id : str
            The workspace id.

        ### Returns
        ----
        Dict
            A `Dashboard` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.add_dashboard_in_group(
                name='my_new_dashboard',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        # Define the payload.
        payload = {
            'name': name
        }

        # Make the request.
        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/dashboards',
            json_payload=payload
        )

        return content

    def get_dashboards(self) -> Dict:
        """Returns a list of dashboards from `My Workspace`.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_dashboards()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.endpoint
        )

        return content

    def get_dashboard(self, dashboard_id: str) -> Dict:
        """Returns the specified dashboard from "My Workspace".

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

        ### Returns
        -------
        Dict
            A `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_dashboard(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/dashboards/{dashboard_id}'
        )

        return content

    def get_group_dashboards(self, group_id: str) -> Dict:
        """Returns a list of dashboards from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_group_dashboards(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.group_endpoint.format(group_id=group_id)
        )

        return content

    def get_group_dashboard(self, group_id: str, dashboard_id: str) -> Dict:
        """Returns the specified dashboard from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dashboard_id : str
            The ID of the dashboard you want to query.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_group_dashboard(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dashboard_id='1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/dashboards/{dashboard_id}'
        )

        return content

    def get_tiles(self, dashboard_id: str) -> Dict:
        """Returns a list of tiles within the specified dashboard from "My Workspace".

        ### Overview
        ----
        Note: All tile types are supported except for "model tiles", which include 
        datasets and live tiles that contain an entire report page.

        ### Parameters
        ----
        dashboard_id : str
            The ID of the dashboard you want to query.

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
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/dashboards/{dashboard_id}/tiles'
        )

        return content

    def get_group_tiles(self, group_id: str, dashboard_id: str) -> Dict:
        """Returns a list of tiles within the specified dashboard from the specified workspace.

        ### Overview
        ----
        Note: All tile types are supported except for "model tiles", which include 
        datasets and live tiles that contain an entire report page.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dashboard_id : str
            The ID of the dashboard you want to query.

        ### Returns
        -------
        Dict
            A collection of `Tile` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_group_tiles(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/dashboards/{dashboard_id}/tiles'
        )

        return content

    def get_tile(self, dashboard_id: str, tile_id: str) -> Dict:
        """Returns the specified tile within the specified dashboard from "My Workspace".

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

        ### Returns
        -------
        Dict
            A `Tile` resources.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_tile(
                dashboard_id='bf2c7d16-ec7b-40a2-ab56-f8797fdc5fb8',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/dashboards/{dashboard_id}/tiles/{tile_id}'
        )

        return content

    def get_group_tile(self, group_id: str, dashboard_id: str, tile_id: str) -> Dict:
        """Returns the specified tile within the specified dashboard from the specified workspace.

        ### Overview
        ----
        Note: All tile types are supported except for "model tiles", which include 
        datasets and live tiles that contain an entire report page.

        ### Parameters
        ----
        group_id : str
            The workspace id.

        dashboard_id : str
            The ID of the dashboard you want to query.

        tile_id: str
            The tile id you want to query.

        ### Returns
        -------
        Dict
            A `Tile` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.get_group_tile(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dashboard_id='1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/dashboards/{dashboard_id}/tiles/{tile_id}'
        )

        return content

    def clone_tile(
        self,
        dashboard_id: str,
        tile_id: str,
        target_dashboard_id: str,
        position_conflict_action: str = 'tail',
        target_model_id: str = None,
        target_report_id: str = None,
        target_workspace_id: str = None
    ) -> Dict:
        """Clones the specified tile from "My Workspace".

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
            'targetDashboardId': target_dashboard_id,
            'positionConflictAction': position_conflict_action,
            'targetModelId': target_model_id,
            'targetReportId': target_report_id,
            'targetWorkspaceId': target_workspace_id
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/dashboards/{dashboard_id}/tiles/{tile_id}/Clone',
            json_payload=payload
        )

        return content

    def clone_group_tile(
        self,
        group_id: str,
        dashboard_id: str,
        tile_id: str,
        target_dashboard_id: str,
        position_conflict_action: str = 'tail',
        target_model_id: str = None,
        target_report_id: str = None,
        target_workspace_id: str = None
    ) -> Dict:
        """Clones the specified tile from the specified workspace.

        ### Overview
        ----
        If target report id and target dataset are not specified, the following can occur:
        When a tile clone is performed within the same workspace, the report and dataset 
        links will be cloned from the source tile. When cloning a tile within a different 
        workspace, report and dataset links will be rested, and the tile will be broken.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

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

        ### Returns
        -------
        Dict
            A `Tile` resource.

        ### Usage
        ----
            >>> dashboard_service = power_bi_client.dashboards()
            >>> dashboard_service.clone_tile(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dashboard_id='1a0a15d9-67d1-4e97-b7bd-4f0ed4ec8358',
                tile_id='093bfb85-828e-4705-bcf8-0126dd2d5d70',
                target_dashboard_id='86cb0a0e-612d-4822-9a29-d83478e21199'
            )
        """

        payload = {
            'targetDashboardId': target_dashboard_id,
            'positionConflictAction': position_conflict_action,
            'targetModelId': target_model_id,
            'targetReportId': target_report_id,
            'targetWorkspaceId': target_workspace_id
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/dashboards/{dashboard_id}/tiles/{tile_id}/Clone',
            json_payload=payload
        )

        return content
