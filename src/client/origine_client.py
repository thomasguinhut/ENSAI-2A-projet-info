import requests

from typing import List


class OrigineClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_origine(self) -> List[dict]:

        # Appel du Web service
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")

        liste_origine = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            i = 1
            if raw_types:
                for t in raw_types:
                    origine = {}
                    origine["id_origine"] = i
                    origine["nom_origine"] = t["strArea"]
                    liste_origine.append(origine)
                    i += 1
        return liste_origine
