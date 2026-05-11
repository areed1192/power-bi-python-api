"""Module for interacting with the `Reports` Service."""

from __future__ import annotations

from enum import Enum
from typing import Dict
from typing import Union

from powerbi.session import PowerBiSession


class Reports:
    """A class for interacting with the Reports Service."""

    def __init__(self, session: PowerBiSession) -> None:
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

    def _build_endpoint(self, path: str, group_id: str = None) -> str:
        if group_id:
            return f"myorg/groups/{group_id}/{path}"
        return f"myorg/{path}"

    def get_reports(self, group_id: str = None) -> Dict:
        """Returns a list of reports.

        ### Parameters
        ----
        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            A collection of `Report` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_reports()
            >>> reports_service.get_reports(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint("reports", group_id),
        )

        return content

    def get_report(self, report_id: str, group_id: str = None) -> Dict:
        """Returns the specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> reports_service.get_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"reports/{report_id}", group_id),
        )

        return content

    def get_pages(self, report_id: str, group_id: str = None) -> Dict:
        """Returns a list of pages within the specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> reports_service.get_pages(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"reports/{report_id}/pages", group_id),
        )

        return content

    def get_page(self, report_id: str, page_name: str, group_id: str = None) -> Dict:
        """Returns the specified page within the specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        page_name : str
            The name of the page.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> reports_service.get_page(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                page_name='ReportSection',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/pages/{page_name}", group_id
            ),
        )

        return content

    def clone_report(
        self,
        report_id: str,
        name: str,
        target_model_id: str = None,
        target_workspace_id: str = None,
        group_id: str = None,
    ) -> Dict:
        """Clones the specified report.

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

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

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
            >>> reports_service.clone_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                name='MyNewReport',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        params = {
            "name": name,
            "targetModelId": target_model_id,
            "targetWorkspaceId": target_workspace_id,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(f"reports/{report_id}/Clone", group_id),
            json_payload=params,
        )

        return content

    def delete_report(self, report_id: str, group_id: str = None) -> None:
        """Deletes the specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.delete_report(
                report_id='c19c7599-7f92-4d11-b384-c9ae33368304'
            )
            >>> reports_service.delete_report(
                report_id='c19c7599-7f92-4d11-b384-c9ae33368304',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="delete",
            endpoint=self._build_endpoint(f"reports/{report_id}", group_id),
        )

        return content

    def export_report(self, report_id: str, group_id: str = None) -> None:
        """Exports the specified report to a .pbix file.

        ### Parameters
        ----
        report_id : str
            The report Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.export_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
            >>> reports_service.export_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(f"reports/{report_id}/export", group_id),
        )

        return content

    def get_datasources(self, report_id: str, group_id: str = None) -> Dict:
        """Returns a list of datasources for the specified RDL report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            A list of `Datasource` resources.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_datasources(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
            >>> reports_service.get_datasources(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/datasources", group_id
            ),
        )

        return content

    def export_to_file(
        self,
        report_id: str,
        file_format: Union[str, Enum],
        paginated_report_configuration: dict = None,
        power_bi_report_configuration: dict = None,
        group_id: str = None,
    ) -> Dict:
        """Exports the specified report to the requested format.

        ### Parameters
        ----
        report_id : str
            The report Id.

        file_format : Union[str, Enum]
            File format you want the report exported to.

        paginated_report_configuration : dict (optional, Default=None)
            The configuration used to export a paginated report.

        power_bi_report_configuration : dict (optional, Default=None)
            The configuration used to export a Power BI report.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            An `Export` resource describing the export job.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.export_to_file(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                file_format='CSV'
            )
            >>> reports_service.export_to_file(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                file_format='PDF',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        if isinstance(file_format, Enum):
            file_format = file_format.value

        params = {
            "format": file_format,
            "paginatedReportConfiguration": paginated_report_configuration,
            "powerBIReportConfiguration": power_bi_report_configuration,
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/ExportTo", group_id
            ),
            json_payload=params,
        )

        return content

    def update_report_content(
        self, report_id: str, request_body: dict, group_id: str = None
    ) -> Dict:
        """Updates the content of the specified report with the content
        of a specified source report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        request_body : dict
            The request body containing sourceReport and sourceType.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            A `Report` resource.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.update_report_content(
                report_id="f0ca06d0-4a40-4329-823d-6184d9a3f468",
                request_body={
                    "sourceReport": {
                        "sourceReportId": "8e4d5880-81d6-4804-ab97-054665050799",
                        "sourceWorkspaceId": "2f42a406-a075-4a15-bbf2-97ef958c94cb"
                    },
                    "sourceType": "ExistingReport"
                }
            )
            >>> reports_service.update_report_content(
                report_id="f0ca06d0-4a40-4329-823d-6184d9a3f468",
                request_body={
                    "sourceReport": {
                        "sourceReportId": "8e4d5880-81d6-4804-ab97-054665050799",
                        "sourceWorkspaceId": "2f42a406-a075-4a15-bbf2-97ef958c94cb"
                    },
                    "sourceType": "ExistingReport"
                },
                group_id="f78705a2-bead-4a5c-ba57-166794b05c78"
            )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/UpdateReportContent", group_id
            ),
            json_payload=request_body,
        )

        return content

    def get_export_to_file_status(
        self, report_id: str, export_id: str, group_id: str = None
    ) -> Dict:
        """Returns the current status of the Export to File job for the
        specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        export_id : str
            The export Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        Dict
            An `Export` resource with job status details.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_export_to_file_status(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                export_id='Mi9C5419i....PS4='
            )
            >>> reports_service.get_export_to_file_status(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                export_id='Mi9C5419i....PS4=',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/exports/{export_id}", group_id
            ),
        )

        return content

    def get_file_of_export_to_file(
        self, report_id: str, export_id: str, group_id: str = None
    ) -> bytes:
        """Returns the file from the Export to File job for the
        specified report.

        ### Parameters
        ----
        report_id : str
            The report Id.

        export_id : str
            The export Id.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Returns
        ----
        bytes
            The exported file content.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.get_file_of_export_to_file(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                export_id='Mi9C5419i....PS4='
            )
            >>> reports_service.get_file_of_export_to_file(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                export_id='Mi9C5419i....PS4=',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        content = self.power_bi_session.make_request(
            method="get",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/exports/{export_id}/file", group_id
            ),
        )

        return content

    def bind_to_gateway(
        self,
        report_id: str,
        gateway_object_id: str,
        bind_details: list = None,
        group_id: str = None,
    ) -> None:
        """Binds the specified data source of the paginated report to
        the specified gateway.

        ### Parameters
        ----
        report_id : str
            The report Id.

        gateway_object_id : str
            The gateway ID. When using a gateway cluster, the gateway ID
            refers to the primary (first) gateway in the cluster.

        bind_details : list (optional, Default=None)
            List of bind detail dicts, each containing 'dataSourceName'
            and 'dataSourceObjectId'.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.bind_to_gateway(
                report_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934',
                bind_details=[
                    {
                        'dataSourceName': 'DataSource1',
                        'dataSourceObjectId': 'dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb'
                    }
                ]
            )
            >>> reports_service.bind_to_gateway(
                report_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                gateway_object_id='1f69e798-5852-4fdd-ab01-33bb14b6e934',
                bind_details=[
                    {
                        'dataSourceName': 'DataSource1',
                        'dataSourceObjectId': 'dc2f2dac-e5e2-4c37-af76-2a0bc10f16cb'
                    }
                ],
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        params = {
            "gatewayObjectId": gateway_object_id,
            "bindDetails": bind_details or [],
        }

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/Default.BindToGateway", group_id
            ),
            json_payload=params,
        )

        return content

    def rebind_report(
        self, report_id: str, dataset_id: str, group_id: str = None
    ) -> None:
        """Rebinds the specified report to the specified dataset.

        ### Parameters
        ----
        report_id : str
            The report Id.

        dataset_id : str
            The new dataset ID for the rebound report. If the dataset
            resides in a different workspace than the report, a shared
            dataset will be created in the report's workspace.

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.rebind_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229'
            )
            >>> reports_service.rebind_report(
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082',
                dataset_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        params = {"datasetId": dataset_id}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/Rebind", group_id
            ),
            json_payload=params,
        )

        return content

    def take_over_in_group(
        self, group_id: str, report_id: str
    ) -> None:
        """Transfers ownership of the data sources for the specified
        paginated report (RDL) to the current authorized user.

        ### Parameters
        ----
        group_id : str
            The workspace Id.

        report_id : str
            The report Id.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.take_over_in_group(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                report_id='cec3fab1-2fc2-424e-8d36-d6180ef05082'
            )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"myorg/groups/{group_id}/reports/{report_id}/Default.TakeOver",
        )

        return content

    def update_datasources(
        self, report_id: str, update_details: list, group_id: str = None
    ) -> None:
        """Updates the data sources of the specified paginated report (RDL).

        ### Parameters
        ----
        report_id : str
            The report Id.

        update_details : list
            A list of update detail dicts, each containing 'datasourceName'
            and 'connectionDetails' (with 'server' and 'database').

        group_id : str (optional, Default=None)
            The workspace id. If not provided, uses "My Workspace".

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> reports_service.update_datasources(
                report_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                update_details=[
                    {
                        'datasourceName': 'SqlDatasource',
                        'connectionDetails': {
                            'server': 'New-Sql-Server',
                            'database': 'New-Sql-Database'
                        }
                    }
                ]
            )
            >>> reports_service.update_datasources(
                report_id='cfafbeb1-8037-4d0c-896e-a46fb27ff229',
                update_details=[
                    {
                        'datasourceName': 'SqlDatasource',
                        'connectionDetails': {
                            'server': 'New-Sql-Server',
                            'database': 'New-Sql-Database'
                        }
                    }
                ],
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78'
            )
        """

        params = {"updateDetails": update_details}

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=self._build_endpoint(
                f"reports/{report_id}/Default.UpdateDatasources", group_id
            ),
            json_payload=params,
        )

        return content
