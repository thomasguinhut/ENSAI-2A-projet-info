from utils.log_decorator import log

from business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao


class IngredientService:
    """Classe contenant les méthodes de service des Ingrédients"""

    @log
    def creer(self, ingredient: dict) -> Ingredient:
        """Création d'un ingrédient à partir de son nom"""
        nouvel_ingredient = Ingredient(
            id_ingredient=ingredient["id_ingredient"], nom_ingredient=ingredient["nom_ingredient"]
        )
        return nouvel_ingredient if IngredientDao().creer(ingredient=nouvel_ingredient) else None
