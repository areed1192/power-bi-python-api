import json

from typing import Dict
from typing import Union
from powerbi.utils import Dataset
from powerbi.utils import Table
from powerbi.utils import PowerBiEncoder
from powerbi.session import PowerBiSession
from enum import Enum


class Reports():

    def __init__(self, session: object) -> None:
        """Initializes the `Reports` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def get_reports(self) -> Dict:
        """Returns a list of reports from "My Workspace".

        ### Returns
        ----
        Dict
            A collection of `Report` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_reports()
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports',
        )

        return content

    def get_group_reports(self, group_id: str) -> Dict:
        """Returns a list of reports from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        ### Returns
        ----
        Dict
            A collection of `Report` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_group_reports(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/reports',
        )

        return content

    def get_report(self, report_id: str) -> Dict:
        """Returns the specified report from "My Workspace".

        ### Parameters
        ----
        report_id : str
            The report Id.

        ### Returns
        ----
        Dict
            A `Report` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports/{report_id}',
        )

        return content

    def get_group_report(self, group_id: str, report_id: str) -> Dict:
        """Returns the specified report from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        ### Returns
        ----
        Dict
            A `Report` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_group_reports(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}',
        )

        return content

    def get_pages(self, report_id: str) -> Dict:
        """Returns a list of pages within the specified report from "My Workspace".

        ### Parameters
        ----
        report_id : str
            The report Id.

        ### Returns
        ----
        Dict
            A collection of `Page` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_pages(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports/{report_id}/pages',
        )

        return content

    def get_group_pages(self, group_id: str, report_id: str) -> Dict:
        """Returns a list of pages within the specified report from the 
        specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        ### Returns
        ----
        Dict
            A collection of `Page` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_group_pages(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}/pages',
        )

        return content

    def get_page(self, report_id: str, page_name: str) -> Dict:
        """Returns the specified page within the specified report from the 
        specified workspace.

        ### Parameters
        ----
        report_id : str
            The report Id.

        page_name : str
            The name of the page.

        ### Returns
        ----
        Dict
            A `Page` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_page(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                page_name='ReportSection'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports/{report_id}/pages/{page_name}',
        )

        return content

    def get_group_page(self, group_id: str, report_id: str, page_name: str) -> Dict:
        """Returns a list of pages within the specified report from the 
        specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        page_name : str
            The name of the page.

        ### Returns
        ----
        Dict
            A `Page` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_group_page(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                page_name='ReportSection'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}/pages/{page_name}',
        )

        return content

    def clone_report(self, report_id: str, name: str, target_model_id: str = None, target_workspace_id: str = None) -> Dict:
        """Clones the specified report from "My Workspace".

        ### Parameters
        ----
        report_id : str
            The report Id.

        name : str
            The new report name.

        target_model_id : str (optional, Default=None)
            Optional parameter for specifying the target associated dataset id.
            If not provided, the new report will be associated with the same 
            dataset as the source report

        target_workspace_id : str (optional, Default=None)
            Optional parameter for specifying the target workspace id. Empty 
            Guid (00000000-0000-0000-0000-000000000000) indicates 'My Workspace'.
            If not provided, the new report will be cloned within the same workspace
            as the source report.

        ### Returns
        ----
        Dict
            A `Report` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.clone_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                name='MyNewReport'
            )
        """

        params = {
            'name': name,
            'targetModelId': target_model_id,
            'targetWorkspaceId': target_workspace_id
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/reports/{report_id}/Clone',
            json_payload=params
        )

        return content

    def clone_group_report(
        self,
        group_id: str,
        report_id: str,
        name: str,
        target_model_id: str = None,
        target_workspace_id: str = None
    ) -> Dict:
        """Clones the specified report from "My Workspace".

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        name : str
            The new report name.

        target_model_id : str (optional, Default=None)
            Optional parameter for specifying the target associated dataset id.
            If not provided, the new report will be associated with the same 
            dataset as the source report

        target_workspace_id : str (optional, Default=None)
            Optional parameter for specifying the target workspace id. Empty 
            Guid (00000000-0000-0000-0000-000000000000) indicates 'My Workspace'.
            If not provided, the new report will be cloned within the same workspace
            as the source report.

        ### Returns
        ----
        Dict
            A `Report` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.clone_group_report(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                name='MyNewReport'
            )
        """

        params = {
            'name': name,
            'targetModelId': target_model_id,
            'targetWorkspaceId': target_workspace_id
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}/Clone',
            json_payload=params
        )

        return content

    def delete_report(self, report_id: str) -> None:
        """Deletes the specified report from "My Workspace".

        ### Parameters
        ----
        report_id : str
            The report Id.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.delete_report(
                report_id='c19c7599-7f92-4d11-b384-c9ae33368304'
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/reports/{report_id}'
        )

        return content

    def delete_group_report(self, group_id: str, report_id: str) -> None:
        """Clones the specified report from "My Workspace".

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.delete_group_report(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='f0ca06d0-4a40-4329-823d-6184d9a3f468',
            )
        """

        content = self.power_bi_session.make_request(
            method='delete',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}'
        )

        return content

    def export_report(self, report_id: str) -> None:
        """Exports the specified report from "My Workspace" to 
        a .pbix file.

        ### Parameters
        ----
        report_id : str
            The report Id.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.export_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports/{report_id}/export'
        )

        return content

    def export_group_report(self, group_id: str, report_id: str) -> None:
        """Exports the specified report from "My Workspace" to 
        a .pbix file.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.export_group_report(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/reports/{report_id}/export'
        )

        return content

    def get_datasources(self, report_id: str) -> Dict:
        """Returns a list of datasources for the specified RDL 
        report from "My Workspace".

        ### Parameters
        ----
        report_id : str
            The report Id.

        ### Returns
        ----
            A list of `Datsource` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_datasources(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/reports/{report_id}/datasources'
        )

        return content

    def export_to_file(
        self,
        report_id: str,
        file_format: Union[str, Enum],
        paginated_report_configuration: dict = None,
        power_bi_report_configuration: dict = None
    ) -> bytes:
        """Exports the specified report from "My Workspace" to 
        requested format.

        ### Parameters
        ----
        report_id : str
            The report Id.

        file_format : Union[str, Enum]
            File format you want the reprot expored to.

        paginated_report_configuration : dict (optional, Default=None)
            The configuration used to export a paginated report.

        power_bi_report_configuration : dict (optional, Default=None)
            The configuration used to export a Power BI report.

        ### Returns
        ----
            A bytes stream.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.export_to_file(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                file_format='CSV'
            )
        """

        if isinstance(file_format, Enum):
            file_format = file_format.value

        params = {
            'format': file_format,
            'paginatedReportConfiguration': paginated_report_configuration,
            'powerBIReportConfiguration': power_bi_report_configuration
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/reports/{report_id}/ExportTo',
            json_payload=params
        )

        return content

    def _group_export_to_file(self) -> None:
        pass

    def _get_export_to_file_status(self) -> None:
        pass

    def _get_group_export_to_file_status(self) -> None:
        pass

    def _get_export_to_file_results(self) -> None:
        pass

    def _get_group_export_to_file_results(self) -> None:
        pass
