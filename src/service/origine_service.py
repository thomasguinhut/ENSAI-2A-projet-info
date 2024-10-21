from utils.log_decorator import log

from src.business_object.origine import Origine
from dao.origine_dao import OrigineDao


class OrigineService:

    """

    Création de classe OrigineService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'pplication en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

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
