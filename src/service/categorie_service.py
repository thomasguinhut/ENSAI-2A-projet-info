from utils.log_decorator import log

from src.business_object.categorie import Categorie
from dao.categorie_dao import CategorieDao


class CategorieService:
    """Classe contenant les méthodes de service des Catégories"""

    @log
    def creer(self, categorie: dict) -> Categorie:
        """Création d'une catégorie à partir de son nom"""
        nouvelle_categorie = Categorie(
            id_categorie=categorie["id_categorie"], nom_categorie=categorie["nom_categorie"]
        )
        return nouvelle_categorie if CategorieDao().creer(nouvelle_categorie) else None
