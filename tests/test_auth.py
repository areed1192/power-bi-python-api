"""Tests for the PowerBiAuth class."""

import json
import time

import pytest
from unittest.mock import patch, MagicMock, mock_open

from powerbi.auth import PowerBiAuth


@pytest.fixture
def auth():
    """Return a PowerBiAuth instance with MSAL patched."""
    with patch("powerbi.auth.msal.ConfidentialClientApplication"):
        auth = PowerBiAuth(
            client_id="test-client-id",
            client_secret="test-client-secret",
            redirect_uri="https://localhost:44300/",
            scope=["https://analysis.windows.net/powerbi/api/.default"],
        )
        yield auth


class TestInit:
    """Tests for PowerBiAuth.__init__()."""

    def test_stores_client_id(self, auth):
        assert auth.client_id == "test-client-id"

    def test_stores_client_secret(self, auth):
        assert auth.client_secret == "test-client-secret"

    def test_stores_redirect_uri(self, auth):
        assert auth.redirect_uri == "https://localhost:44300/"

    def test_stores_scope(self, auth):
        assert auth.scope == ["https://analysis.windows.net/powerbi/api/.default"]

    def test_default_account_type(self, auth):
        assert auth.account_type == "common"

    def test_tokens_initially_none(self, auth):
        assert auth.access_token is None
        assert auth.refresh_token is None

    def test_creates_msal_app(self, auth):
        assert auth.client_app is not None


class TestTokenSeconds:
    """Tests for PowerBiAuth._token_seconds()."""

    def test_returns_zero_when_no_access_token(self, auth):
        auth.access_token = None
        assert auth._token_seconds("access_token") == 0

    def test_returns_zero_when_access_token_expired(self, auth):
        auth.access_token = "some-token"
        auth.token_dict = {"expires_in": time.time() - 10}
        assert auth._token_seconds("access_token") == 0

    def test_returns_positive_when_access_token_valid(self, auth):
        auth.access_token = "some-token"
        auth.token_dict = {"expires_in": time.time() + 3600}
        result = auth._token_seconds("access_token")
        assert result > 3500

    def test_returns_zero_when_no_refresh_token(self, auth):
        auth.refresh_token = None
        assert auth._token_seconds("refresh_token") == 0

    def test_returns_zero_when_refresh_token_expired(self, auth):
        auth.refresh_token = "some-refresh"
        auth.token_dict = {"ext_expires_in": time.time() - 10}
        assert auth._token_seconds("refresh_token") == 0

    def test_returns_positive_when_refresh_token_valid(self, auth):
        auth.refresh_token = "some-refresh"
        auth.token_dict = {"ext_expires_in": time.time() + 7200}
        result = auth._token_seconds("refresh_token")
        assert result > 7000

    def test_raises_on_invalid_token_type(self, auth):
        with pytest.raises(ValueError, match="Invalid Token Type"):
            auth._token_seconds("bad_type")


class TestSilentSso:
    """Tests for PowerBiAuth._silent_sso()."""

    def test_returns_true_when_access_token_valid(self, auth):
        auth.access_token = "valid"
        auth.token_dict = {"expires_in": time.time() + 3600}
        assert auth._silent_sso() is True

    def test_returns_true_when_refresh_succeeds(self, auth):
        auth.access_token = "expired"
        auth.token_dict = {"expires_in": time.time() - 100}
        auth.refresh_token = "valid-refresh"

        new_token = {
            "access_token": "new-access",
            "refresh_token": "new-refresh",
            "expires_in": 3600,
            "ext_expires_in": 7200,
        }
        auth.client_app.acquire_token_by_refresh_token.return_value = new_token
        auth.credentials = None  # skip file I/O

        with patch.object(auth, "_load_or_save_credentials"):
            assert auth._silent_sso() is True

    def test_returns_false_when_no_tokens(self, auth):
        auth.access_token = None
        auth.refresh_token = None
        auth.token_dict = None
        assert auth._silent_sso() is False


class TestLogin:
    """Tests for PowerBiAuth.login()."""

    def test_login_silent_sso_success_skips_prompt(self, auth):
        auth.credentials = None
        with patch.object(auth, "_load_or_save_credentials"), \
             patch.object(auth, "_silent_sso", return_value=True):
            auth.login()
            # No input() called - silent SSO short-circuited.

    def test_login_prompts_when_silent_fails(self, auth):
        auth.credentials = None
        redirect_url = "https://localhost:44300/?code=auth-code&state=xyz"

        with patch.object(auth, "_load_or_save_credentials"), \
             patch.object(auth, "_silent_sso", return_value=False), \
             patch.object(auth, "authorization_url", return_value="https://login.example.com/auth"), \
             patch("builtins.input", return_value=redirect_url), \
             patch.object(auth, "grab_access_token") as mock_grab:
            auth.login()
            mock_grab.assert_called_once()


class TestGrabRefreshToken:
    """Tests for PowerBiAuth.grab_refresh_token()."""

    def test_successful_refresh(self, auth):
        new_token = {
            "access_token": "new-access",
            "refresh_token": "new-refresh",
            "expires_in": 3600,
            "ext_expires_in": 7200,
        }
        auth.client_app.acquire_token_by_refresh_token.return_value = new_token
        auth.refresh_token = "old-refresh"

        with patch.object(auth, "_load_or_save_credentials") as mock_save:
            result = auth.grab_refresh_token()
            assert result["access_token"] == "new-access"
            mock_save.assert_called_once_with(action="save", token_dict=new_token)

    def test_failed_refresh_raises_permission_error(self, auth):
        auth.client_app.acquire_token_by_refresh_token.return_value = {
            "error": "invalid_grant",
            "error_description": "token expired",
        }
        auth.refresh_token = "bad-refresh"

        with pytest.raises(PermissionError, match="Permissions not authorized"):
            auth.grab_refresh_token()


class TestLoadOrSaveCredentials:
    """Tests for PowerBiAuth._load_or_save_credentials()."""

    def test_load_returns_true_when_file_has_refresh_token(self, auth, tmp_path):
        cred_file = tmp_path / "state.jsonc"
        cred_data = {
            "access_token": "at",
            "refresh_token": "rt",
            "expires_in": time.time() + 3600,
            "ext_expires_in": time.time() + 7200,
        }
        cred_file.write_text(json.dumps(cred_data))
        auth.credentials = str(cred_file)

        result = auth._load_or_save_credentials(action="load")
        assert result is True
        assert auth.access_token == "at"
        assert auth.refresh_token == "rt"

    def test_load_returns_false_when_no_refresh_token(self, auth, tmp_path):
        cred_file = tmp_path / "state.jsonc"
        cred_file.write_text(json.dumps({"access_token": "at"}))
        auth.credentials = str(cred_file)

        result = auth._load_or_save_credentials(action="load")
        assert result is False

    def test_save_writes_file(self, auth, tmp_path):
        cred_file = tmp_path / "state.jsonc"
        auth.credentials = str(cred_file)

        token_dict = {
            "access_token": "saved-at",
            "refresh_token": "saved-rt",
            "expires_in": 3600,
            "ext_expires_in": 7200,
        }
        auth._load_or_save_credentials(action="save", token_dict=token_dict)

        saved = json.loads(cred_file.read_text())
        assert saved["access_token"] == "saved-at"
        assert saved["refresh_token"] == "saved-rt"
        # expires_in should have been converted to an absolute timestamp.
        assert saved["expires_in"] > time.time()

    def test_load_returns_none_when_file_missing(self, auth, tmp_path):
        auth.credentials = str(tmp_path / "nonexistent.jsonc")
        result = auth._load_or_save_credentials(action="load")
        assert result is None


class TestAuthorizationUrl:
    """Tests for PowerBiAuth.authorization_url()."""

    def test_returns_url_from_msal(self, auth):
        auth.client_app.get_authorization_request_url.return_value = (
            "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=test"
        )
        url = auth.authorization_url()
        assert "login.microsoftonline.com" in url
        auth.client_app.get_authorization_request_url.assert_called_once()
