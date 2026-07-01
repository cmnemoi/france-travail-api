import pytest

from france_travail_api.offres.models.metier import Metier
from france_travail_api.offres.models.offre import Offre
from tests.dsl import scenario


@pytest.mark.e2e
def test_should_find_job_offers() -> None:
    flow = scenario().e2e()

    flow.when_searching_offres(mots_cles="developpeur", range_param="0-2").then_all_offers_are(Offre)

    flow.close()


@pytest.mark.e2e
def test_should_get_job_offer_by_id() -> None:
    flow = scenario().e2e()

    flow.when_searching_offres(mots_cles="developpeur", range_param="0-0")
    flow.when_getting_offre(offer_id=flow.first_offer_id()).then_offre_should_be_instance_of(Offre)

    flow.close()


@pytest.mark.e2e
def test_should_get_metiers_from_referentiel() -> None:
    flow = scenario().e2e()

    flow.when_getting_metiers().then_all_metiers_are(Metier)

    flow.close()
