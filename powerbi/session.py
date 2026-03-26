"""Handles all the requests made to the Microsoft Power Bi API."""

import sys
import json
import logging
import pathlib

from typing import Dict

import requests


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

        # We can also add custom formatting to our log messages.
        log_format = "%(asctime)-15s|%(filename)s|%(message)s"

        self.client: PowerBiClient = client
        self.resource_url = "https://api.powerbi.com/"
        self.version = "v1.0/"

        self._session = requests.Session()
        self._session.verify = True

        if not pathlib.Path("logs").exists():
            pathlib.Path("logs").mkdir()
            pathlib.Path("logs/log_file_custom.log").touch()
        if sys.version_info[1] == 8:
            logging.basicConfig(
                filename="logs/log_file_custom.log",
                level=logging.INFO,
                format=log_format,
            )
        else:
            logging.basicConfig(
                filename="logs/log_file_custom.log",
                level=logging.INFO,
                encoding="utf-8",
                format=log_format,
            )

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

        ### Returns:
        ----
            A Dictionary object containing the
            JSON values.
        """

        url = self.build_url(endpoint=endpoint)
        headers = self.build_headers()

        logging.info("URL: %s", url)

        prepared = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json_payload,
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

            logging.error(msg=json.dumps(obj=error_dict, indent=4))

            raise requests.HTTPError(
                f"""
                {response.status_code} {response.reason}
                for url: {response.url} | {response_data}
                """,
                response=response,
            )

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
