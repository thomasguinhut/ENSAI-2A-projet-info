from utils.log_decorator import log

from business_object.origine import Origine
from dao.origine_dao import OrigineDao


class OrigineService:

    """

    Création de classe OrigineService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en rapport avec l'origine des recette
    en objet de la classe Origine. Cela facilite ensuite la
    manipulation des informations.

    """

    @log
    def creer(self, origine: dict[str, str]) -> Origine:
        """

        Crée une Origine.

        Parameters
        ----------
        origine : dict[id_origine: str, nom_origine: str]
            On utilise l'output de la méthode get_origine() présente dans
            la classe OrigineClient.

        Returns
        -------
        Origine

        """

        nouvelle_origine = Origine(
            id_origine=origine["id_origine"],
            nom_origine=origine["nom_origine"]
        )

        if OrigineDao().creer(nouvelle_origine):
            return nouvelle_origine
        else:
            return None

    @log
    def trouver_liste_origines(self) -> list[Origine]:
        """

        Affiche toutes les origines de la base de données.

        Returns
        -------
        list[Origine]

        """

        res = OrigineDao().trouver_liste_origines()
        liste_origines = []
        if res:
            for row in res:
                origine = Origine(
                    id_origine=row["id_origine"],
                    nom_origine=row["nom_origine"],
                )
                liste_origines.append(origine)
        return liste_origines

    @log
    def get_nom_origine_by_id(self, id_origine: str) -> str:
        """

        Donne le nom de l'origine à partir de son id.

        Parameters
        ----------
        id : str

        Returns
        -------
        str
            nom de l'origine recherchée

        Raises
        ------
        TypeError
            id_origine doit être un str

        """

        if not isinstance(id_origine, str):
            raise TypeError("id_origine doit être un str")
        return OrigineDao().get_nom_origine_by_id(id_origine)

    @log
    def get_id_origine_by_name(self, nom_origine: str) -> str:
        """

        Donne l'id de l'origine à partir de son nom.

        Parameters
        ----------
        nom_origine : str

        Returns
        -------
        id_origine str
            id de l'origine recherchée

        Raises
        ------
        TypeError
            nom_origine doit être un str

        """

        if not isinstance(nom_origine, str):
            raise TypeError("nom_origine doit être un str")
        return OrigineDao().get_id_origine_by_name(nom_origine)
