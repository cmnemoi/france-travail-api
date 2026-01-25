import pytest

from france_travail_api.offres.models.appellation import Appellation
from tests.dsl import expect


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            {"code": "11573", "libelle": "Boulanger / Boulangère"},
            Appellation(code="11573", libelle="Boulanger / Boulangère"),
        ),
        (
            {},
            Appellation(code=None, libelle=None),
        ),
    ],
)
def test_from_dict_should_create_appellation(data: dict, expected: Appellation) -> None:
    expect(Appellation.from_dict(data)).to_equal(expected)
