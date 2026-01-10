from france_travail_api._url import FranceTravailUrl


def test_should_convert_snake_case_to_camel_case() -> None:
    """Snake_case parameters should be converted to camelCase in URL."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(
        mots_cles="test",
        code_rome="M1805",
        secteur_activite="62",
        acces_travailleur_handicape=True,
    )

    assert "motsCles=test" in url
    assert "codeRome=M1805" in url
    assert "secteurActivite=62" in url
    assert "accesTravailleurHandicape=true" in url


def test_should_handle_single_word_parameters() -> None:
    """Single-word parameters should remain lowercase."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(sort="1", domaine="M18")

    assert "sort=1" in url
    assert "domaine=M18" in url


def test_should_transform_boolean_to_lowercase_string() -> None:
    """Boolean values should be converted to "true"/"false" strings."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(
        temps_plein=True,
        inclure_limitrophes=False,
        accessible=True,
    )

    assert "tempsPlein=true" in url
    assert "inclureLimitrophes=false" in url
    assert "accessible=true" in url


def test_should_transform_integers_to_string() -> None:
    """Integer values should be converted to strings."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(
        origine_offre=1,
        distance=10,
        publiee_depuis=7,
        count=0,
    )

    assert "origineOffre=1" in url
    assert "distance=10" in url
    assert "publieeDepuis=7" in url
    assert "count=0" in url


def test_should_keep_strings_unchanged() -> None:
    """String values should pass through unchanged."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(
        type_contrat="CDI",
        qualification="cadre",
        code="ABC123",
    )

    assert "typeContrat=CDI" in url
    assert "qualification=cadre" in url
    assert "code=ABC123" in url


def test_should_handle_special_mappings() -> None:
    """Special mappings should override default camelCase conversion."""
    url_builder = FranceTravailUrl(
        "https://api.example.com",
        special_mappings={
            "code_rome": "codeROME",  # All caps ROME
            "code_naf": "codeNAF",  # All caps NAF
            "range_param": "range",  # Python keyword
        },
    )

    url = url_builder.build(
        code_rome="M1805",
        code_naf="62.02A",
        range_param="0-149",
        mots_cles="test",  # Standard camelCase for unmapped params
    )

    assert "codeROME=M1805" in url
    assert "codeNAF=62.02A" in url
    assert "range=0-149" in url
    assert "motsCles=test" in url


def test_should_build_url_with_only_required_parameter() -> None:
    """Should build URL with a single parameter."""
    url_builder = FranceTravailUrl("https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search")

    url = url_builder.build(mots_cles="développeur python")

    assert url == "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search?motsCles=développeur python"


def test_should_ignore_none_parameters() -> None:
    """None values should be excluded from the URL."""
    url_builder = FranceTravailUrl("https://api.example.com")

    url = url_builder.build(
        mots_cles="développeur",
        sort=None,
        domaine="M18",
        commune=None,
    )

    assert "motsCles=développeur" in url
    assert "domaine=M18" in url
    assert "sort" not in url
    assert "commune" not in url


def test_should_build_url_with_france_travail_special_mappings() -> None:
    """France Travail API uses special mappings for ROME, NAF, MRS codes."""
    url_builder = FranceTravailUrl(
        "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search",
        special_mappings={
            "code_rome": "codeROME",
            "code_naf": "codeNAF",
            "offres_mrs": "offresMRS",
        },
    )

    url = url_builder.build(
        mots_cles="développeur python",
        code_rome="M1805,M1810",
        code_naf="62.02A",
        offres_mrs=True,
    )

    assert "motsCles=développeur python" in url
    assert "codeROME=M1805,M1810" in url
    assert "codeNAF=62.02A" in url
    assert "offresMRS=true" in url


def test_should_handle_all_parameter_types_together() -> None:
    """Test comprehensive URL building with mixed parameter types."""
    url_builder = FranceTravailUrl("https://api.example.com/search")

    url = url_builder.build(
        mots_cles="développeur python",
        sort="1",
        commune="75056",
        distance=10,
        temps_plein=True,
        type_contrat="CDI",
    )

    assert "motsCles=développeur python" in url
    assert "sort=1" in url
    assert "commune=75056" in url
    assert "distance=10" in url
    assert "tempsPlein=true" in url
    assert "typeContrat=CDI" in url


def test_should_accept_custom_base_url() -> None:
    """Different APIs can use different base URLs."""
    url_builder = FranceTravailUrl("https://custom-api.example.com/v3/search")

    url = url_builder.build(mots_cles="test", sort="1")

    assert url.startswith("https://custom-api.example.com/v3/search?")
    assert "motsCles=test" in url
    assert "sort=1" in url


def test_should_work_with_completely_different_api() -> None:
    """Test that the builder works with any API using custom mappings."""
    url_builder = FranceTravailUrl(
        "https://api.example.com/search",
        special_mappings={
            "query": "q",  # Short form
            "max_results": "limit",  # Different name
        },
    )

    url = url_builder.build(
        query="python",
        max_results=10,
        user_name="john",  # Standard camelCase for unmapped
    )

    assert "q=python" in url
    assert "limit=10" in url
    assert "userName=john" in url
    assert "maxResults" not in url  # Mapped to "limit"
