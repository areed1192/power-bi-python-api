# Authentication

This library uses **MSAL** (Microsoft Authentication Library) with a **Confidential Client**
flow, which is the recommended approach for server-side / backend applications.

## How It Works

1. **Register an app** in the [Power BI App Registration Portal](https://dev.powerbi.com/Apps)
   (or Azure AD). Note your **Client ID**, **Client Secret**, and **Redirect URI**.

2. **First run** — the library opens a browser-based authorization prompt. After you
   sign in, paste the redirect URL back into the terminal. The resulting tokens are
   saved to a local JSON file (`power_bi_state.jsonc`).

3. **Subsequent runs** — the library loads the saved tokens and attempts a **silent SSO**.
   If the access token is still valid, no interaction is needed. If it has expired, the
   refresh token is used automatically to obtain a new access token.

## Configuration

Copy the example config and fill in your credentials:

```console
cp config/config.ini.example config/config.ini
```

```ini
[power_bi_api]
client_id = <your Azure AD app client id>
client_secret = <your Azure AD app client secret>
redirect_uri = https://localhost:44300/
group_id = <your workspace / group id>
```

!!! note
    `config/config.ini` is git-ignored and will never be committed.

## Token Persistence

By passing `credentials="config/power_bi_state.jsonc"` to the client, tokens are
persisted to disk. On subsequent runs, the library will:

1. Load the saved token from the JSON file.
2. Check if the access token is still valid.
3. If expired, use the refresh token to obtain a new access token silently.
4. If the refresh token is also expired, prompt for re-authentication.
