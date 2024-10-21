from utils.log_decorator import log

from src.business_object.recette import Recette
from src.business_object.origine import Origine
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine

from dao.recette_dao import RecetteDao


class RecetteService:
    """Classe contenant les méthodes de service des Recettes"""

    @log
    def creer(self, recette: dict) -> Recette:
        """Création d'une recette à partir de son nom"""
        nouvelle_recette = Recette(
            id_recette=recette["id_recette"],
            nom_recette=recette["nom_recette"],
            ingredients_recette=recette["ingredients_recette"],
            instructions_recette=recette["instructions_recette"],
            categorie_recette=Categorie(nom_categorie=recette["categorie_recette"],
            origine_recette=Origine(nom_origine=["origine_recette"]),
        )
        return nouvelle_recette if RecetteDao().creer(nouvelle_recette) else None
