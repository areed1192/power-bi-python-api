"""Custom exception hierarchy for the Power BI Python SDK."""

from __future__ import annotations


class PowerBiError(Exception):
    """Base exception for all Power BI SDK errors."""


class PowerBiAuthError(PowerBiError):
    """Raised when authentication or token operations fail."""


class PowerBiApiError(PowerBiError):
    """Raised when the Power BI REST API returns an HTTP error.

    Wraps the underlying HTTP error with the status code and
    response body for easier debugging.

    ### Attributes
    ----
    status_code : int
        The HTTP status code returned by the API.
    response_body : str
        The raw response body text.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 0,
        response_body: str = "",
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class PowerBiValidationError(PowerBiError):
    """Raised when client-side input validation fails."""
