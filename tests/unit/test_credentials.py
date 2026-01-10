import datetime
import http
import uuid

import pytest

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth._token import Token
from france_travail_api.auth.scope import Scope
from france_travail_api.exceptions import FranceTravailException
from france_travail_api.http_transport._http_response import HTTPResponse
from tests.test_doubles.fake_http_client import FakeHttpClient

NOW = datetime.datetime(2025, 12, 25, 10, 0, 0, tzinfo=datetime.UTC)


def test_should_return_token() -> None:
    http_client = FakeHttpClient()
    http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )
    credentials = FranceTravailCredentials(
        client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES], http_client=http_client
    )

    assert credentials.get_token(NOW) == Token(
        access_token="my_token",
        expires_at=NOW + datetime.timedelta(seconds=1_499),
        scope="api_offresdemploiv2 o2dsoffre",
        token_type="Bearer",
    )


def test_should_return_cached_token_if_not_expired() -> None:
    http_client = FakeHttpClient()
    http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token1",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )
    http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token2",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )
    credentials = FranceTravailCredentials(
        client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES], http_client=http_client
    )

    credentials.get_token(NOW)
    token = credentials.get_token(NOW)
    assert token == Token(
        access_token="my_token1",
        expires_at=NOW + datetime.timedelta(seconds=1_499),
        scope="api_offresdemploiv2 o2dsoffre",
        token_type="Bearer",
    )


def test_should_raise_base_exception_when_http_client_returns_error() -> None:
    http_client = FakeHttpClient()
    http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            body={"error": "unknown_error", "error_description": "An unknown error occurred"},
            headers={},
            request_id=uuid.uuid4(),
        )
    )

    with pytest.raises(
        FranceTravailException,
        match="An error occurred while communicating with the France Travail API: An unknown error occurred",
    ):
        FranceTravailCredentials(
            client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES], http_client=http_client
        ).get_token()


def test_should_return_authorization_header() -> None:
    http_client = FakeHttpClient()
    http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )

    authorization_header = FranceTravailCredentials(
        client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES], http_client=http_client
    ).to_authorization_header()

    assert authorization_header == {"Authorization": "Bearer my_token"}
