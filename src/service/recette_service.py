from tabulate import tabulate

from utils.log_decorator import log

from src.business_object.recette import Recette
from dao.recette_dao import RecetteDao


class RecetteService:
    """Classe contenant les méthodes de service des Recettes"""

    @log
    def creer(self, recette) -> Recette:
        """Création d'une recette à partir de son nom"""
        nouvelle_recette = Recette(
            id_recette=recette["id_recette"],
            nom_recette=recette["nom"],
            liste_ingredient=recette["ingredients"],
            instructions=recette["instructions"],
            liste_categorie=recette["categorie"],
            origine_recette=["origine"],
        )
        return nouvelle_recette if RecetteDao().creer(nouvelle_recette) else None
