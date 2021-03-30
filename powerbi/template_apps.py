from typing import Dict
from powerbi.session import PowerBiSession


class TemplateApps():

    def __init__(self, session: object) -> None:
        """Initializes the `TemplateApps` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> template_apps_service = power_bi_client.template_apps()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

        # Set the endpoint.
        self.endpoint = 'myorg/CreateTemplateAppInstallTicket'

    def create_install_ticket(self, app_id: str, owner_tenant_id: str, package_key: str, config: Dict) -> Dict:
        """Generates an installation ticket for Template Apps automated install flow.

        ### Overview
        ----
        This API is only available when using service principal for authentication,
        see Service Principal with Power BI document along with considerations and
        limitations section.

        ### Parameters
        ----
        app_id : str
            Unique application Id.
        
        owner_tenant_id : str
            Application owner's tenant object Id.
        
        package_key : str
            Application version secure key.
        
        config : Dict
            Automated install configuration.

        ### Returns
        ----
        Dict
            A `InstallTicket` resource.

        ### Usage
        ----
            >>> template_apps_service = power_bi_client.template_apps()
            >>> template_apps_service.create_install_ticket(
                    app_id='91ce06d1-d81b-4ea0-bc6d-2ce3dd2f8e87',
                    owner_tenant_id='d43e3248-3d83-44aa-a94d-c836bd7f9b79',
                    package_key='g632bb64...OfsoqT56xEM=',
                    config={
                        'configuration': {
                            'param1': 'value1',
                            'param2': 'value2'
                        }
                    }                
                )
        """

        payload = {
            'appId': app_id,
            'packageKey': package_key,
            'ownerTenantId': owner_tenant_id,
            'config': config
        }

        content = self.power_bi_session.make_request(
            method='post',
            endpoint=self.endpoint,
            json_payload=payload
        )

        return content
