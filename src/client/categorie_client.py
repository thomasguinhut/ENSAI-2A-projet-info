import requests

from typing import List


class CategorieClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_categorie() -> List[dict]:
        req = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php?")
        liste_categories = []
        if req.status_code == 200:
            raw_types = req.json()["categories"]
            for t in raw_types:
                categorie = {}
                categorie["id_categorie"] = t["idCategory"]
                categorie["nom_categorie"] = t["strCategory"]
                liste_categories.append(categorie)
        return liste_categories

    def get_id_categorie_by_name(nom_categorie: str) -> str:
        req = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php?")
        if req.status_code == 200:
            raw_types = req.json()["categories"]
            for t in raw_types:
                if t["strCategory"].lower() == nom_categorie.lower():
                    return t["idCategory"]
