import pytest

from france_travail_api.offres.models.origine_offre import CodeOrigineOffre, OrigineOffre


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("1", CodeOrigineOffre.FRANCE_TRAVAIL),
        ("2", CodeOrigineOffre.PARTENAIRE),
    ],
)
def test_code_origine_offre_from_code_should_return_correct_value(code: str, expected: CodeOrigineOffre) -> None:
    result = CodeOrigineOffre.from_code(code)
    assert result == expected


def test_code_origine_offre_from_code_should_raise_key_error_when_code_is_invalid() -> None:
    with pytest.raises(KeyError):
        CodeOrigineOffre.from_code("INVALID")


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            {
                "origine": "1",
                "urlOrigine": "https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
            },
            OrigineOffre(
                origine=CodeOrigineOffre.FRANCE_TRAVAIL,
                url_origine="https://candidat.francetravail.fr/offres/recherche/detail/201WLXK",
                partenaires=None,
            ),
        ),
        (
            {
                "origine": "2",
                "urlOrigine": "https://partenaire.com/offre/123",
            },
            OrigineOffre(
                origine=CodeOrigineOffre.PARTENAIRE,
                url_origine="https://partenaire.com/offre/123",
                partenaires=None,
            ),
        ),
        ({}, OrigineOffre(origine=None, url_origine=None, partenaires=None)),
        (
            {"urlOrigine": "https://example.com"},
            OrigineOffre(origine=None, url_origine="https://example.com", partenaires=None),
        ),
    ],
)
def test_from_dict_should_create_origine_offre(data: dict, expected: OrigineOffre) -> None:
    result = OrigineOffre.from_dict(data)
    assert result == expected
