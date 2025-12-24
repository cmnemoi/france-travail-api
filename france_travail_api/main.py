# import os

# from dotenv import load_dotenv

# from france_travail_api import FranceTravailClient

# load_dotenv()

# client_id = os.getenv("FRANCE_TRAVAIL_CLIENT_ID")
# client_secret = os.getenv("FRANCE_TRAVAIL_CLIENT_SECRET")

# if not client_id or not client_secret:
#     print("Please set FRANCE_TRAVAIL_CLIENT_ID and FRANCE_TRAVAIL_CLIENT_SECRET environment variables")
#     exit(1)

# with FranceTravailClient(client_id=client_id, client_secret=client_secret) as client:
#     print(client)
#     for offre in client.offres.search(keywords="data scientist"):
#         print(offre)
