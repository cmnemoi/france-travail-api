import os

import pytest

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth.scope import Scope
from france_travail_api.http_transport._http_client import HttpClient
from france_travail_api.offres._client import FranceTravailOffresClient
from france_travail_api.offres.models import Offre


@pytest.mark.integration
def test_should_search_job_offers() -> None:
    client_id = os.environ["FRANCE_TRAVAIL_CLIENT_ID"]
    client_secret = os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"]

    with HttpClient() as http_client:
        credentials = FranceTravailCredentials(
            client_id=client_id,
            client_secret=client_secret,
            scopes=[Scope.OFFRES],
            http_client=http_client,
        )
        offres_client = FranceTravailOffresClient(credentials, http_client)

        offers = offres_client.search(mots_cles="developpeur", range_param="0-2")

    assert all(isinstance(offer, Offre) for offer in offers)
