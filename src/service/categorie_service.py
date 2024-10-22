from utils.log_decorator import log

from business_object.categorie import Categorie
from dao.categorie_dao import CategorieDao


class CategorieService:

    """

    Création de classe CategorieService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

    """

    @log
    def creer(self, categorie: dict[str, str]) -> Categorie:
        """

        Crée une Catégorie.

        Parameters
        ----------
        categorie : dict[id_categorie: str, nom_categorie: str]
            On utilise l'output de la méthode get_categorie() présente dans
            la classe CategorieClient.

        Returns
        -------
        Categorie

        """

        nouvelle_categorie = Categorie(
            id_categorie=categorie["id_categorie"],
            nom_categorie=categorie["nom_categorie"]
        )

        if CategorieDao().creer(nouvelle_categorie):
            return nouvelle_categorie
        else:
            return None
