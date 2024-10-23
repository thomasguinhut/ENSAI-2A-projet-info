import requests

from typing import List

from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.ingredient import Ingredient


class RecetteClient:

    """

    Création de classe RecetteClient.

    Cette classe, qui ne contient que des méthodes, fait le lien entre
    l'API et l'application. Elle récupère les infos disponibles sous format
    JSON pour les transformer en objet Python, ici une liste de dictionnaires
    avec un dictionnaire par recette.

    """

    def __init__(self) -> None:
        pass

    def get_recette(self) -> List[dict[
            str, str, str, Origine, Categorie, List[Ingredient]]]:
        """

        Récupère toutes les recettes enregstrées dans l'API, ainsi que toutes
        leurs informations.

        Returns
        -------
        List[dict[
            id_recette: str,
            nom_recette: str,
            instructions_recette: str,
            origine_recette: Origine,
            categorie_recette: Categorie,
            ingredients_recette: list[Ingredient]
        ]]

        """

        liste_recette = []
        for letter in range(ord("a"), ord("z") + 1):
            req = requests.get(
                "https://www.themealdb.com/api/json/v1/1/search.php?f="
                f"{chr(letter)}"
            )
            recette = {}
            if req.status_code == 200:
                raw_types = req.json().get("meals")
                if raw_types:
                    for t in raw_types:
                        if t is not None:
                            recette = {}
                            recette["id_recette"] = t.get("idMeal", "")
                            recette["nom_recette"] = t.get("strMeal", "")
                            recette["instructions_recette"] = t.get(
                                "strInstructions", "")
                            recette["origine_recette"] = t.get("strArea", "")
                            recette["categorie_recette"] = t.get(
                                "strCategory", "")
                            L_ingredients = []
                            for i in range(1, 20):
                                ingredient_api = t.get(
                                    "strIngredient" + str(i), "")
                                if (ingredient_api is not None and
                                        ingredient_api != ""):
                                    L_ingredients.append(ingredient_api)
                            recette["ingredients_recette"] = L_ingredients
                            liste_recette.append(recette)
        return liste_recette
