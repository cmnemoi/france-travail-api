import datetime
import os

import pytest

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth.scope import Scope
from france_travail_api.http_transport._http_client import HttpClient

NOW = datetime.datetime(2025, 12, 25, 10, 0, 0, tzinfo=datetime.UTC)


@pytest.mark.integration
def test_should_return_token() -> None:
    credentials = FranceTravailCredentials(
        client_id=os.environ["FRANCE_TRAVAIL_CLIENT_ID"],
        client_secret=os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"],
        scopes=[Scope.OFFRES],
        http_client=HttpClient(),
    )

    token = credentials.get_token(NOW)

    assert token.access_token is not None
    assert token.expires_at == NOW + datetime.timedelta(seconds=1_499)
    assert token.scope == Scope.OFFRES
    assert token.token_type == "Bearer"


@pytest.mark.integration
def test_should_raise_exception_if_client_id_or_secret_are_invalid() -> None:
    with pytest.raises(Exception, match="Your France Travail client ID or secret are invalid"):
        FranceTravailCredentials(
            client_id="invalid-client-id",
            client_secret="invalid-client-secret",
            scopes=[Scope.OFFRES],
            http_client=HttpClient(),
        ).get_token()
