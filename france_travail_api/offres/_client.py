from france_travail_api._url import FranceTravailUrl
from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.http_transport._http_client import HttpClient
from france_travail_api.offres.models import Offre

JOB_OFFER_SEARCH_API_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"


class FranceTravailOffresClient:
    def __init__(self, credentials: FranceTravailCredentials, http_client: HttpClient) -> None:
        self._credentials = credentials
        self._http_client = http_client

    def search(
        self,
        mots_cles: str,
        sort: str | None = None,
        domaine: str | None = None,
        code_rome: str | None = None,
        appellation: str | None = None,
        theme: str | None = None,
        secteur_activite: str | None = None,
        code_naf: str | None = None,
        experience: str | None = None,
        type_contrat: str | None = None,
        nature_contrat: str | None = None,
        origine_offre: int | None = None,
        qualification: str | None = None,
        temps_plein: bool | None = None,
        commune: str | None = None,
        distance: int | None = None,
        departement: str | None = None,
        inclure_limitrophes: bool | None = None,
        region: str | None = None,
        pays_continent: str | None = None,
        niveau_formation: str | None = None,
        permis: str | None = None,
        salaire_min: str | None = None,
        periode_salaire: str | None = None,
        acces_travailleur_handicape: bool | None = None,
        publiee_depuis: int | None = None,
        min_creation_date: str | None = None,
        max_creation_date: str | None = None,
        offres_mrs: bool | None = None,
        experience_exigence: str | None = None,
        grand_domaine: str | None = None,
        partenaires: str | None = None,
        mode_selection_partenaires: str | None = None,
        duree_hebdo_min: str | None = None,
        duree_hebdo_max: str | None = None,
        duree_contrat_min: str | None = None,
        duree_contrat_max: str | None = None,
        duree_hebdo: str | None = None,
        offres_manque_candidats: bool | None = None,
        entreprises_adaptees: bool | None = None,
        employeurs_handi_engages: bool | None = None,
        range_param: str | None = None,
    ) -> list[Offre]:
        """Search for job offers.

        Parameters
        ----------
        mots_cles : str
            Keywords to search for
        sort : str, optional
            Sorting method: 0 (relevance), 1 (creation date), 2 (distance)
        domaine : str, optional
            Job domain code
        code_rome : str, optional
            ROME code (up to 200 values, comma-separated)
        appellation : str, optional
            ROME appellation code
        theme : str, optional
            ROME theme code
        secteur_activite : str, optional
            Activity sector (NAF division, up to 2 values)
        code_naf : str, optional
            NAF code (format 99.99X, up to 2 values)
        experience : str, optional
            Experience level: 0 (not specified), 1 (<1 year), 2 (1-3 years), 3 (>3 years)
        type_contrat : str, optional
            Contract type code
        nature_contrat : str, optional
            Contract nature code
        origine_offre : int, optional
            Offer origin: 1 (France Travail), 2 (Partner)
        qualification : str, optional
            Qualification: 0 (non-executive), 9 (executive)
        temps_plein : bool, optional
            Full-time or part-time
        commune : str, optional
            INSEE commune code (up to 5 values, comma-separated)
        distance : int, optional
            Distance radius in km around the commune
        departement : str, optional
            Department code (up to 5 values, comma-separated)
        inclure_limitrophes : bool, optional
            Include neighboring departments
        region : str, optional
            Region code
        pays_continent : str, optional
            Country or continent code
        niveau_formation : str, optional
            Education level code
        permis : str, optional
            Driving license code
        salaire_min : str, optional
            Minimum salary (requires periode_salaire)
        periode_salaire : str, optional
            Salary period: M (monthly), A (annual), H (hourly), C (per performance)
        acces_travailleur_handicape : bool, optional
            Accessible to workers with disabilities
        publiee_depuis : int, optional
            Published within last X days
        min_creation_date : str, optional
            Minimum creation date (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        max_creation_date : str, optional
            Maximum creation date (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        offres_mrs : bool, optional
            Only offers with simulation-based recruitment method
        experience_exigence : str, optional
            Experience requirement: D (beginner accepted), S (desired), E (required)
        grand_domaine : str, optional
            Major domain code
        partenaires : str, optional
            Partner codes list
        mode_selection_partenaires : str, optional
            Partner selection mode: INCLUS or EXCLU
        duree_hebdo_min : str, optional
            Minimum weekly duration (format HHMM)
        duree_hebdo_max : str, optional
            Maximum weekly duration (format HHMM)
        duree_contrat_min : str, optional
            Minimum contract duration in months (0-99)
        duree_contrat_max : str, optional
            Maximum contract duration in months (0-99)
        duree_hebdo : str, optional
            Contract duration type: 0 (not specified), 1 (full-time), 2 (part-time)
        offres_manque_candidats : bool, optional
            Filter offers difficult to fill
        entreprises_adaptees : bool, optional
            Filter adapted companies for workers with disabilities
        employeurs_handi_engages : bool, optional
            Filter employers committed to hiring workers with disabilities
        range_param : str, optional
            Pagination range (format: p-d, limited to 150 results)

        Returns
        -------
        list[Offre]
            List of job offers matching the search criteria

        Examples
        --------
        >>> client = FranceTravailOffresClient(credentials, http_client)
        >>> client.search(mots_cles="développeur python", commune="75056", distance=10, type_contrat="CDI")
        [Offre(id="201WLXK", intitule="Développeur backend Python/Django (H/F)", ...)]

        References
        ----------
        .. [1] France Travail API Documentation - Offres d'emploi - Rechercher des offres
           https://francetravail.io/produits-partages/catalogue/offres-emploi/documentation#/api-reference/operations/recupererListeOffre
        """
        params = locals().copy()
        params.pop("self")

        url = self._build_search_url(params)
        response_body = self._execute_search_request(url)
        return [Offre.from_dict(offre_json) for offre_json in response_body.get("resultats", [])]

    def _build_search_url(self, params: dict[str, str | int | bool]) -> str:
        return FranceTravailUrl(
            JOB_OFFER_SEARCH_API_URL,
            special_mappings=self._get_special_param_mappings(),
        ).build(**params)

    def _execute_search_request(self, url: str) -> dict:
        response = self._http_client.get(
            url=url,
            headers=self._credentials.to_authorization_header(),
        )
        return response.body

    def _get_special_param_mappings(self) -> dict[str, str]:
        return {
            "code_rome": "codeROME",
            "code_naf": "codeNAF",
            "offres_mrs": "offresMRS",
            "range_param": "range",  # 'range' is a Python reserved keyword
        }
