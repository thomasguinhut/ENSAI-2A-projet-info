import os
import requests

from typing import List


class IngredientClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_ingredient(self) -> List[str]:

        # Appel du Web service
        req = requests.get("www.themealdb.com/api/json/v1/1/list.php?i=list")
        ingredients = {}
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                ingredients[t["idIngredient"]] = t["strIngredient"]

        return ingredients
