""""Handles all the requests made to the Microsoft Power Bi API Apps endpoint."""

from typing import Dict
from powerbi.session import PowerBiSession


class Apps:
    """Handles all the requests made to the Microsoft Power Bi API Apps endpoint."""

    def __init__(self, session: object) -> None:
        """Initializes the `Apps` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = "myorg/apps"

    def get_app(self, app_id: str) -> Dict:
        """Returns the specified installed app.

        ### Returns
        -------
        Dict
            A collection of `App` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_app(app_id='c0g14be3-38d3-49hc-ef1d-b4f57c9c9058')
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/apps/{app_id}"
        )

        return content

    def get_apps(self) -> Dict:
        """Returns a list of installed apps.

        ### Returns
        -------
        Dict
            A collection of `Apps` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_apps()
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=self.endpoint
        )

        return content

    def get_dashboard(self, app_id: str, dashboard_id: str) -> Dict:
        """Returns the specified dashboard from the specified app.

        ### Returns
        -------
        Dict
            A collection of `Dashboard` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_dashboard(
                app_id='c0g14be3-38d3-49hc-ef1d-b4f57c9c9058',
                dashboard_id='088bbddg-a162-4a31-98f8-1aea79df954a'
                )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/apps/{app_id}/dashboards/{dashboard_id}"
        )

        return content

    def get_dashboards(self, app_id: str) -> Dict:
        """Returns a list of dashboards from the specified app.

        ### Returns
        -------
        Dict
            A collection of `Dashboards` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_dashboards(
                app_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/apps/{app_id}/dashboards"
        )

        return content

    def get_report(self, app_id: str, report_id: str) -> Dict:
        """Returns the specified report from the specified app.

        ### Returns
        -------
        Dict
            A collection of `Report` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_report(
                app_id='f089354e-8366-4e18-aea3-4cb4a3a50b48',
                report_id='088bbddg-a162-4a31-98f8-1aea79df954a'
                )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/apps/{app_id}/reports/{report_id}"
        )

        return content

    def get_reports(self, app_id: str) -> Dict:
        """Returns a list of reports from the specified app.

        ### Returns
        -------
        Dict
            A collection of `Reports` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_reports(
                app_id='f089354e-8366-4e18-aea3-4cb4a3a50b48'
                )
        """

        content = self.power_bi_session.make_request(
            method="get", endpoint=f"myorg/apps/{app_id}/reports"
        )

        return content

    def get_tile(self, app_id: str, dashboard_id: str, tile_id: str) -> Dict:
        """Returns the specified tile within the specified dashboard from the specified app.

        Supported tiles include datasets and live tiles that contain an entire report page.

        ### Returns
        -------
        Dict
            A collection of `Tile` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_tile(
                app_id='f089354e-8366-4e18-aea3-4cb4a3a50b48',
                dashboard_id='5b218778-e7a5-4d73-8187-f10824047715',
                tile_id='312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/apps/{app_id}/dashboards/{dashboard_id}/tiles/{tile_id}",
        )

        return content

    def get_tiles(self, app_id: str, dashboard_id: str) -> Dict:
        """Returns a list of reports from the specified app.

        ### Returns
        -------
        Dict
            A collection of `Tiles` resources.

        ### Usage
        ----
            >>> apps_service = power_bi_client.apps()
            >>> apps_service.get_tiles(
                app_id='f089354e-8366-4e18-aea3-4cb4a3a50b48',
                dashboard_id='5b218778-e7a5-4d73-8187-f10824047715'
                )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=f"myorg/apps/{app_id}/dashboards/{dashboard_id}/tiles",
        )

        return content
