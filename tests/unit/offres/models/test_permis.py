import pytest

from france_travail_api.offres.models.exigence import Exigence
from france_travail_api.offres.models.permis import Permis


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            {
                "libelle": "B - Véhicule léger",
                "exigence": "E",
            },
            Permis(
                libelle="B - Véhicule léger",
                exigence=Exigence.OBLIGATOIRE,
            ),
        ),
        ({}, Permis(libelle=None, exigence=None)),
        (
            {
                "libelle": "C - Poids lourd",
                "exigence": "S",
            },
            Permis(
                libelle="C - Poids lourd",
                exigence=Exigence.SOUHAITE,
            ),
        ),
    ],
)
def test_from_dict_should_create_permis(data: dict, expected: Permis) -> None:
    result = Permis.from_dict(data)
    assert result == expected


@pytest.mark.parametrize("invalid_code", ["X", "INVALID", "123"])
def test_from_dict_should_raise_error_when_exigence_code_is_invalid(invalid_code: str) -> None:
    data = {
        "libelle": "A - Moto",
        "exigence": invalid_code,
    }

    with pytest.raises(ValueError, match=f"Unknown exigence code: {invalid_code}"):
        Permis.from_dict(data)
