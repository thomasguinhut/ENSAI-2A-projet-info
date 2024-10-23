import requests

from typing import List


class OrigineClient:

    """

    Création de classe OrigineClient.

    Cette classe, qui ne contient que des méthodes, fait le lien entre
    l'API et l'application. Elle récupère les infos disponibles sous format
    JSON pour les transformer en objet Python, ici une liste de dictionnaires
    avec un dictionnaire par origine.

    """

    def __init__(self) -> None:
        pass

    def get_origine(self) -> List[dict[str, str]]:
        """

        Récupère toutes les origines enregstrées dans l'API.

        On crée nous-même l'id de l'origine, car il n'y en a pas dans l'API.

        Returns
        -------
        List[dict[id_origine: str, nom_origine: str]]

        """

        req = requests.get(
            "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
        )
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
