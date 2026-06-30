import pytest

from france_travail_api.auth.scope import Scope
from france_travail_api.offres.models import Offre
from tests.dsl import scenario


@pytest.mark.integration
def test_should_search_job_offers() -> None:
    flow = scenario().integration().with_live_credentials(scopes=[Scope.OFFRES]).with_offres_client()

    flow.when_searching_offres(mots_cles="développeur", departement="75", range_param="0-4").then_all_offers_are(Offre)

    flow.close()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_should_search_job_offers_async() -> None:
    flow = scenario().integration().with_live_credentials(scopes=[Scope.OFFRES]).with_offres_client()

    await flow.when_searching_offres_async(mots_cles="développeur", departement="75", range_param="0-4")
    flow.then_all_offers_are(Offre)

    await flow.close_async()
