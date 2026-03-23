# MON_API_BLOG
Une API REST pour la gestion d'articles de blog, construite avec **FastAPI** et **SQLAlchemy**, connectée à une base de données **MySQL**.

---

## Fonctionnalités

- Créer un article
- Lister tous les articles
- Récupérer un article par son ID
- Modifier un article
- Supprimer un article
- **Rechercher** des articles par mot-clé (titre ou contenu)
- **Filtrer** des articles par catégorie

## Stack technique

| Composant       | Technologie               |
| --------------- | ------------------------- |
| Framework       | FastAPI 0.111.1           |
| Serveur ASGI    | Uvicorn 0.23.2            |
| ORM             | SQLAlchemy 2.0.22         |
| Base de données | MySQL (via PyMySQL 1.1.1) |
| Validation      | Pydantic 2.5.1            |


## Structure du projet

```
MON_API_BLOG/
├── main.py           # Points d'entrée de l'API (routes)
├── models.py         # Modèle SQLAlchemy (table Article)
├── shemas.py         # Schémas Pydantic (validation des données)
├── database.py       # Connexion à la base de données
└── requirements.txt  # Dépendances Python
```


## Installation & lancement

### 1. Prérequis

- Python 3.10+
- MySQL installé et en cours d'exécution
- Une base de données nommée `blog` créée dans MySQL

```sql
CREATE DATABASE blog;
```

### 2. Cloner le projet

```bash
git clone <url-du-repo>
cd MON_API_BLOG
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

Dans `database.py`, ajuste l'URL de connexion selon ton environnement :

```python
DATABASE_URL = "mysql+pymysql://root@localhost:3306/blog"
# Format : mysql+pymysql://<utilisateur>:<mot_de_passe>@<hôte>:<port>/<nom_bdd>
```

### 5. Lancer le serveur

```bash
uvicorn main:app --reload
```

L'API sera disponible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

La documentation interactive Swagger est accessible sur : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Endpoints

### Articles

| Méthode  | Route                         | Description                     |
| -------- | ----------------------------- | ------------------------------- |
| `POST`   | `/articles`                   | Créer un nouvel article         |
| `GET`    | `/articles`                   | Lister tous les articles        |
| `GET`    | `/articles/{id}`              | Récupérer un article par son ID |
| `PUT`    | `/articles/{id}`              | Modifier un article existant    |
| `DELETE` | `/articles/{id}`              | Supprimer un article            |
| `GET`    | `/articles/search?query=`     | Rechercher par mot-clé          |
| `GET`    | `/articles/filter?categorie=` | Filtrer par catégorie           |


## Modèle de données

Un **Article** contient les champs suivants :

| Champ       | Type  | Description                      |
| ----------- | ----- | -------------------------------- |
| `id`        | `int` | Identifiant unique (auto-généré) |
| `titre`     | `str` | Titre de l'article (obligatoire) |
| `contenu`   | `str` | Contenu de l'article             |
| `auteur`    | `str` | Nom de l'auteur                  |
| `categorie` | `str` | Catégorie de l'article           |
| `tags`      | `str` | Tags associés à l'article        |

### Exemple de body (POST / PUT)

```json
{
  "titre": "Mon premier article",
  "contenu": "Voici le contenu de mon article...",
  "auteur": "Alice",
  "categorie": "Tech",
  "tags": "python, fastapi, api"
}
```


## CORS

L'API accepte les requêtes depuis toutes les origines (`*`). Pour la production, il est recommandé de restreindre les origines autorisées dans `main.py` :

```python
allow_origins=["https://ton-frontend.com"]
```


## 
