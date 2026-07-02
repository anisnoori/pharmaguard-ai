from services.api import fetch_drugs, simplify_drug

from database.database import save_api_drug

def sync_drugs():

    drugs = fetch_drugs(50)

    for drug in drugs:

        item = simplify_drug(drug)

        save_api_drug(

            item["application_number"],

            item["brand"],

            item["manufacturer"]

        )

    return len(drugs)