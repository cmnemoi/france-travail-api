import pytest

from france_travail_api.offres.models.experience import ExperienceExigee


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("D", ExperienceExigee.DEBUTANT_ACCEPTE),
        ("S", ExperienceExigee.EXPERIENCE_SOUHAITEE),
        ("E", ExperienceExigee.EXPERIENCE_EXIGEE),
    ],
)
def test_from_code_should_return_correct_experience(code: str, expected: ExperienceExigee) -> None:
    result = ExperienceExigee.from_code(code)
    assert result == expected


@pytest.mark.parametrize("invalid_code", ["X", "INVALID", "123", ""])
def test_from_code_should_return_none_when_code_is_unknown(invalid_code: str) -> None:
    with pytest.raises(ValueError, match=f"Unknown experience exigee code: {invalid_code}"):
        ExperienceExigee.from_code(invalid_code)
