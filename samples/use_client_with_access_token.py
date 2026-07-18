"""Demonstrates initializing `PowerBiClient` with a token you already have.

Useful when the access token was acquired elsewhere — e.g. a service
principal client-credentials flow, a managed identity, or another
part of your application — and you don't want this library to run
its own MSAL/OAuth login flow on top of that.
"""

from powerbi.client import PowerBiClient

# Assume this came from your own auth flow (MSAL, a managed identity,
# a secrets manager, etc.) rather than this library.
existing_access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6...."

# Initialize the Client directly with the token. `client_id`,
# `client_secret`, `redirect_uri`, and `scope` aren't needed in this
# path since there's no login flow to run.
power_bi_client = PowerBiClient(access_token=existing_access_token)

# Use it exactly like a normally-authenticated client.
dashboard_service = power_bi_client.dashboards()
