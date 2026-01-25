from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Appellation:
    """
    Appellation from France Travail ROME referential.

    Attributes
    ----------
    code : str | None
        Appellation ROME code (e.g., "11573" for Boulanger / Boulangère)
    libelle : str | None
        Appellation label/name (e.g., "Boulanger / Boulangère")
    """

    code: str | None = None
    libelle: str | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Appellation":
        """
        Create an Appellation from JSON data.

        Parameters
        ----------
        data : dict[str, Any]
            Dictionary containing appellation data from France Travail API

        Returns
        -------
        Appellation
            Appellation instance created from the provided data
        """
        return Appellation(
            code=data.get("code"),
            libelle=data.get("libelle"),
        )
