import requests

from typing import List


class IngredientClient:

    """

    Création de classe IngredientClient.

    Cette classe, qui ne contient que des méthodes, fait le lien entre
    l'API et l'application. Elle récupère les infos disponibles sous format
    JSON pour les transformer en objet Python, ici une liste de dictionnaire
    avec un dictionnaire par ingrédient.

    """

    def __init__(self) -> None:
        pass

    def get_ingredient(self) -> List[dict[str, str]]:
        """

        Récupère toutes les ingrédients enregstrées dans l'API.

        Returns
        -------
        List[dict[id_ingredient: str, nom_ingredient: str]]

        """

        req = requests.get(
            "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
        )
        liste_ingredients = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                ingredient = {}
                ingredient["id_ingredient"] = t["idIngredient"]
                ingredient["nom_ingredient"] = t["strIngredient"]
                liste_ingredients.append(ingredient)
        return liste_ingredients

    def get_id_ingredient_by_name(nom_ingredient: str) -> str:
        """

        Donne l'id de l'ingrédient à partir de son nom.

        Parameters
        ----------
        nom_ingredient : str

        Returns
        -------
        str
            id de l'ingrédient recherché

        Raises
        ------
        TypeError
            nom_ingredient doit être un str

        """

        if not isinstance(nom_ingredient, str):
            raise TypeError("nom_ingredient doit être un str")

        req = requests.get(
            "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
        )
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                if t["strIngredient"].lower() == nom_ingredient.lower():
                    return t["idIngredient"]
