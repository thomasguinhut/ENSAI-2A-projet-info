from utils.log_decorator import log

from src.business_object.origine import Origine
from dao.origine_dao import OrigineDao


class OrigineService:
    """Classe contenant les méthodes de service des Origines"""

    @log
    def creer(self, origine: dict) -> Origine:
        """Création d'une origine à partir de son nom"""
        nouvelle_origine = Origine(
            id_origine=origine["id_origine"], nom_origine=origine["nom_origine"]
        )
        return nouvelle_origine if OrigineDao().creer(nouvelle_origine) else None
