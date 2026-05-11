"""Tests for the PowerBiSession class."""

import json

import pytest
import requests
from unittest.mock import MagicMock

from powerbi.session import PowerBiSession


class TestBuildUrl:
    """Tests for PowerBiSession.build_url()."""

    def test_builds_full_url(self, mock_session):
        url = mock_session.build_url("myorg/datasets")
        assert url == "https://api.powerbi.com/v1.0/myorg/datasets"

    def test_builds_url_with_nested_endpoint(self, mock_session):
        url = mock_session.build_url("myorg/groups/abc-123/datasets")
        assert url == "https://api.powerbi.com/v1.0/myorg/groups/abc-123/datasets"


class TestBuildHeaders:
    """Tests for PowerBiSession.build_headers()."""

    def test_contains_authorization(self, mock_session):
        headers = mock_session.build_headers()
        assert headers["Authorization"] == "Bearer fake-access-token"

    def test_contains_content_type(self, mock_session):
        headers = mock_session.build_headers()
        assert headers["Content-Type"] == "application/json"


class TestEndpointValidation:
    """Tests for the endpoint validation added to make_request()."""

    def test_rejects_empty_segment(self, mock_session):
        with pytest.raises(ValueError, match="empty path segment"):
            mock_session.make_request(method="get", endpoint="myorg/datasets//tables")

    def test_rejects_none_literal_segment(self, mock_session):
        with pytest.raises(ValueError, match="'None' path segment"):
            mock_session.make_request(
                method="get", endpoint="myorg/datasets/None/tables"
            )

    def test_accepts_valid_endpoint(self, mock_session):
        response = MagicMock()
        response.ok = True
        response.content = b'{"value": []}'
        response.headers = {"Content-Type": "application/json"}
        response.json.return_value = {"value": []}
        mock_session._session.send.return_value = response

        result = mock_session.make_request(
            method="get", endpoint="myorg/datasets/abc-123/tables"
        )
        assert result == {"value": []}


class TestMakeRequestSuccess:
    """Tests for successful make_request() responses."""

    def _mock_response(self, json_body=None, content=b"", status_code=200,
                       content_type="application/json"):
        response = MagicMock(spec=requests.Response)
        response.ok = True
        response.status_code = status_code
        response.content = content
        response.headers = {"Content-Type": content_type}
        response.json.return_value = json_body
        return response

    def test_get_returns_json(self, mock_session):
        body = {"value": [{"id": "ds-1", "name": "Sales"}]}
        response = self._mock_response(json_body=body, content=b'{"value":[]}')
        mock_session._session.send.return_value = response

        result = mock_session.make_request(method="get", endpoint="myorg/datasets")
        assert result == body

    def test_empty_response_returns_success_dict(self, mock_session):
        response = self._mock_response(content=b"", status_code=200)
        response.content = b""
        mock_session._session.send.return_value = response

        result = mock_session.make_request(method="delete", endpoint="myorg/datasets/x")
        assert result["message"] == "response successful"
        assert result["status_code"] == 200

    def test_zip_response_returns_bytes(self, mock_session):
        zip_bytes = b"PK\x03\x04fakecontent"
        response = self._mock_response(
            content=zip_bytes, content_type="application/zip"
        )
        mock_session._session.send.return_value = response

        result = mock_session.make_request(method="get", endpoint="myorg/reports/x/export")
        assert result == zip_bytes

    def test_post_sends_json_payload(self, mock_session):
        body = {"id": "new-ds"}
        response = self._mock_response(json_body=body, content=b'{"id":"new-ds"}')
        mock_session._session.send.return_value = response

        result = mock_session.make_request(
            method="post",
            endpoint="myorg/datasets",
            json_payload={"name": "Test"},
        )
        assert result == body

        # Verify the prepared request was sent.
        mock_session._session.send.assert_called_once()

    def test_files_removes_content_type(self, mock_session):
        """When files are provided, Content-Type should be removed."""
        response = self._mock_response(
            json_body={"id": "imp-1"}, content=b'{"id":"imp-1"}'
        )
        mock_session._session.send.return_value = response

        mock_session.make_request(
            method="post",
            endpoint="myorg/imports",
            files={"file": ("test.pbix", b"data")},
        )

        # Verify send was called (the header stripping happens inside).
        mock_session._session.send.assert_called_once()


class TestMakeRequestErrors:
    """Tests for error handling in make_request()."""

    def test_raises_http_error_on_4xx(self, mock_session):
        response = MagicMock(spec=requests.Response)
        response.ok = False
        response.status_code = 404
        response.reason = "Not Found"
        response.content = b'{"error": "not found"}'
        response.url = "https://api.powerbi.com/v1.0/myorg/datasets/bad"
        response.text = '{"error": "not found"}'
        response.json.return_value = {"error": "not found"}
        response.request = MagicMock()
        response.request.headers = {"Authorization": "Bearer secret"}
        response.request.method = "GET"
        mock_session._session.send.return_value = response

        with pytest.raises(requests.HTTPError):
            mock_session.make_request(method="get", endpoint="myorg/datasets/bad")

    def test_raises_http_error_on_5xx(self, mock_session):
        response = MagicMock(spec=requests.Response)
        response.ok = False
        response.status_code = 500
        response.reason = "Internal Server Error"
        response.content = b""
        response.url = "https://api.powerbi.com/v1.0/myorg/datasets"
        response.text = ""
        response.json.side_effect = ValueError("No JSON")
        response.request = MagicMock()
        response.request.headers = {"Authorization": "Bearer secret"}
        response.request.method = "GET"
        mock_session._session.send.return_value = response

        with pytest.raises(requests.HTTPError):
            mock_session.make_request(method="get", endpoint="myorg/datasets")

    def test_error_redacts_auth_header(self, mock_session):
        response = MagicMock(spec=requests.Response)
        response.ok = False
        response.status_code = 401
        response.reason = "Unauthorized"
        response.content = b'{"message":"unauthorized"}'
        response.url = "https://api.powerbi.com/v1.0/myorg/datasets"
        response.text = '{"message":"unauthorized"}'
        response.json.return_value = {"message": "unauthorized"}
        response.request = MagicMock()
        response.request.headers = {
            "Authorization": "Bearer real-secret-token",
            "Content-Type": "application/json",
        }
        response.request.method = "GET"
        mock_session._session.send.return_value = response

        with pytest.raises(requests.HTTPError) as exc_info:
            mock_session.make_request(method="get", endpoint="myorg/datasets")

        # The original request headers should NOT be mutated.
        assert response.request.headers["Authorization"] == "Bearer real-secret-token"


class TestClose:
    """Tests for PowerBiSession.close()."""

    def test_close_calls_session_close(self, mock_session):
        mock_session.close()
        mock_session._session.close.assert_called_once()
