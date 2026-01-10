import pytest

from france_travail_api.offres.models.exigence import Exigence
from france_travail_api.offres.models.langue import Langue


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            {
                "libelle": "Anglais",
                "exigence": "E",
            },
            Langue(
                libelle="Anglais",
                exigence=Exigence.OBLIGATOIRE,
            ),
        ),
        ({}, Langue(libelle=None, exigence=None)),
        (
            {
                "libelle": "Espagnol",
                "exigence": "S",
            },
            Langue(
                libelle="Espagnol",
                exigence=Exigence.SOUHAITE,
            ),
        ),
    ],
)
def test_from_dict_should_create_langue(data: dict, expected: Langue) -> None:
    result = Langue.from_dict(data)
    assert result == expected


@pytest.mark.parametrize("invalid_code", ["INVALID", "X", "123"])
def test_from_dict_should_raise_error_when_exigence_code_is_invalid(invalid_code: str) -> None:
    data = {
        "libelle": "Allemand",
        "exigence": invalid_code,
    }

    with pytest.raises(ValueError, match=f"Unknown exigence code: {invalid_code}"):
        Langue.from_dict(data)
