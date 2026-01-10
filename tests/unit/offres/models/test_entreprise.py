import pytest

from france_travail_api.offres.models.entreprise import Entreprise


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            {
                "nom": "Boulanger austral",
                "description": "Votre nouvelle boulangerie locale",
                "logo": "https://boulanger-austral.net/logo.png",
                "url": "https://boulanger-austral.net",
                "entrepriseAdaptee": True,
            },
            Entreprise(
                nom="Boulanger austral",
                description="Votre nouvelle boulangerie locale",
                logo="https://boulanger-austral.net/logo.png",
                url="https://boulanger-austral.net",
                entreprise_adaptee=True,
            ),
        ),
        (
            {},
            Entreprise(
                nom=None,
                description=None,
                logo=None,
                url=None,
                entreprise_adaptee=None,
            ),
        ),
        (
            {
                "nom": "Boulanger austral",
                "entrepriseAdaptee": False,
            },
            Entreprise(
                nom="Boulanger austral",
                description=None,
                logo=None,
                url=None,
                entreprise_adaptee=False,
            ),
        ),
    ],
)
def test_from_dict_should_create_entreprise(data: dict, expected: Entreprise) -> None:
    result = Entreprise.from_dict(data)
    assert result == expected
