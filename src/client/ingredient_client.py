import requests

from typing import List


class IngredientClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_ingredient(self) -> List[dict]:

        # Appel du Web service
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
        liste_ingredients = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                ingredient = {}
                ingredient["id_ingredient"] = t["idIngredient"]
                ingredient["nom_ingredient"] = t["strIngredient"]
                liste_ingredients.append(ingredient)
        return liste_ingredients
