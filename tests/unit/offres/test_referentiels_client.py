import http
import uuid

import pytest

from france_travail_api.auth.scope import Scope
from france_travail_api.http_transport._http_response import HTTPResponse
from france_travail_api.offres.models import Appellation, Metier
from tests.dsl import scenario


@pytest.fixture
def metiers_response() -> HTTPResponse:
    return HTTPResponse(
        status_code=http.HTTPStatus.OK,
        body=[
            {"code": "D1102", "libelle": "Boulangerie - viennoiserie"},
            {"code": "M1805", "libelle": "Études et développement informatique"},
        ],
        request_id=uuid.uuid4(),
        headers={},
    )


def test_should_get_metiers_from_referentiel(metiers_response: HTTPResponse) -> None:
    flow = (
        scenario()
        .unit()
        .with_token_response()
        .with_http_response(metiers_response)
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    metiers = flow._offres_client.referentiels.metiers()

    assert len(metiers) == 2
    assert metiers[0] == Metier(code="D1102", libelle="Boulangerie - viennoiserie")
    assert metiers[1] == Metier(code="M1805", libelle="Études et développement informatique")


@pytest.mark.asyncio
async def test_should_get_metiers_from_referentiel_async(metiers_response: HTTPResponse) -> None:
    flow = (
        scenario()
        .unit()
        .with_token_response()
        .with_http_response(metiers_response)
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    metiers = await flow._offres_client.referentiels.metiers_async()
    assert metiers == [
        Metier(code="D1102", libelle="Boulangerie - viennoiserie"),
        Metier(code="M1805", libelle="Études et développement informatique"),
    ]


@pytest.fixture
def appellations_response() -> HTTPResponse:
    return HTTPResponse(
        status_code=http.HTTPStatus.OK,
        body=[
            {"code": "11573", "libelle": "Boulanger / Boulangère"},
            {"code": "38444", "libelle": "Développeur / Développeuse back-end"},
        ],
        request_id=uuid.uuid4(),
        headers={},
    )


def test_should_get_appellations_from_referentiel(appellations_response: HTTPResponse) -> None:
    flow = (
        scenario()
        .unit()
        .with_token_response()
        .with_http_response(appellations_response)
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    appellations = flow._offres_client.referentiels.appellations()

    assert len(appellations) == 2
    assert appellations[0] == Appellation(code="11573", libelle="Boulanger / Boulangère")
    assert appellations[1] == Appellation(code="38444", libelle="Développeur / Développeuse back-end")


@pytest.mark.asyncio
async def test_should_get_appellations_from_referentiel_async(appellations_response: HTTPResponse) -> None:
    flow = (
        scenario()
        .unit()
        .with_token_response()
        .with_http_response(appellations_response)
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    appellations = await flow._offres_client.referentiels.appellations_async()
    assert appellations == [
        Appellation(code="11573", libelle="Boulanger / Boulangère"),
        Appellation(code="38444", libelle="Développeur / Développeuse back-end"),
    ]
