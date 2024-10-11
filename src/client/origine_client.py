import requests

from typing import List


class OrigineClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_origine(self) -> List[Origine]:

        # Appel du Web service
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
        origine = {}
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            i = 1
            for t in raw_types:
                origine[i] = t["strArea"]
                i += 1

        return origine
