import requests
from elasticsearch import Elasticsearch

# Connexion à l'instance ElasticSearch
es = Elasticsearch(hosts="http://elastic:changeme@localhost:9200/")

# URL de l'API pour récupérer les données

url_api = "https://recherche-entreprises.api.gouv.fr/search"

# Fonction pour récupérer le nombre total de pages
def get_total_pages(url_api):
    url = (url_api +
           "?region=93")
    donnees = requests.get(url).json()
    total_pages = donnees["total_pages"]
    return total_pages

# Fonction pour insérer les données dans ElasticSearch
def result_per_page(url_api, total_pages):
    page = 1
    while page <= total_pages:  # Boucle pour parcourir toutes les pages de l'API et insérer les données dans ElasticSearch
        url = (url_api +
               "?region=93"
               f"&page={page}")

        donnees = requests.get(url).json()

        es.index(index="company", body=donnees)
        page += 1  # Incrémentation de la page pour passer à la suivante

# Appel des fonctions
result_per_page(url_api, get_total_pages(url_api))
