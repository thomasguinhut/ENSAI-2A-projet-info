import requests

from typing import List


class OrigineClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_origine() -> List[dict]:
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
        liste_origine = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            i = 1
            if raw_types:
                for t in raw_types:
                    origine = {}
                    origine["id_origine"] = str(i)
                    origine["nom_origine"] = t["strArea"]
                    liste_origine.append(origine)
                    i += 1
        return liste_origine

    def get_id_origine_by_name(nom_origine: str) -> str:
        raw_types = OrigineClient.get_origine()
        for t in raw_types:
            if t["nom_origine"].lower() == nom_origine.lower():
                return t["id_origine"]
