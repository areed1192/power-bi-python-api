"""Shared pytest fixtures for the powerbi test suite."""

import pytest
from unittest.mock import MagicMock, patch

from powerbi.auth import PowerBiAuth
from powerbi.session import PowerBiSession
from powerbi.client import PowerBiClient


@pytest.fixture
def mock_auth():
    """Return a PowerBiAuth instance with login patched out."""
    with patch.object(PowerBiAuth, "login"):
        auth = PowerBiAuth(
            client_id="test-client-id",
            client_secret="test-client-secret",
            redirect_uri="https://localhost:44300/",
            scope=["https://analysis.windows.net/powerbi/api/.default"],
        )
        auth.access_token = "fake-access-token"
        auth.refresh_token = "fake-refresh-token"
        yield auth


@pytest.fixture
def mock_session(mock_auth):
    """Return a PowerBiSession whose HTTP layer is mocked."""
    with patch.object(PowerBiAuth, "login"):
        client = PowerBiClient(
            client_id="test-client-id",
            client_secret="test-client-secret",
            redirect_uri="https://localhost:44300/",
            scope=["https://analysis.windows.net/powerbi/api/.default"],
        )
        # The session reads token from self.client (the auth client).
        client.power_bi_auth_client.access_token = "fake-access-token"

        session = client.power_bi_session
        session._session = MagicMock()
        yield session


@pytest.fixture
def power_bi_client():
    """Return a PowerBiClient with auth patched out."""
    with patch.object(PowerBiAuth, "login"):
        client = PowerBiClient(
            client_id="test-client-id",
            client_secret="test-client-secret",
            redirect_uri="https://localhost:44300/",
            scope=["https://analysis.windows.net/powerbi/api/.default"],
        )
        client.access_token = "fake-access-token"
        yield client
