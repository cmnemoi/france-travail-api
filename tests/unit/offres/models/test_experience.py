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


@pytest.mark.parametrize(
    ("experience", "expected_api_value"),
    [
        (ExperienceExigee.DEBUTANT_ACCEPTE, "D"),
        (ExperienceExigee.EXPERIENCE_SOUHAITEE, "S"),
        (ExperienceExigee.EXPERIENCE_EXIGEE, "E"),
    ],
)
def test_to_api_value_should_return_correct_code(experience: ExperienceExigee, expected_api_value: str) -> None:
    result = experience.to_api_value()
    assert result == expected_api_value
