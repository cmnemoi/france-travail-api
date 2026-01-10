import pytest

from france_travail_api.offres.models.exigence import Exigence


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("E", Exigence.OBLIGATOIRE),
        ("S", Exigence.SOUHAITE),
    ],
)
def test_from_code_should_return_correct_exigence(code: str, expected: Exigence) -> None:
    result = Exigence.from_code(code)
    assert result == expected


@pytest.mark.parametrize("invalid_code", ["X", "INVALID", "123", ""])
def test_from_code_should_raise_value_error_when_code_is_unknown(invalid_code: str) -> None:
    with pytest.raises(ValueError, match=f"Unknown exigence code: {invalid_code}"):
        Exigence.from_code(invalid_code)
