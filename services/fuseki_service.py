
import requests

FUSEKI_URL = "http://localhost:3030/university/query"


def execute_query(sparql_query):
    response = requests.post(
        FUSEKI_URL,
        data={"query": sparql_query},
        headers={
            "Accept": "application/sparql-results+json"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()