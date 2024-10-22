import requests

from typing import List


class CategorieClient:

    """

    Création de classe CatégorieClient.

    Cette classe, qui ne contient que des méthodes, fait le lien entre
    l'API et l'application. Elle récupère les infos disponibles sous format
    JSON pour les transformer en objet Python, ici une liste de dictionnaire
    avec un dictionnaire par catégorie.

    """

    def __init__(self) -> None:
        pass

    def get_categorie(self) -> List[dict[str, str]]:
        """

        Récupère toutes les catégories enregstrées dans l'API.

        Returns
        -------
        List[dict[id_categorie: str, nom_categorie: str]]

        """
        req = requests.get(
            "https://www.themealdb.com/api/json/v1/1/categories.php?"
        )
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
        """

        Donne l'id de la catégorie à partir de son nom.

        Parameters
        ----------
        nom_categorie : str

        Returns
        -------
        str
            id de la catégorie recherchée

        Raises
        ------
        TypeError
            nom_categorie doit être un str

        """

        if not isinstance(nom_categorie, str):
            raise TypeError("nom_categorie doit être un str")

        req = requests.get(
            "https://www.themealdb.com/api/json/v1/1/categories.php?"
        )
        if req.status_code == 200:
            raw_types = req.json()["categories"]
            for t in raw_types:
                if t["strCategory"].lower() == nom_categorie.lower():
                    return t["idCategory"]
