from utils.log_decorator import log

from src.business_object.recette import Recette
from src.business_object.origine import Origine
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine
from src.business_object.ingredient import Ingredient
from src.client.ingredient_client import IngredientClient
from src.client.categorie_client import CategorieClient
from src.client.origine_client import OrigineClient

from dao.recette_dao import RecetteDao


class RecetteService:
    """Classe contenant les méthodes de service des Recettes"""

    @log
    def creer(recette: dict) -> Recette:
        """Création d'une recette à partir de son nom"""

        liste_ingredients = []
        for nom_ingredient in recette["ingredients_recette"]:
            id_ingredient = IngredientClient.get_id_ingredient_by_name(nom_ingredient)
            if id_ingredient:
                ingredient = Ingredient(id_ingredient, nom_ingredient)
                liste_ingredients.append(ingredient)

        id_categorie = CategorieClient.get_id_categorie_by_name(recette["categorie_recette"])
        if id_categorie:
            categorie = Categorie(id_categorie, recette["categorie_recette"])

        id_origine = OrigineClient.get_id_origine_by_name(recette["origine_recette"])
        if id_origine:
            origine = Origine(id_origine, recette["origine_recette"])

        nouvelle_recette = Recette(
            id_recette=recette["id_recette"],
            nom_recette=recette["nom_recette"],
            ingredients_recette=liste_ingredients,
            instructions_recette="test",
            categorie_recette=categorie,
            origine_recette=origine,
        )
        return nouvelle_recette if RecetteDao().creer(nouvelle_recette) else None
