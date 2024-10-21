import requests
from src.business_object.origine import Origine

from typing import List


class OrigineClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        pass

    def get_origine(self) -> List[Origine]:

        # Appel du Web service
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
        origine = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                origine.append(t["strArea"])
        return origine
