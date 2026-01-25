from typing import Any, cast

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.http_transport._http_client import HttpClient
from france_travail_api.http_transport._http_response import HTTPResponse
from france_travail_api.offres.models.appellation import Appellation
from france_travail_api.offres.models.metier import Metier

REFERENTIEL_METIERS_API_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/referentiel/metiers"
REFERENTIEL_APPELLATIONS_API_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/referentiel/appellations"


class ReferentielsClient:
    def __init__(self, credentials: FranceTravailCredentials, http_client: HttpClient) -> None:
        self._credentials = credentials
        self._http_client = http_client

    def metiers(self) -> list[Metier]:
        """Get the ROME jobs (métiers) referential.

        Returns
        -------
        list[Metier]
            List of ROME jobs with their codes and labels

        Examples
        --------
        >>> client = FranceTravailOffresClient(credentials, http_client)
        >>> client.referentiels.metiers()
        [Metier(code="D1102", libelle="Boulangerie - viennoiserie"), ...]

        References
        ----------
        .. [1] France Travail API Documentation - Référentiel - Métiers ROME
           https://francetravail.io/produits-partages/catalogue/offres-emploi/documentation#/api-reference/operations/recupererReferentielMetiers
        """
        response = self._execute_get_request(REFERENTIEL_METIERS_API_URL)
        return self._parse_metiers_response(response)

    async def metiers_async(self) -> list[Metier]:
        """Get the ROME jobs (métiers) referential asynchronously.

        Returns
        -------
        list[Metier]
            List of ROME jobs with their codes and labels

        Examples
        --------
        >>> import asyncio
        >>> client = FranceTravailOffresClient(credentials, http_client)
        >>> asyncio.run(client.referentiels.metiers_async())
        [Metier(code="D1102", libelle="Boulangerie - viennoiserie"), ...]

        References
        ----------
        .. [1] France Travail API Documentation - Référentiel - Métiers ROME
           https://francetravail.io/produits-partages/catalogue/offres-emploi/documentation#/api-reference/operations/recupererReferentielMetiers
        """
        response = await self._execute_get_request_async(REFERENTIEL_METIERS_API_URL)
        return self._parse_metiers_response(response)

    def appellations(self) -> list[Appellation]:
        """Get the ROME appellations referential.

        Returns
        -------
        list[Appellation]
            List of ROME appellations with their codes and labels

        Examples
        --------
        >>> client = FranceTravailOffresClient(credentials, http_client)
        >>> client.referentiels.appellations()
        [Appellation(code="11573", libelle="Boulanger / Boulangère"), ...]

        References
        ----------
        .. [1] France Travail API Documentation - Référentiel - Appellations ROME
           https://francetravail.io/produits-partages/catalogue/offres-emploi/documentation#/api-reference/operations/recupererReferentielAppellations
        """
        response = self._execute_get_request(REFERENTIEL_APPELLATIONS_API_URL)
        return self._parse_appellations_response(response)

    async def appellations_async(self) -> list[Appellation]:
        """Get the ROME appellations referential asynchronously.

        Returns
        -------
        list[Appellation]
            List of ROME appellations with their codes and labels

        Examples
        --------
        >>> import asyncio
        >>> client = FranceTravailOffresClient(credentials, http_client)
        >>> asyncio.run(client.referentiels.appellations_async())
        [Appellation(code="11573", libelle="Boulanger / Boulangère"), ...]

        References
        ----------
        .. [1] France Travail API Documentation - Référentiel - Appellations ROME
           https://francetravail.io/produits-partages/catalogue/offres-emploi/documentation#/api-reference/operations/recupererReferentielAppellations
        """
        response = await self._execute_get_request_async(REFERENTIEL_APPELLATIONS_API_URL)
        return self._parse_appellations_response(response)

    def _execute_get_request(self, url: str) -> HTTPResponse:
        return self._http_client.get(
            url=url,
            headers=self._credentials.to_authorization_header(),
        )

    async def _execute_get_request_async(self, url: str) -> HTTPResponse:
        return await self._http_client.get_async(
            url=url,
            headers=self._credentials.to_authorization_header(),
        )

    def _parse_metiers_response(self, response: HTTPResponse) -> list[Metier]:
        metiers_data = cast(list[dict[str, Any]], response.body)
        return [Metier.from_dict(metier_json) for metier_json in metiers_data]

    def _parse_appellations_response(self, response: HTTPResponse) -> list[Appellation]:
        appellations_data = cast(list[dict[str, Any]], response.body)
        return [Appellation.from_dict(appellation_json) for appellation_json in appellations_data]
