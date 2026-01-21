"""Module for the Power BI `EmbedTokens` service."""

from enum import Enum

from powerbi.session import PowerBiSession


class EmbedTokens:
    """Class for the `EmbedTokens` service."""

    def __init__(self, session: object) -> None:
        """Initializes the `EmbedTokens` service.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> embed_token_service = power_bi_client.embed_tokens()
        """

        # Set the session.
        self.power_bi_session: PowerBiSession = session

    def dashboards_generate_token_in_group(
        self,
        group_id: str,
        dashboard_id: str,
        access_level: str | Enum,
        dataset_id: str,
        identities: list,
        lifetime_in_minutes: int,
        allow_save_as: bool = False,
    ) -> dict:
        """Returns a list of datasets in a group.

        ### Parameters
        ----
        group_id : str
            The Workspace ID.

        dashboard_id : str
            The Dashboard ID.

        access_level : str | Enum
            The required access level for embed token
            generation.

        dataset_id : str
            The dataset ID used for report creation. Only
            applies when you generate an embed token for
            report creation.

        identities : list
            A list of identities to be used for the embed token.

        allow_save_as : bool (optional, default=False)
            Whether an embedded report can be saved as a new
            report. The default value is false. Only applies
            when you generate an embed token for report
            embedding.


        ### Returns
        -------
        Dict
            A collection of `Dataset` resources.

        ### Usage
        ----
            >>> embed_tokens_service = power_bi_client.embed_tokens()
            >>> embed_tokens_service.dashboards_generate_token_in_group(
                group_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                dashboard_id='f78705a2-bead-4a5c-ba57-166794b05c78',
                access_level='',
                dataset_id='',
                identities=[],
                allow_save_as=False
            )
        """

        content = self.power_bi_session.make_request(
            method="post",
            endpoint=f"/myorg/groups/{group_id}/dashboards/{dashboard_id}/GenerateToken",
        )

        return content
