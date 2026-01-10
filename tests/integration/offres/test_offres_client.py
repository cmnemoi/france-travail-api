import os

import pytest

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth.scope import Scope
from france_travail_api.http_transport._http_client import HttpClient
from france_travail_api.offres._client import FranceTravailOffresClient
from france_travail_api.offres.models.offre import Offre


@pytest.mark.integration
def test_should_search_offers_with_real_http_call() -> None:
    with HttpClient() as http_client:
        credentials = FranceTravailCredentials(
            client_id=os.environ["FRANCE_TRAVAIL_CLIENT_ID"],
            client_secret=os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"],
            scopes=[Scope.OFFRES],
            http_client=http_client,
        )
        offres_client = FranceTravailOffresClient(credentials, http_client)

        offers = offres_client.search(mots_cles="développeur", departement="75", range_param="0-4")

        assert all(isinstance(offer, Offre) for offer in offers)
