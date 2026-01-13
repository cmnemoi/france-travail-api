import pytest

from france_travail_api.offres.models.contrat import CodeTypeContrat


class TestCodeTypeContrat:
    @pytest.mark.parametrize(
        ("contrat", "expected_value"),
        [
            (CodeTypeContrat.CDI, "CDI"),
            (CodeTypeContrat.CDD, "CDD"),
            (CodeTypeContrat.MIS, "MIS"),
            (CodeTypeContrat.SAI, "SAI"),
            (CodeTypeContrat.CCE, "CCE"),
            (CodeTypeContrat.FRA, "FRA"),
            (CodeTypeContrat.LIB, "LIB"),
            (CodeTypeContrat.REP, "REP"),
            (CodeTypeContrat.TTI, "TTI"),
            (CodeTypeContrat.DDI, "DDI"),
            (CodeTypeContrat.DIN, "DIN"),
            (CodeTypeContrat.DDT, "DDT"),
        ],
    )
    def test_to_api_value(self, contrat: CodeTypeContrat, expected_value: str) -> None:
        assert contrat.to_api_value() == expected_value
