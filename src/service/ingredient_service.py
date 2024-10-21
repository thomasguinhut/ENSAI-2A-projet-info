from tabulate import tabulate

from utils.log_decorator import log

from src.business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao


class IngredientService:
    """Classe contenant les méthodes de service des Ingrédients"""

    @log
    def creer(self, nom_ingredient) -> Ingredient:
        """Création d'un ingrédient à partir de son nom"""
        nouvel_ingredient = Ingredient(nom=nom_ingredient)
        return nouvel_ingredient if IngredientDao().creer(nouvel_ingredient) else None
