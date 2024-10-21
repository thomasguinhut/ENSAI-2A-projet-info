from tabulate import tabulate

from utils.log_decorator import log

from src.business_object.origine import Origine
from dao.origine_dao import OrigineDao


class OrigineService:
    """Classe contenant les méthodes de service des Origines"""

    @log
    def creer(self, origine) -> Origine:
        """Création d'une origine à partir de son nom"""
        nouvelle_origine = Origine(nom=origine)
        return nouvelle_origine if OrigineDao().creer(nouvelle_origine) else None
