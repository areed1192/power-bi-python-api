"""Demonstrates initializing `PowerBiClient` with a token you already have.

Useful when the access token was acquired elsewhere — e.g. a service
principal client-credentials flow, a managed identity, or another
part of your application — and you don't want this library to run
its own MSAL/OAuth login flow on top of that.
"""

from powerbi.client import PowerBiClient
from powerbi.token_provider import StaticTokenProvider

# Assume this came from your own auth flow (MSAL, a managed identity,
# a secrets manager, etc.) rather than this library. This placeholder is
# obviously not a real token — replace it with the token string your own
# auth flow produces.
existing_access_token = "REPLACE_WITH_YOUR_ACCESS_TOKEN"

# Wrap it in a StaticTokenProvider: it always returns the same string,
# since this library has no way to refresh a token it didn't acquire.
# If you need automatic refresh, implement your own TokenProvider subclass
# whose get_token() fetches/refreshes internally.
token_provider = StaticTokenProvider(existing_access_token)

# Initialize the Client directly with the provider. `client_id`,
# `client_secret`, `redirect_uri`, and `scope` aren't needed in this
# path since there's no login flow to run.
power_bi_client = PowerBiClient(token_provider=token_provider)

# Use it exactly like a normally-authenticated client.
dashboard_service = power_bi_client.dashboards()
