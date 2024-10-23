from utils.log_decorator import log

from business_object.categorie import Categorie
from dao.categorie_dao import CategorieDao


class CategorieService:

    """

    Création de classe CategorieService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en rapport avec la catégorie des recettes
    en objet de la classe Catégorie. Cela facilite ensuite la
    manipulation des informations.

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

    @log
    def trouver_liste_categories(self) -> list[Categorie]:
        """

        Affiche toutes les catégories de la base de données.

        Returns
        -------
        list[Categorie]

        """

        res = CategorieDao().trouver_liste_categories()
        liste_categories = []
        if res:
            for row in res:
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=row["nom_categorie"],
                )
                liste_categories.append(categorie)
        return liste_categories

    @log
    def get_nom_categorie_by_id(self, id_categorie: str) -> str:
        """

        Donne le nom de la catégorie à partir de son id.

        Parameters
        ----------
        id_categorie: str

        Returns
        -------
        nom_categorie: str
            nom de la catégorie recherchée

        Raises
        ------
        TypeError
            id_categorie doit être un str

        """

        if not isinstance(id_categorie, str):
            raise TypeError("id_categorie doit être un str")
        return CategorieDao().get_nom_categorie_by_id(id_categorie)

    @log
    def get_id_categorie_by_name(self, nom_categorie: str) -> str:
        """

        Donne l'id de la catégorie à partir de son nom.

        Parameters
        ----------
        nom_origine : str

        Returns
        -------
        id_categorie str
            id de la catégorie recherchée

        Raises
        ------
        TypeError
            nom_categorie doit être un str

        """

        if not isinstance(nom_categorie, str):
            raise TypeError("nom_categorie doit être un str")
        return CategorieDao().get_id_categorie_by_name(nom_categorie)
