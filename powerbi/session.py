"""Handles all the requests made to the Microsoft Power Bi API."""

import json
import logging

from typing import Dict

import requests

logger = logging.getLogger(__name__)


class PowerBiSession:
    """Serves as the Session for the Current Microsoft
    Power Bi API."""

    def __init__(self, client: object) -> None:
        """Initializes the `PowerBiSession` client.

        ### Overview:
        ----
        The `PowerBiSession` object handles all the requests made
        for the different endpoints on the Microsoft Power Bi API.

        ### Arguments:
        ----
        client (str): The Microsoft Power BI API Python Client.

        ### Usage:
        ----
            >>> power_bi_session = PowerBiSession()
        """

        from powerbi.client import ( # pylint: disable=import-outside-toplevel
            PowerBiClient,
        )

        self.client: PowerBiClient = client
        self.resource_url = "https://api.powerbi.com/"
        self.version = "v1.0/"

        self._session = requests.Session()
        self._session.verify = True

    def build_headers(self) -> Dict:
        """Used to build the headers needed to make the request.

        ### Parameters
        ----
        mode: str, optional
            The content mode the headers is being built for, by default `json`.

        ### Returns
        ----
        Dict:
            A dictionary containing all the components.
        """

        # Fake the headers.
        headers = {
            "Authorization": f"Bearer {self.client.access_token}",
            "Content-Type": "application/json",
        }

        return headers

    def build_url(self, endpoint: str) -> str:
        """Build the URL used the make string.

        ### Parameters
        ----
        endpoint : str
            The endpoint used to make the full URL.

        ### Returns
        ----
        str:
            The full URL with the endpoint needed.
        """

        url = self.resource_url + self.version + endpoint

        return url

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        data: dict = None,
        json_payload: dict = None,
        files: dict = None,
    ) -> Dict:
        """Handles all the requests in the library.

        ### Overview:
        ---
        A central function used to handle all the requests made in the library,
        this function handles building the URL, defining Content-Type, passing
        through payloads, and handling any errors that may arise during the
        request.

        ### Arguments:
        ----
        method : str
            The Request method, can be one of the following:
            ['get','post','put','delete','patch']

        endpoint : str
            The API URL endpoint, example is 'quotes'

        params : dict
            The URL params for the request.

        data : dict
            A data payload for a request.

        json_payload : dict
            A json data payload for a request

        files : dict
            A files payload for multipart/form-data uploads.
            When provided, Content-Type is omitted so requests
            can set the multipart boundary automatically.

        ### Returns:
        ----
            A Dictionary object containing the
            JSON values.
        """

        url = self.build_url(endpoint=endpoint)
        headers = self.build_headers()

        # For multipart file uploads, remove Content-Type so requests
        # can set the multipart boundary automatically.
        if files:
            headers.pop("Content-Type", None)

        logger.info("URL: %s", url)

        prepared = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json_payload,
            files=files,
        ).prepare()

        response: requests.Response = self._session.send(request=prepared)

        # --- error path ---
        if not response.ok:
            try:
                response_data = response.json() if response.content else ""
            except ValueError:
                response_data = response.text

            # Log with the auth header redacted (copy to avoid mutating the original).
            redacted_headers = dict(response.request.headers)
            redacted_headers["Authorization"] = "Bearer XXXXXXX"

            error_dict = {
                "error_code": response.status_code,
                "response_url": response.url,
                "response_body": response_data,
                "response_request": redacted_headers,
                "response_method": response.request.method,
            }

            logger.error(msg=json.dumps(obj=error_dict, indent=4))

            message = (
                f"\033[91m{response.status_code} {response.reason}\033[0m\n"
                f"\033[93mURL:\033[0m {response.url}"
            )
            if response_data:
                message += f"\n\033[93mResponse:\033[0m {response_data}"

            raise requests.HTTPError(message, response=response)

        # --- success path ---
        if not response.content:
            return {
                "message": "response successful",
                "status_code": response.status_code,
            }

        content_type = response.headers.get("Content-Type", "")
        if content_type == "application/zip":
            return response.content

        return response.json()

    def close(self) -> None:
        """Close the underlying requests session."""

        self._session.close()
