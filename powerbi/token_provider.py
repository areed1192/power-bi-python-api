"""Token provider abstraction for supplying Power BI access tokens."""

from __future__ import annotations

from abc import ABC, abstractmethod


class TokenProvider(ABC):
    """Abstract base for anything that can supply a valid access token.

    Implementations are responsible for deciding internally whether their
    token is still valid and fetching/refreshing it if not. Callers should
    call `get_token()` immediately before each use rather than caching the
    returned value themselves.
    """

    @abstractmethod
    def get_token(self) -> str:
        """Return a valid access token."""


class StaticTokenProvider(TokenProvider):
    """Wraps an already-acquired access token that this library will not
    attempt to refresh or validate.

    Suitable when the caller manages token acquisition/refresh themselves
    (e.g. a service principal client-credentials flow, a managed identity,
    or any auth flow handled outside this library).
    """

    def __init__(self, token: str) -> None:
        self._token = token

    def get_token(self) -> str:
        return self._token
