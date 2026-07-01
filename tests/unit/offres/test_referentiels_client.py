import pytest

from france_travail_api.auth.scope import Scope
from france_travail_api.offres.models import Appellation, Metier
from tests.dsl import scenario


def test_should_get_metiers_from_referentiel() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    flow.given_metiers(
        [
            Metier(code="D1102", libelle="Boulangerie - viennoiserie"),
            Metier(code="M1805", libelle="Études et développement informatique"),
        ]
    ).when_getting_metiers().then_metiers_should_be_equal(
        [
            Metier(code="D1102", libelle="Boulangerie - viennoiserie"),
            Metier(code="M1805", libelle="Études et développement informatique"),
        ]
    )


@pytest.mark.asyncio
async def test_should_get_metiers_from_referentiel_async() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    await flow.given_metiers(
        [
            Metier(code="D1102", libelle="Boulangerie - viennoiserie"),
            Metier(code="M1805", libelle="Études et développement informatique"),
        ]
    ).when_getting_metiers_async()
    flow.then_metiers_should_be_equal(
        [
            Metier(code="D1102", libelle="Boulangerie - viennoiserie"),
            Metier(code="M1805", libelle="Études et développement informatique"),
        ]
    )


def test_should_get_appellations_from_referentiel() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    flow.given_appellations(
        [
            Appellation(code="11573", libelle="Boulanger / Boulangère"),
            Appellation(code="38444", libelle="Développeur / Développeuse back-end"),
        ]
    ).when_getting_appellations().then_appellations_should_be_equal(
        [
            Appellation(code="11573", libelle="Boulanger / Boulangère"),
            Appellation(code="38444", libelle="Développeur / Développeuse back-end"),
        ]
    )


@pytest.mark.asyncio
async def test_should_get_appellations_from_referentiel_async() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    await flow.given_appellations(
        [
            Appellation(code="11573", libelle="Boulanger / Boulangère"),
            Appellation(code="38444", libelle="Développeur / Développeuse back-end"),
        ]
    ).when_getting_appellations_async()
    flow.then_appellations_should_be_equal(
        [
            Appellation(code="11573", libelle="Boulanger / Boulangère"),
            Appellation(code="38444", libelle="Développeur / Développeuse back-end"),
        ]
    )
