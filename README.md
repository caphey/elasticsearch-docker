# elasticsearch-docker

## Présentation du projet
Ce projet a pour but la visualisation de données sur Elasticsearch. L'instance Elasticsearch est hébergée sur Docker, offrant une solution flexible et évolutive pour le stockage et la récupération des données.

![Capture d'écran du projet](elasticsearch.png)

## Fichiers
* [insert.py](https://github.com/caphey/elasticsearch-docker/blob/main/insert.py) : Ce script est responsable de la récupération des données à partir d'une API et de leur insertion dans l'instance Elasticsearch. Il utilise la bibliothèque requests pour récupérer les données et la bibliothèque elasticsearch pour interagir avec l'instance Elasticsearch.

## Comment ça marche
Le script [insert.py](https://github.com/caphey/elasticsearch-docker/blob/main/insert.py) se connecte d'abord à l'instance Elasticsearch en utilisant l'URL de l'hôte fournie. Il récupère ensuite les données de l'API à `https://recherche-entreprises.api.gouv.fr/search`. Les données sont paginées, donc le script détermine d'abord le nombre total de pages en utilisant la fonction [get_total_pages](https://github.com/caphey/elasticsearch-docker/blob/main/insert.py). Il parcourt ensuite chaque page, récupère les données et les insère dans l'instance Elasticsearch en utilisant la fonction [result_per_page](https://github.com/caphey/elasticsearch-docker/blob/main/insert.py).

## Exécution du projet
Pour exécuter le projet, il suffit d'exécuter le script [insert.py](https://github.com/caphey/elasticsearch-docker/blob/main/insert.py). Assurez-vous que votre instance `Elasticsearch` est en cours d'exécution et accessible à l'URL de l'hôte spécifiée.

## Dépendances
* Python
* Requests
* Elasticsearch
* Kibana
* Git

## Installation des instances Elasticsearch et Kibana

Ouvrez votre terminal et clonez le répertoire GitHub [docker-elk](https://github.com/deviantony/docker-elk) :
```bash
git clone https://github.com/deviantony/docker-elk
```
Modifiez les lignes suivantes dans le fichier `elasticsearch.yml` dans `elasticsearch/config/` :
```bash
xpack.license.self_generated.type: basic
xpack.security.enabled: false
```
Rendez-vous dans le répertoire cloné à l'aide de la commande `cd`, puis ordonnez à Docker de créer un groupe d'instance à partir des fichiers de configurations télechargés (il faut que Docker soit lancé et fonctionnel) :
```bash
cd docker-elk
docker-compose up setup
```
Puis, lancez les instances
```bash
docker-compose up
```
Une fois la commande terminée, vous pouvez accédez à Kibana en vous rendant à l'adresse suivante : ![http://localhost:5601](http://localhost:5601). L'identifiant par défaut est `elastic` et le mot de passe `changeme`.
