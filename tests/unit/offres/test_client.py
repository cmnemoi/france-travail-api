import datetime
import http
import uuid

from france_travail_api.auth._credentials import FranceTravailCredentials
from france_travail_api.auth.scope import Scope
from france_travail_api.http_transport._http_response import HTTPResponse
from france_travail_api.offres._client import FranceTravailOffresClient
from france_travail_api.offres.models import (
    CodeOrigineOffre,
    CodeTypeContrat,
    Competence,
    Contact,
    ContexteTravail,
    Entreprise,
    Exigence,
    ExperienceExigee,
    Formation,
    Langue,
    LieuTravail,
    Offre,
    OrigineOffre,
    Permis,
    Salaire,
)
from france_travail_api.offres.models.agence import Agence
from tests.test_doubles.fake_http_client import FakeHttpClient


def test_should_search_job_offers() -> None:
    fake_http_client = FakeHttpClient()
    fake_http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )
    fake_http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.PARTIAL_CONTENT,
            body={
                "resultats": [
                    {
                        "id": "201WLXK",
                        "intitule": "Développeur backend Python/Django (H/F)",
                        "description": "Vous rejoindrez un environnement dynamique et stimulant, où la qualité des solutions techniques et l'impact concret de votre travail sont essentiels.\n\nLe poste nécessite un renfort rapide, avec des missions variées et techniques qui demandent autonomie, rigueur et collaboration.\n\n\nEn tant que Développeur backend Python/Django, vos missions seront de : \n\n * Concevoir et développer des applications backend robustes et évolutives\n * Maintenir et faire évoluer des solutions existantes, notamment autour d'un ERP (Odoo)\n * Diagnostiquer et résoudre des problématiques techniques et opérationnelles\n * Collaborer avec les équipes métiers pour assurer la qualité et la pertinence des solutions\n * Participer à l'évolution du modèle de données et à l'architecture technique\n * Proposer des optimisations et bonnes pratiques pour le backend\n\n * 4 à 5 ans d'expérience minimum sur un poste similaire\n   \n    Vos expertises, notre force commune\n * Python (expertise attendue)\n * Django & Django REST Framework\n * Développement d'API sécurisées\n * SQL & modélisation de bases de données\n * Git / GitLab\n * Environnement Linux\n *  Connaissances en JS ou framework JS appréciées\n\n Vos qualités humaines, nos valeurs partagées\n\n * A un esprit d'équipe et un sens de l'entraide\n * Fait preuve de fiabilité, engagement et responsabilité, surtout dans un contexte chargé\n * Communique de manière claire et constructive\n * Est autonome, tout en appréciant le travail collaboratif\n * Possède une curiosité technique et une volonté de progresser",
                        "dateCreation": "2025-12-23T16:01:23.690Z",
                        "dateActualisation": "2025-12-24T09:03:02.003Z",
                        "lieuTravail": {
                            "libelle": "72 - Le Mans",
                            "latitude": 48.007462,
                            "longitude": 0.197404,
                            "codePostal": "72000",
                            "commune": "72181",
                        },
                        "romeCode": "M1855",
                        "romeLibelle": "Développeur / Développeuse web",
                        "appellationlibelle": "Développeur / Développeuse back-end",
                        "entreprise": {"nom": "HOLENEK INGENIERIE", "entrepriseAdaptee": False},
                        "typeContrat": "CDI",
                        "typeContratLibelle": "CDI",
                        "natureContrat": "Contrat travail",
                        "experienceExige": "E",
                        "experienceLibelle": "4 An(s)",
                        "salaire": {"libelle": "Annuel de 38000.0 Euros à 45000.0 Euros sur 12.0 mois"},
                        "dureeTravailLibelle": "35H/semaine\nTravail en journée",
                        "dureeTravailLibelleConverti": "Temps plein",
                        "alternance": False,
                        "contact": {
                            "coordonnees1": "https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                            "urlPostulation": "https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                        },
                        "agence": {},
                        "nombrePostes": 1,
                        "accessibleTH": False,
                        "qualificationCode": "9",
                        "qualificationLibelle": "Cadre",
                        "codeNAF": "62.02A",
                        "secteurActivite": "62",
                        "secteurActiviteLibelle": "Conseil en systèmes et logiciels informatiques",
                        "origineOffre": {
                            "origine": "1",
                            "urlOrigine": "https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
                        },
                        "offresManqueCandidats": False,
                        "contexteTravail": {"horaires": ["35H/semaine\nTravail en journée"]},
                        "entrepriseAdaptee": False,
                        "employeurHandiEngage": False,
                    },
                    {
                        "id": "201TPBN",
                        "intitule": "Informaticien - Développeur C++ / QT / Python  - (H/F)",
                        "description": "Nous recherchons un(e) Informaticien - Développeur C++ / QT / Python - H/F pour rejoindre notre équipe R&D en charge du développement et du maintien en conditions opérationnelles de l'atelier logiciel utilisé pour le développement des simulateurs dans le domaine de l'énergie.\nMissions :\n * Développement et maintenance d'applications en C++ sous Windows et Linux.\n * Utilisation des frameworks Qt et QML pour créer des interfaces utilisateur modernes et performantes.\n * Développement de scripts et d'outils en Python pour automatiser des tâches et améliorer l'efficacité des processus.\n * Gestion de la configuration et du versionnage des projets à l'aide de GitLab.\n * Collaboration avec des équipes pluridisciplinaires pour comprendre les besoins des utilisateurs et proposer des solutions techniques adaptées.\n * Participation à la conception et à l'architecture des logiciels, en veillant à leur évolutivité et à leur maintenabilité.\n * Documentation des développements et des processus pour assurer une bonne traçabilité et faciliter la prise en main (en anglais).\n * Résolution des problèmes techniques et optimisation des performances des applications.\nEnjeux :\n * Contribuer à la création de solutions logicielles de haute qualité, répondant aux besoins des clients et aux exigences techniques.\n * Participer à l'amélioration continue des processus de développement et des outils utilisés.\n * S'intégrer dans une équipe dynamique et collaborative, où l'entraide et la confiance sont des valeurs fondamentales.\n\nFormation : Diplôme d'ingénieur ou équivalent en informatique, ou expérience professionnelle équivalente.\n\nExpérience : Expérience significative en développement logiciel en C++ et Python, ainsi qu'une bonne connaissance des frameworks Qt et QML.\n\nCompétences techniques : \n\n * Maîtrise des langages de programmation C++ et Python.\n * Expérience avec les frameworks Qt et QML pour le développement d'interfaces utilisateur.\n * Connaissance des systèmes d'exploitation Windows et Linux.\n * Expérience avec les outils de gestion de version, notamment GitLab.\n * Capacité à développer des scripts et des outils pour automatiser des tâches.\n * Connaissance des bonnes pratiques de développement logiciel, notamment en matière de qualité, de robustesse et de maintenabilité.\nCompétences transversales : \n * Capacité à travailler en équipe et à collaborer avec des équipes pluridisciplinaires.\n * Bonne communication écrite et orale en anglais.\n * Sens de l'organisation et respect des délais.\n * Capacité à résoudre des problèmes techniques complexes.\n * Créativité et esprit d'innovation pour proposer des solutions techniques adaptées.\n * Rigueur et attention aux détails.\n * Autonomie et capacité à prendre des initiatives.\n * Curiosité et volonté d'apprendre.\n * Sens du service et orientation client.\n\nDate de début : Dès que possible\n\nType d'emploi : CDI\n\nLieu : Grenoble\n\nRejoignez CORYS, une entreprise à taille humaine, agile, dynamique, de haute technicité, pour travailler en convivialité avec des collaborateurs, qui partagent un esprit d'équipe dynamique basé sur l'entraide et la confiance, et sur des métiers passionnants qui génèrent expériences enrichissantes et opportunités internes.\n\nLes avantages Corys :\n * 3 modes de restaurations subventionnées + boissons chaudes gratuites\n * Prime d'intéressement\n * Compte Epargne Temps\n * Prise en charge des abonnements transport en commun \n * Comité Sociale et Economique dynamique\n * Télétravail...",
                        "dateCreation": "2025-12-19T21:01:24.323Z",
                        "dateActualisation": "2025-12-22T09:00:45.080Z",
                        "lieuTravail": {
                            "libelle": "38 - Grenoble",
                            "latitude": 45.18637,
                            "longitude": 5.711296,
                            "codePostal": "38000",
                            "commune": "38185",
                        },
                        "romeCode": "M1841",
                        "romeLibelle": "Ingénieur informaticien / Ingénieure informaticienne",
                        "appellationlibelle": "Ingénieur informaticien / Ingénieure informaticienne",
                        "entreprise": {"nom": "CORYS", "entrepriseAdaptee": False},
                        "typeContrat": "CDI",
                        "typeContratLibelle": "CDI",
                        "natureContrat": "Contrat travail",
                        "experienceExige": "E",
                        "experienceLibelle": "2 An(s) - Sur même type de poste",
                        "experienceCommentaire": "Sur même type de poste",
                        "salaire": {"libelle": "Annuel de 38000.0 Euros à 43000.0 Euros sur 13.0 mois"},
                        "dureeTravailLibelle": "35H/semaine\nTravail en journée",
                        "dureeTravailLibelleConverti": "Temps plein",
                        "alternance": False,
                        "contact": {
                            "coordonnees1": "https://taleez.com/apply/informaticien-developpeur-c-qt-python-h-f-grenoble-corys-cdi/applying",
                            "urlPostulation": "https://taleez.com/apply/informaticien-developpeur-c-qt-python-h-f-grenoble-corys-cdi/applying",
                        },
                        "agence": {
                            "telephone": "06 12 34 56 78",
                            "courriel": "Pour postuler, utiliser le lien suivant : https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
                        },
                        "nombrePostes": 1,
                        "accessibleTH": False,
                        "qualificationCode": "9",
                        "qualificationLibelle": "Cadre",
                        "codeNAF": "62.02A",
                        "secteurActivite": "62",
                        "secteurActiviteLibelle": "Conseil en systèmes et logiciels informatiques",
                        "trancheEffectifEtab": "200 à 249 salariés",
                        "origineOffre": {
                            "origine": "1",
                            "urlOrigine": "https://candidat.francetravail.fr/offres/recherche/detail/201TPBN",
                        },
                        "offresManqueCandidats": False,
                        "contexteTravail": {"horaires": ["35H/semaine\nTravail en journée"]},
                        "entrepriseAdaptee": False,
                        "employeurHandiEngage": False,
                        "formations": [
                            {
                                "codeFormation": "21538",
                                "domaineLibelle": "boulangerie",
                                "niveauLibelle": "CAP, BEP et équivalents",
                                "commentaire": "Mention bien souhaitée",
                                "exigence": "E",
                            }
                        ],
                        "langues": [
                            {
                                "libelle": "Anglais",
                                "exigence": "E",
                            }
                        ],
                        "permis": [
                            {
                                "libelle": "B - Véhicule léger",
                                "exigence": "S",
                            }
                        ],
                        "outilsBureautiques": ["Jira"],
                        "competences": [
                            {
                                "code": "483320",
                                "libelle": "Faire preuve d'autonomie",
                                "exigence": "E",
                            }
                        ],
                    },
                ],
                "filtresPossibles": [
                    {
                        "filtre": "typeContrat",
                        "agregation": [
                            {"valeurPossible": "CDD", "nbResultats": 245},
                            {"valeurPossible": "CDI", "nbResultats": 2682},
                        ],
                    },
                    {
                        "filtre": "experience",
                        "agregation": [
                            {"valeurPossible": "4", "nbResultats": 943},
                            {"valeurPossible": "3", "nbResultats": 502},
                        ],
                    },
                    {
                        "filtre": "qualification",
                        "agregation": [
                            {"valeurPossible": "9", "nbResultats": 497},
                            {"valeurPossible": "X", "nbResultats": 2268},
                        ],
                    },
                    {
                        "filtre": "natureContrat",
                        "agregation": [
                            {"valeurPossible": "E1", "nbResultats": 2888},
                            {"valeurPossible": "E2", "nbResultats": 117},
                        ],
                    },
                ],
            },
            request_id=uuid.uuid4(),
            headers={},
        )
    )

    credentials = FranceTravailCredentials(
        client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES], http_client=fake_http_client
    )

    job_offers = FranceTravailOffresClient(credentials, fake_http_client)
    offers = job_offers.search(mots_cles="développeur python")

    assert offers == [
        Offre(
            id="201WLXK",
            intitule="Développeur backend Python/Django (H/F)",
            description="Vous rejoindrez un environnement dynamique et stimulant, où la qualité des solutions techniques et l'impact concret de votre travail sont essentiels.\n\nLe poste nécessite un renfort rapide, avec des missions variées et techniques qui demandent autonomie, rigueur et collaboration.\n\n\nEn tant que Développeur backend Python/Django, vos missions seront de : \n\n * Concevoir et développer des applications backend robustes et évolutives\n * Maintenir et faire évoluer des solutions existantes, notamment autour d'un ERP (Odoo)\n * Diagnostiquer et résoudre des problématiques techniques et opérationnelles\n * Collaborer avec les équipes métiers pour assurer la qualité et la pertinence des solutions\n * Participer à l'évolution du modèle de données et à l'architecture technique\n * Proposer des optimisations et bonnes pratiques pour le backend\n\n * 4 à 5 ans d'expérience minimum sur un poste similaire\n   \n    Vos expertises, notre force commune\n * Python (expertise attendue)\n * Django & Django REST Framework\n * Développement d'API sécurisées\n * SQL & modélisation de bases de données\n * Git / GitLab\n * Environnement Linux\n *  Connaissances en JS ou framework JS appréciées\n\n Vos qualités humaines, nos valeurs partagées\n\n * A un esprit d'équipe et un sens de l'entraide\n * Fait preuve de fiabilité, engagement et responsabilité, surtout dans un contexte chargé\n * Communique de manière claire et constructive\n * Est autonome, tout en appréciant le travail collaboratif\n * Possède une curiosité technique et une volonté de progresser",
            date_creation=datetime.datetime(2025, 12, 23, 16, 1, 23, 690000, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 12, 24, 9, 3, 2, 3000, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="72 - Le Mans",
                latitude=48.007462,
                longitude=0.197404,
                code_postal="72000",
                commune="72181",
            ),
            rome_code="M1855",
            rome_libelle="Développeur / Développeuse web",
            appellation_libelle="Développeur / Développeuse back-end",
            entreprise=Entreprise(nom="HOLENEK INGENIERIE", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="4 An(s)",
            experience_commentaire=None,
            formations=[],
            langues=[],
            permis=[],
            outils_bureautiques=[],
            competences=[],
            salaire=Salaire(libelle="Annuel de 38000.0 Euros à 45000.0 Euros sur 12.0 mois"),
            duree_travail_libelle="35H/semaine\nTravail en journée",
            duree_travail_libelle_converti="Temps plein",
            complement_exercice=None,
            condition_exercice=None,
            alternance=False,
            contact=Contact(
                coordonnees1="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                url_postulation="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
            ),
            agence=None,
            nombre_postes=1,
            accessible_th=False,
            deplacement_code=None,
            deplacement_libelle=None,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.02A",
            secteur_activite="62",
            secteur_activite_libelle="Conseil en systèmes et logiciels informatiques",
            qualites_professionnelles=[],
            tranche_effectif_etab=None,
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine\nTravail en journée"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        ),
        Offre(
            id="201TPBN",
            intitule="Informaticien - Développeur C++ / QT / Python  - (H/F)",
            description="Nous recherchons un(e) Informaticien - Développeur C++ / QT / Python - H/F pour rejoindre notre équipe R&D en charge du développement et du maintien en conditions opérationnelles de l'atelier logiciel utilisé pour le développement des simulateurs dans le domaine de l'énergie.\nMissions :\n * Développement et maintenance d'applications en C++ sous Windows et Linux.\n * Utilisation des frameworks Qt et QML pour créer des interfaces utilisateur modernes et performantes.\n * Développement de scripts et d'outils en Python pour automatiser des tâches et améliorer l'efficacité des processus.\n * Gestion de la configuration et du versionnage des projets à l'aide de GitLab.\n * Collaboration avec des équipes pluridisciplinaires pour comprendre les besoins des utilisateurs et proposer des solutions techniques adaptées.\n * Participation à la conception et à l'architecture des logiciels, en veillant à leur évolutivité et à leur maintenabilité.\n * Documentation des développements et des processus pour assurer une bonne traçabilité et faciliter la prise en main (en anglais).\n * Résolution des problèmes techniques et optimisation des performances des applications.\nEnjeux :\n * Contribuer à la création de solutions logicielles de haute qualité, répondant aux besoins des clients et aux exigences techniques.\n * Participer à l'amélioration continue des processus de développement et des outils utilisés.\n * S'intégrer dans une équipe dynamique et collaborative, où l'entraide et la confiance sont des valeurs fondamentales.\n\nFormation : Diplôme d'ingénieur ou équivalent en informatique, ou expérience professionnelle équivalente.\n\nExpérience : Expérience significative en développement logiciel en C++ et Python, ainsi qu'une bonne connaissance des frameworks Qt et QML.\n\nCompétences techniques : \n\n * Maîtrise des langages de programmation C++ et Python.\n * Expérience avec les frameworks Qt et QML pour le développement d'interfaces utilisateur.\n * Connaissance des systèmes d'exploitation Windows et Linux.\n * Expérience avec les outils de gestion de version, notamment GitLab.\n * Capacité à développer des scripts et des outils pour automatiser des tâches.\n * Connaissance des bonnes pratiques de développement logiciel, notamment en matière de qualité, de robustesse et de maintenabilité.\nCompétences transversales : \n * Capacité à travailler en équipe et à collaborer avec des équipes pluridisciplinaires.\n * Bonne communication écrite et orale en anglais.\n * Sens de l'organisation et respect des délais.\n * Capacité à résoudre des problèmes techniques complexes.\n * Créativité et esprit d'innovation pour proposer des solutions techniques adaptées.\n * Rigueur et attention aux détails.\n * Autonomie et capacité à prendre des initiatives.\n * Curiosité et volonté d'apprendre.\n * Sens du service et orientation client.\n\nDate de début : Dès que possible\n\nType d'emploi : CDI\n\nLieu : Grenoble\n\nRejoignez CORYS, une entreprise à taille humaine, agile, dynamique, de haute technicité, pour travailler en convivialité avec des collaborateurs, qui partagent un esprit d'équipe dynamique basé sur l'entraide et la confiance, et sur des métiers passionnants qui génèrent expériences enrichissantes et opportunités internes.\n\nLes avantages Corys :\n * 3 modes de restaurations subventionnées + boissons chaudes gratuites\n * Prime d'intéressement\n * Compte Epargne Temps\n * Prise en charge des abonnements transport en commun \n * Comité Sociale et Economique dynamique\n * Télétravail...",
            date_creation=datetime.datetime(2025, 12, 19, 21, 1, 24, 323000, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 12, 22, 9, 0, 45, 80000, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="38 - Grenoble",
                latitude=45.18637,
                longitude=5.711296,
                code_postal="38000",
                commune="38185",
            ),
            rome_code="M1841",
            rome_libelle="Ingénieur informaticien / Ingénieure informaticienne",
            appellation_libelle="Ingénieur informaticien / Ingénieure informaticienne",
            entreprise=Entreprise(nom="CORYS", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="2 An(s) - Sur même type de poste",
            experience_commentaire="Sur même type de poste",
            formations=[
                Formation(
                    code_formation="21538",
                    domaine_libelle="boulangerie",
                    niveau_libelle="CAP, BEP et équivalents",
                    commentaire="Mention bien souhaitée",
                    exigence=Exigence.OBLIGATOIRE,
                )
            ],
            langues=[
                Langue(
                    libelle="Anglais",
                    exigence=Exigence.OBLIGATOIRE,
                )
            ],
            permis=[
                Permis(
                    libelle="B - Véhicule léger",
                    exigence=Exigence.SOUHAITE,
                )
            ],
            outils_bureautiques=["Jira"],
            competences=[
                Competence(
                    code="483320",
                    libelle="Faire preuve d'autonomie",
                    exigence=Exigence.OBLIGATOIRE,
                )
            ],
            salaire=Salaire(libelle="Annuel de 38000.0 Euros à 43000.0 Euros sur 13.0 mois"),
            duree_travail_libelle="35H/semaine\nTravail en journée",
            duree_travail_libelle_converti="Temps plein",
            complement_exercice=None,
            condition_exercice=None,
            alternance=False,
            contact=Contact(
                coordonnees1="https://taleez.com/apply/informaticien-developpeur-c-qt-python-h-f-grenoble-corys-cdi/applying",
                url_postulation="https://taleez.com/apply/informaticien-developpeur-c-qt-python-h-f-grenoble-corys-cdi/applying",
            ),
            agence=Agence(
                telephone="06 12 34 56 78",
                courriel="Pour postuler, utiliser le lien suivant : https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
            ),
            nombre_postes=1,
            accessible_th=False,
            deplacement_code=None,
            deplacement_libelle=None,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.02A",
            secteur_activite="62",
            secteur_activite_libelle="Conseil en systèmes et logiciels informatiques",
            qualites_professionnelles=[],
            tranche_effectif_etab="200 à 249 salariés",
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/201TPBN",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine\nTravail en journée"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        ),
    ]


def test_should_search_job_offers_with_additional_filters() -> None:
    fake_http_client = FakeHttpClient()
    fake_http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={
                "scope": "api_offresdemploiv2 o2dsoffre",
                "expires_in": 1_499,
                "token_type": "Bearer",
                "access_token": "my_token",
            },
            headers={},
            request_id=uuid.uuid4(),
        )
    )
    fake_http_client.add_response(
        HTTPResponse(
            status_code=http.HTTPStatus.OK,
            body={"resultats": []},
            request_id=uuid.uuid4(),
            headers={},
        )
    )

    credentials = FranceTravailCredentials(
        client_id="client-id",
        client_secret="client-secret",
        scopes=[Scope.OFFRES],
        http_client=fake_http_client,  # type: ignore
    )

    job_offers = FranceTravailOffresClient(credentials, fake_http_client)  # type: ignore
    job_offers.search(
        mots_cles="développeur python",
        sort="1",
        domaine="M18",
        commune="75056",
        departement="75",
        type_contrat="CDI",
    )

    # Vérifier que l'URL contient bien tous les paramètres
    assert fake_http_client.last_get_url is not None
    assert "motsCles=développeur python" in fake_http_client.last_get_url
    assert "sort=1" in fake_http_client.last_get_url
    assert "domaine=M18" in fake_http_client.last_get_url
    assert "commune=75056" in fake_http_client.last_get_url
    assert "departement=75" in fake_http_client.last_get_url
    assert "typeContrat=CDI" in fake_http_client.last_get_url
