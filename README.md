# France Travail API SDK (Python)

[![Continuous Integration](https://github.com/cmnemoi/france_travail_api/actions/workflows/continuous_integration.yaml/badge.svg)](https://github.com/cmnemoi/france_travail_api/actions/workflows/continuous_integration.yaml)
[![Continuous Delivery](https://github.com/cmnemoi/france_travail_api/actions/workflows/create_github_release.yaml/badge.svg)](https://github.com/cmnemoi/france_travail_api/actions/workflows/create_github_release.yaml)
[![codecov](https://codecov.io/gh/cmnemoi/france_travail_api/graph/badge.svg?token=FLAARH38AG)](https://codecov.io/gh/cmnemoi/france_travail_api)

Un SDK Python moderne et facile à utiliser pour l'API France Travail (anciennement Pôle Emploi).

## Fonctionnalités

- **Authentification gérée automatiquement** (Client Credentials Flow)
- **Support Sync et Async** unifié
- **Retry automatique** avec backoff exponentiel (gestion des 429 Too Many Requests)
- **Pagination simplifiée** (itérateurs)
- **Types forts** avec `dataclasses`
- **Architecture extensible** (support multi-API prévu)

## Installation

```bash
pip install france-travail-api
```

## Configuration

Vous avez besoin de vos identifiants Client ID et Client Secret disponibles sur le portail [France Travail](https://francetravail.io/).

Vous pouvez les fournir directement ou via des variables d'environnement :

```bash
export FRANCE_TRAVAIL_CLIENT_ID="votre_client_id"
export FRANCE_TRAVAIL_CLIENT_SECRET="votre_client_secret"
```

## Usage

### Recherche d'offres d'emploi

```python
from france_travail_api import FranceTravailClient

# Initialisation
client = FranceTravailClient(
    client_id="votre_id", 
    client_secret="votre_secret"
)

# Recherche simple
resultats = client.offres.search(motsCles="python", commune="75101")
print(f"Total offres: {resultats.total}")

for offre in resultats.offres:
    print(f"{offre.intitule} - {offre.entreprise.nom}")

# Pagination automatique (itérateur)
for offre in client.offres.search_iter(motsCles="data scientist", departement="75"):
    print(f"{offre.id}: {offre.intitule}")
```

### Async / Await

Le même client supporte les appels asynchrones :

```python
import asyncio
from france_travail_api import FranceTravailClient

async def main():
    async with FranceTravailClient() as client:
        # Recherche async
        result = await client.offres.search_async(motsCles="react")
        print(f"Trouvé {result.total} offres")
        
        # Récupération d'une offre spécifique
        if result.offres:
            offre_id = result.offres[0].id
            detail = await client.offres.get_async(offre_id)
            print(detail.description)

asyncio.run(main())
```

### Référentiels

Accédez facilement aux tables de référence (codes ROME, communes, etc.) :

```python
communes = client.offres.referentiel.communes()
metiers = client.offres.referentiel.metiers()
```

### Mode Sandbox

Pour tester sans consommer vos quotas de production :

```python
client = FranceTravailClient(sandbox=True)
# Les appels seront redirigés vers l'API de test
```

## Gestion des Erreurs

Les exceptions sont typées pour faciliter la gestion des erreurs :

```python
from france_travail_api import FranceTravailClient, RateLimitError, ResourceNotFoundError

try:
    client.offres.get("id_inexistant")
except ResourceNotFoundError:
    print("Offre introuvable")
except RateLimitError as e:
    print(f"Quota dépassé, réessayez dans {e.retry_after} secondes")
```

## License

The source code of this repository is licensed under the [Apache License 2.0](LICENSE).
