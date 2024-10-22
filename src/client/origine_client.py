import requests

from typing import List


class OrigineClient:

    """

    Création de classe OrigineClient.

    Cette classe, qui ne contient que des méthodes, fait le lien entre
    l'API et l'application. Elle récupère les infos disponibles sous format
    JSON pour les transformer en objet Python, ici une liste de dictionnaire
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

    def get_id_origine_by_name(nom_origine: str) -> str:
        """

        Donne l'id de l'origine à partir de son nom.

        Il s'agit bien de l'id que l'on crée nous-même dans la méthode
        get_origine().

        Parameters
        ----------
        nom_origine : str

        Returns
        -------
        str
            id de l'origine recherchée

        Raises
        ------
        TypeError
            nom_origine doit être un str

        """

        if not isinstance(nom_origine, str):
            raise TypeError("nom_origine doit être un str")

        raw_types = OrigineClient.get_origine()
        for t in raw_types:
            if t["nom_origine"].lower() == nom_origine.lower():
                return t["id_origine"]
