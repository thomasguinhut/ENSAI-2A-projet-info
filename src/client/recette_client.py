import requests

from typing import List


class RecetteClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_recette() -> List[dict]:
        liste_recette = []
        for letter in range(ord("a"), ord("z") + 1):
            req = requests.get(
                f"https://www.themealdb.com/api/json/v1/1/search.php?f={chr(letter)}"
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
                            recette["instructions_recette"] = t.get("strInstructions", "")
                            recette["origine_recette"] = t.get("strArea", "")
                            recette["categorie_recette"] = t.get("strCategory", "")
                            L_ingredients = []
                            for i in range(1, 20):
                                ingredient_api = t.get("strIngredient" + str(i), "")
                                if ingredient_api is not None and ingredient_api != "":
                                    L_ingredients.append(ingredient_api)
                            recette["ingredients_recette"] = L_ingredients
                            liste_recette.append(recette)
        return liste_recette
