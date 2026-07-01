import datetime

import pytest

from france_travail_api.auth.scope import Scope
from france_travail_api.exceptions import OffreNotFoundException
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
from tests.dsl import scenario


def test_should_search_job_offers() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    flow.given_offers_found(
        [
            Offre(
                id="201WLXK",
                intitule="Développeur backend Python/Django (H/F)",
                description="Développement backend Python/Django dans une équipe produit.",
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
                formations=[],
                langues=[],
                permis=[],
                outils_bureautiques=[],
                competences=[],
                salaire=Salaire(libelle="Annuel de 38000.0 Euros à 45000.0 Euros sur 12.0 mois"),
                duree_travail_libelle="35H/semaine\nTravail en journée",
                duree_travail_libelle_converti="Temps plein",
                alternance=False,
                contact=Contact(
                    coordonnees1="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                    url_postulation="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                ),
                nombre_postes=1,
                accessible_th=False,
                qualification_code="9",
                qualification_libelle="Cadre",
                code_naf="62.02A",
                secteur_activite="62",
                secteur_activite_libelle="Conseil en systèmes et logiciels informatiques",
                qualites_professionnelles=[],
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
                description="Développement C++, Qt et Python dans une équipe R&D.",
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
                langues=[Langue(libelle="Anglais", exigence=Exigence.OBLIGATOIRE)],
                permis=[Permis(libelle="B - Véhicule léger", exigence=Exigence.SOUHAITE)],
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
    ).when_searching_offres(mots_cles="développeur python").then_offres_should_be_equal(
        [
            Offre(
                id="201WLXK",
                intitule="Développeur backend Python/Django (H/F)",
                description="Développement backend Python/Django dans une équipe produit.",
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
                formations=[],
                langues=[],
                permis=[],
                outils_bureautiques=[],
                competences=[],
                salaire=Salaire(libelle="Annuel de 38000.0 Euros à 45000.0 Euros sur 12.0 mois"),
                duree_travail_libelle="35H/semaine\nTravail en journée",
                duree_travail_libelle_converti="Temps plein",
                alternance=False,
                contact=Contact(
                    coordonnees1="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                    url_postulation="https://taleez.com/apply/developpeur-backend-python-django-h-f-le-mans-holenek-ingenierie-cdi/applying",
                ),
                nombre_postes=1,
                accessible_th=False,
                qualification_code="9",
                qualification_libelle="Cadre",
                code_naf="62.02A",
                secteur_activite="62",
                secteur_activite_libelle="Conseil en systèmes et logiciels informatiques",
                qualites_professionnelles=[],
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
                description="Développement C++, Qt et Python dans une équipe R&D.",
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
                langues=[Langue(libelle="Anglais", exigence=Exigence.OBLIGATOIRE)],
                permis=[Permis(libelle="B - Véhicule léger", exigence=Exigence.SOUHAITE)],
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
    )


def test_should_get_job_offer_by_id() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    flow.given_offer_found(
        Offre(
            id="048KLTP",
            intitule="Développeur Python (H/F)",
            description="Nous recherchons un développeur Python expérimenté.",
            date_creation=datetime.datetime(2025, 1, 15, 10, 0, 0, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 1, 20, 14, 30, 0, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="75 - Paris",
                latitude=48.8566,
                longitude=2.3522,
                code_postal="75001",
                commune="75056",
            ),
            rome_code="M1805",
            rome_libelle="Études et développement informatique",
            appellation_libelle="Développeur / Développeuse Python",
            entreprise=Entreprise(nom="TechCorp", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="3 An(s)",
            formations=[],
            langues=[],
            permis=[],
            outils_bureautiques=[],
            competences=[],
            salaire=Salaire(libelle="Annuel de 45000.0 Euros à 55000.0 Euros sur 12.0 mois"),
            duree_travail_libelle="35H/semaine",
            duree_travail_libelle_converti="Temps plein",
            alternance=False,
            contact=Contact(
                coordonnees1="https://example.com/apply",
                url_postulation="https://example.com/apply",
            ),
            nombre_postes=1,
            accessible_th=False,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.01Z",
            secteur_activite="62",
            secteur_activite_libelle="Programmation informatique",
            qualites_professionnelles=[],
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/048KLTP",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        )
    ).when_getting_offre(offer_id="048KLTP").then_offre_should_be(
        Offre(
            id="048KLTP",
            intitule="Développeur Python (H/F)",
            description="Nous recherchons un développeur Python expérimenté.",
            date_creation=datetime.datetime(2025, 1, 15, 10, 0, 0, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 1, 20, 14, 30, 0, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="75 - Paris",
                latitude=48.8566,
                longitude=2.3522,
                code_postal="75001",
                commune="75056",
            ),
            rome_code="M1805",
            rome_libelle="Études et développement informatique",
            appellation_libelle="Développeur / Développeuse Python",
            entreprise=Entreprise(nom="TechCorp", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="3 An(s)",
            formations=[],
            langues=[],
            permis=[],
            outils_bureautiques=[],
            competences=[],
            salaire=Salaire(libelle="Annuel de 45000.0 Euros à 55000.0 Euros sur 12.0 mois"),
            duree_travail_libelle="35H/semaine",
            duree_travail_libelle_converti="Temps plein",
            alternance=False,
            contact=Contact(
                coordonnees1="https://example.com/apply",
                url_postulation="https://example.com/apply",
            ),
            nombre_postes=1,
            accessible_th=False,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.01Z",
            secteur_activite="62",
            secteur_activite_libelle="Programmation informatique",
            qualites_professionnelles=[],
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/048KLTP",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        )
    )


def test_should_raise_exception_when_job_offer_not_found() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    flow.given_offer_not_found().when_getting_offre(offer_id="INVALID_ID").then_exception_is(
        exception_type=OffreNotFoundException, match="Job offer with ID 'INVALID_ID' not found"
    )


@pytest.mark.asyncio
async def test_should_get_job_offer_by_id_async() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    await flow.given_offer_found(
        Offre(
            id="048KLTP",
            intitule="Développeur Python (H/F)",
            description="Nous recherchons un développeur Python expérimenté.",
            date_creation=datetime.datetime(2025, 1, 15, 10, 0, 0, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 1, 20, 14, 30, 0, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="75 - Paris",
                latitude=48.8566,
                longitude=2.3522,
                code_postal="75001",
                commune="75056",
            ),
            rome_code="M1805",
            rome_libelle="Études et développement informatique",
            appellation_libelle="Développeur / Développeuse Python",
            entreprise=Entreprise(nom="TechCorp", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="3 An(s)",
            formations=[],
            langues=[],
            permis=[],
            outils_bureautiques=[],
            competences=[],
            salaire=Salaire(libelle="Annuel de 45000.0 Euros à 55000.0 Euros sur 12.0 mois"),
            duree_travail_libelle="35H/semaine",
            duree_travail_libelle_converti="Temps plein",
            alternance=False,
            contact=Contact(
                coordonnees1="https://example.com/apply",
                url_postulation="https://example.com/apply",
            ),
            nombre_postes=1,
            accessible_th=False,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.01Z",
            secteur_activite="62",
            secteur_activite_libelle="Programmation informatique",
            qualites_professionnelles=[],
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/048KLTP",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        )
    ).when_getting_offre_async(offer_id="048KLTP")
    flow.then_offre_should_be(
        Offre(
            id="048KLTP",
            intitule="Développeur Python (H/F)",
            description="Nous recherchons un développeur Python expérimenté.",
            date_creation=datetime.datetime(2025, 1, 15, 10, 0, 0, tzinfo=datetime.timezone.utc),
            date_actualisation=datetime.datetime(2025, 1, 20, 14, 30, 0, tzinfo=datetime.timezone.utc),
            lieu_travail=LieuTravail(
                libelle="75 - Paris",
                latitude=48.8566,
                longitude=2.3522,
                code_postal="75001",
                commune="75056",
            ),
            rome_code="M1805",
            rome_libelle="Études et développement informatique",
            appellation_libelle="Développeur / Développeuse Python",
            entreprise=Entreprise(nom="TechCorp", entreprise_adaptee=False),
            type_contrat=CodeTypeContrat.CDI,
            type_contrat_libelle="CDI",
            nature_contrat="Contrat travail",
            experience_exige=ExperienceExigee.EXPERIENCE_EXIGEE,
            experience_libelle="3 An(s)",
            formations=[],
            langues=[],
            permis=[],
            outils_bureautiques=[],
            competences=[],
            salaire=Salaire(libelle="Annuel de 45000.0 Euros à 55000.0 Euros sur 12.0 mois"),
            duree_travail_libelle="35H/semaine",
            duree_travail_libelle_converti="Temps plein",
            alternance=False,
            contact=Contact(
                coordonnees1="https://example.com/apply",
                url_postulation="https://example.com/apply",
            ),
            nombre_postes=1,
            accessible_th=False,
            qualification_code="9",
            qualification_libelle="Cadre",
            code_naf="62.01Z",
            secteur_activite="62",
            secteur_activite_libelle="Programmation informatique",
            qualites_professionnelles=[],
            origine_offre=OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/048KLTP",
            ),
            offres_manque_candidats=False,
            contexte_travail=ContexteTravail(horaires=["35H/semaine"]),
            entreprise_adaptee=False,
            employeur_handi_engage=False,
        )
    )


@pytest.mark.asyncio
async def test_should_raise_exception_when_job_offer_not_found_async() -> None:
    flow = (
        scenario()
        .unit()
        .with_valid_token()
        .with_credentials(client_id="client-id", client_secret="client-secret", scopes=[Scope.OFFRES])
        .with_offres_client()
    )

    await flow.given_offer_not_found().when_getting_offre_async(offer_id="INVALID_ID")
    flow.then_exception_is(exception_type=OffreNotFoundException, match="Job offer with ID 'INVALID_ID' not found")
