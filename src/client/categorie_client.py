import requests

from typing import List


class CategorieClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_categorie(self) -> List[str]:

        # Appel du Web service
        req = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php?")
        categories = {}
        if req.status_code == 200:
            raw_types = req.json()["categories"]
            for t in raw_types:
                categories[t["idCategory"]] = t["strCategory"]

        return categories
