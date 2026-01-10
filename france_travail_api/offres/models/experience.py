from enum import Enum


class ExperienceExigee(Enum):
    """
    Experience exigee codes

    Attributes
    ----------
    DEBUTANT_ACCEPTE : Débutant accepté
    EXPERIENCE_SOUHAITEE : Expérience souhaitée
    EXPERIENCE_EXIGEE : Expérience exigée
    """

    DEBUTANT_ACCEPTE = "Débutant accepté"
    EXPERIENCE_SOUHAITEE = "Expérience souhaitée"
    EXPERIENCE_EXIGEE = "Expérience exigée"

    @staticmethod
    def from_code(code: str) -> "ExperienceExigee | None":
        """Parse experience exigee code to ExperienceExigee enum."""
        match code:
            case "D":
                return ExperienceExigee.DEBUTANT_ACCEPTE
            case "S":
                return ExperienceExigee.EXPERIENCE_SOUHAITEE
            case "E":
                return ExperienceExigee.EXPERIENCE_EXIGEE
            case _:
                raise ValueError(f"Unknown experience exigee code: {code}")
