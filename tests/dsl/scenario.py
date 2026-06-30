from __future__ import annotations

import datetime
import http
import os
import uuid
from dataclasses import dataclass, field
from typing import Any

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth._token import Token
from france_travail_api.auth.scope import Scope
from france_travail_api.client import FranceTravailClient
from france_travail_api.http_transport._http_client import HttpClient
from france_travail_api.http_transport._http_response import HTTPResponse
from france_travail_api.offres._client import FranceTravailOffresClient
from france_travail_api.offres.models.appellation import Appellation
from france_travail_api.offres.models.metier import Metier
from france_travail_api.offres.models.offre import Offre
from tests.test_doubles.fake_http_client import FakeHttpClient


@dataclass
class Scenario:
    now: datetime.datetime = field(
        default_factory=lambda: datetime.datetime(2025, 12, 25, 10, 0, 0, tzinfo=datetime.UTC)
    )
    _http_client: HttpClient | FakeHttpClient | None = None
    _credentials: FranceTravailCredentials | None = None
    _offres_client: FranceTravailOffresClient | None = None
    _client: FranceTravailClient | None = None
    _captured_exception: Exception | None = None
    _token: Token | None = None
    _authorization_header: dict[str, str] | None = None
    _offers: list[Offre] | None = None
    _offre: Offre | None = None
    _metiers: list[Metier] | None = None
    _appellations: list[Appellation] | None = None

    def unit(self) -> "Scenario":
        self._http_client = FakeHttpClient()
        return self

    def integration(self) -> "Scenario":
        self._http_client = HttpClient()
        return self

    def e2e(self) -> "Scenario":
        self._client = FranceTravailClient(
            os.environ["FRANCE_TRAVAIL_CLIENT_ID"],
            os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"],
            scopes=[Scope.OFFRES],
        )
        return self

    def with_http_client(self, http_client: HttpClient | FakeHttpClient) -> "Scenario":
        self._http_client = http_client
        return self

    def with_credentials(self, client_id: str, client_secret: str, scopes: list[Scope]) -> "Scenario":
        if self._http_client is None:
            self._http_client = HttpClient()
        self._credentials = FranceTravailCredentials(client_id, client_secret, scopes, self._http_client)  # type: ignore[arg-type]
        return self

    def with_live_credentials(self, scopes: list[Scope]) -> "Scenario":
        return self.with_credentials(
            client_id=os.environ["FRANCE_TRAVAIL_CLIENT_ID"],
            client_secret=os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"],
            scopes=scopes,
        )

    def with_token_response(self, access_token: str = "my_token", expires_in: int = 1_499) -> "Scenario":
        return self.with_http_response(
            HTTPResponse(
                status_code=http.HTTPStatus.OK,
                body={
                    "scope": "api_offresdemploiv2 o2dsoffre",
                    "expires_in": expires_in,
                    "token_type": "Bearer",
                    "access_token": access_token,
                },
                headers={},
                request_id=uuid.uuid4(),
            )
        )

    def with_error_response(
        self,
        status_code: http.HTTPStatus = http.HTTPStatus.BAD_REQUEST,
        error: str = "unknown_error",
        description: str = "An unknown error occurred",
    ) -> "Scenario":
        return self.with_http_response(
            HTTPResponse(
                status_code=status_code,
                body={"error": error, "error_description": description},
                headers={},
                request_id=uuid.uuid4(),
            )
        )

    def with_http_response(self, response: HTTPResponse) -> "Scenario":
        if not isinstance(self._http_client, FakeHttpClient):
            self._http_client = FakeHttpClient()
        self._http_client.add_response(response)
        return self

    def with_offres_client(self) -> "Scenario":
        if self._credentials is None:
            raise ValueError("Credentials must be configured before offres client")
        if self._http_client is None:
            raise ValueError("HTTP client must be configured before offres client")
        self._offres_client = FranceTravailOffresClient(self._credentials, self._http_client)  # type: ignore[arg-type]
        return self

    def when_get_token(self) -> "Scenario":
        if self._credentials is None:
            raise ValueError("Credentials must be configured before requesting token")
        try:
            self._token = self._credentials.get_token(self.now)
        except Exception as exc:  # pragma: no cover - used by expectations
            self._captured_exception = exc
        return self

    def when_authorization_header(self) -> "Scenario":
        if self._credentials is None:
            raise ValueError("Credentials must be configured before requesting header")
        self._authorization_header = self._credentials.to_authorization_header()
        return self

    def when_searching_offres(self, **kwargs: Any) -> "Scenario":
        self._offers = self._offres_facade().search(**kwargs)
        return self

    async def when_searching_offres_async(self, **kwargs: Any) -> "Scenario":
        self._offers = await self._offres_facade().search_async(**kwargs)
        return self

    def when_getting_offre(self, offer_id: str) -> "Scenario":
        self._capture_offre_result(lambda: self._offres_facade().get(offer_id))
        return self

    async def when_getting_offre_async(self, offer_id: str) -> "Scenario":
        await self._capture_offre_result_async(lambda: self._offres_facade().get_async(offer_id))
        return self

    def when_getting_metiers(self) -> "Scenario":
        self._metiers = self._offres_facade().referentiels.metiers()
        return self

    async def when_getting_metiers_async(self) -> "Scenario":
        self._metiers = await self._offres_facade().referentiels.metiers_async()
        return self

    def when_getting_appellations(self) -> "Scenario":
        self._appellations = self._offres_facade().referentiels.appellations()
        return self

    async def when_getting_appellations_async(self) -> "Scenario":
        self._appellations = await self._offres_facade().referentiels.appellations_async()
        return self

    def first_offer_id(self) -> str:
        if not self._offers:
            raise AssertionError("Expected at least one offer to be present")
        first_offer_id = self._offers[0].id
        if first_offer_id is None:
            raise AssertionError("First offer has no ID")
        return first_offer_id

    def _offres_facade(self) -> FranceTravailOffresClient:
        if self._client is not None:
            return self._client.offres
        if self._offres_client is not None:
            return self._offres_client
        raise ValueError("Offres client must be configured before this action")

    def _capture_offre_result(self, action) -> None:  # type: ignore[no-untyped-def]
        try:
            self._offre = action()
        except Exception as exc:
            self._captured_exception = exc

    async def _capture_offre_result_async(self, action) -> None:  # type: ignore[no-untyped-def]
        try:
            self._offre = await action()
        except Exception as exc:
            self._captured_exception = exc

    def then_token_is(self, expected: Any) -> "Scenario":
        assert self._token == expected
        return self

    def then_token_has_access_token(self) -> "Scenario":
        if self._token is None:
            raise AssertionError("Expected token to be present")
        assert self._token.access_token is not None
        return self

    def then_token_expires_at(self, expected: datetime.datetime) -> "Scenario":
        if self._token is None:
            raise AssertionError("Expected token to be present")
        assert self._token.expires_at == expected
        return self

    def then_token_scope_is(self, expected: Any) -> "Scenario":
        if self._token is None:
            raise AssertionError("Expected token to be present")
        assert self._token.scope == expected
        return self

    def then_token_type_is(self, expected: str) -> "Scenario":
        if self._token is None:
            raise AssertionError("Expected token to be present")
        assert self._token.token_type == expected
        return self

    def then_authorization_header_is(self, expected: dict[str, str]) -> "Scenario":
        if self._authorization_header is None:
            raise AssertionError("Expected authorization header to be present")
        assert self._authorization_header == expected
        return self

    def then_exception_is(self, exception_type: type[Exception], match: str) -> "Scenario":
        if self._captured_exception is None:
            raise AssertionError("Expected exception to be captured")
        assert isinstance(self._captured_exception, exception_type)
        assert match in str(self._captured_exception)
        return self

    def then_all_offers_are(self, expected_type: type) -> "Scenario":
        if self._offers is None:
            raise AssertionError("Expected offers to be present")
        assert all(isinstance(offer, expected_type) for offer in self._offers)
        return self

    def then_offres_should_be_equal(self, expected: list[Any]) -> "Scenario":
        if self._offers is None:
            raise AssertionError("Expected offers to be present")
        assert self._offers == expected
        return self

    def then_offre_should_be(self, expected: Offre) -> "Scenario":
        if self._offre is None:
            raise AssertionError("Expected offre to be present")
        assert self._offre == expected
        return self

    def then_offre_should_be_instance_of(self, expected_type: type) -> "Scenario":
        if self._offre is None:
            raise AssertionError("Expected offre to be present")
        assert isinstance(self._offre, expected_type)
        return self

    def then_all_metiers_are(self, expected_type: type) -> "Scenario":
        if self._metiers is None:
            raise AssertionError("Expected metiers to be present")
        assert all(isinstance(metier, expected_type) for metier in self._metiers)
        return self

    def then_metiers_should_be_equal(self, expected: list[Any]) -> "Scenario":
        if self._metiers is None:
            raise AssertionError("Expected metiers to be present")
        assert self._metiers == expected
        return self

    def then_appellations_should_be_equal(self, expected: list[Any]) -> "Scenario":
        if self._appellations is None:
            raise AssertionError("Expected appellations to be present")
        assert self._appellations == expected
        return self

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            return
        if isinstance(self._http_client, HttpClient):
            self._http_client.close()

    async def close_async(self) -> None:
        if self._client is not None:
            await self._client.close_async()
            return
        if isinstance(self._http_client, HttpClient):
            await self._http_client.close_async()

    def __enter__(self) -> "Scenario":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


def scenario() -> Scenario:
    return Scenario()
