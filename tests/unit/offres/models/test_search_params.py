import pytest

from france_travail_api.offres.models.search_params import (
    DureeHebdo,
    Experience,
    ModeSelectionPartenaires,
    OrigineOffreFilter,
    PeriodeSalaire,
    Qualification,
    Sort,
)


class TestSort:
    @pytest.mark.parametrize(
        ("sort", "expected_value"),
        [
            (Sort.PERTINENCE, "0"),
            (Sort.DATE_CREATION, "1"),
            (Sort.DISTANCE, "2"),
        ],
    )
    def test_to_api_value(self, sort: Sort, expected_value: str) -> None:
        assert sort.to_api_value() == expected_value


class TestExperience:
    @pytest.mark.parametrize(
        ("experience", "expected_value"),
        [
            (Experience.NON_PRECISE, "0"),
            (Experience.MOINS_UN_AN, "1"),
            (Experience.UN_A_TROIS_ANS, "2"),
            (Experience.PLUS_DE_TROIS_ANS, "3"),
        ],
    )
    def test_to_api_value(self, experience: Experience, expected_value: str) -> None:
        assert experience.to_api_value() == expected_value


class TestOrigineOffreFilter:
    @pytest.mark.parametrize(
        ("origine", "expected_value"),
        [
            (OrigineOffreFilter.FRANCE_TRAVAIL, "1"),
            (OrigineOffreFilter.PARTENAIRE, "2"),
        ],
    )
    def test_to_api_value(self, origine: OrigineOffreFilter, expected_value: str) -> None:
        assert origine.to_api_value() == expected_value


class TestQualification:
    @pytest.mark.parametrize(
        ("qualification", "expected_value"),
        [
            (Qualification.NON_CADRE, "0"),
            (Qualification.CADRE, "9"),
        ],
    )
    def test_to_api_value(self, qualification: Qualification, expected_value: str) -> None:
        assert qualification.to_api_value() == expected_value


class TestPeriodeSalaire:
    @pytest.mark.parametrize(
        ("periode", "expected_value"),
        [
            (PeriodeSalaire.MENSUEL, "M"),
            (PeriodeSalaire.ANNUEL, "A"),
            (PeriodeSalaire.HORAIRE, "H"),
            (PeriodeSalaire.CACHET, "C"),
        ],
    )
    def test_to_api_value(self, periode: PeriodeSalaire, expected_value: str) -> None:
        assert periode.to_api_value() == expected_value


class TestModeSelectionPartenaires:
    @pytest.mark.parametrize(
        ("mode", "expected_value"),
        [
            (ModeSelectionPartenaires.INCLUS, "INCLUS"),
            (ModeSelectionPartenaires.EXCLU, "EXCLU"),
        ],
    )
    def test_to_api_value(self, mode: ModeSelectionPartenaires, expected_value: str) -> None:
        assert mode.to_api_value() == expected_value


class TestDureeHebdo:
    @pytest.mark.parametrize(
        ("duree", "expected_value"),
        [
            (DureeHebdo.NON_PRECISE, "0"),
            (DureeHebdo.TEMPS_PLEIN, "1"),
            (DureeHebdo.TEMPS_PARTIEL, "2"),
        ],
    )
    def test_to_api_value(self, duree: DureeHebdo, expected_value: str) -> None:
        assert duree.to_api_value() == expected_value
