import os
import requests

from typing import List


class RecetteClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_recette(self) -> List[str]:

        # Appel du Web service
        liste_recette = []
        for letter in range(ord("a"), ord("z") + 1):
            req = requests.get(
                f"https://www.themealdb.com/api/json/v1/1/search.php?f={chr(letter)}"
            )
            recette = {}
            if req.status_code == 200:
                raw_types = req.json().get(
                    "meals"
                )  # Utilisation de .get() pour éviter une KeyError
                if raw_types:  # Vérification si raw_types n'est pas None ou vide
                    for t in raw_types:
                        if t is not None:
                            recette = (
                                {}
                            )  # Assure-toi que 'recette' est réinitialisé à chaque itération
                            recette["id_recette"] = t.get("idMeal", "")
                            recette["nom"] = t.get("strMeal", "")
                            recette["instructions"] = t.get("strInstructions", "")
                            recette["origine"] = t.get("strArea", "")
                            recette["categorie"] = t.get("strCategory", "")
                            L_ingredients = []
                            for i in range(1, 20):
                                ingredient_api = t.get("strIngredient" + str(i), "")
                                if ingredient_api is not None and ingredient_api != "":
                                    L_ingredients.append(ingredient_api)
                            recette["ingredients"] = L_ingredients
                            liste_recette.append(recette)
        return liste_recette
