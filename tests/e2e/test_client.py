import os

import pytest

from france_travail_api.auth.scope import Scope
from france_travail_api.client import FranceTravailClient
from france_travail_api.offres.models.offre import Offre


@pytest.mark.e2e
def test_should_find_job_offers() -> None:
    client_id = os.environ["FRANCE_TRAVAIL_CLIENT_ID"]
    client_secret = os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"]

    with FranceTravailClient(client_id, client_secret, scopes=[Scope.OFFRES]) as client:
        offers = client.offres.search(mots_cles="developpeur", range_param="0-2")

    assert all(isinstance(offer, Offre) for offer in offers)
