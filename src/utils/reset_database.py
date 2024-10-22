import os
import dotenv
import logging

from log_decorator import log
from singleton import Singleton
from dao.db_connection import DBConnection
from client.ingredient_client import IngredientClient
from client.origine_client import OrigineClient
from client.categorie_client import CategorieClient
from client.recette_client import RecetteClient
from service.ingredient_service import IngredientService
from service.origine_service import OrigineService
from service.categorie_service import CategorieService
from service.recette_service import RecetteService


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    @log
    def lancer(self):
        dotenv.load_dotenv()
        schema = os.environ["POSTGRES_SCHEMA"]
        create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"
        with open("data/init_db.sql", encoding="utf-8") as init_db:
            init_db_as_string = init_db.read()
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(create_schema)
                    cursor.execute(init_db_as_string)
        except Exception as e:
            logging.error(e)
            raise
        return True

    @log
    def remplir(self):

        liste_ingredients = IngredientClient().get_ingredient()
        for dict_ingredient in liste_ingredients:
            print(dict_ingredient)
            IngredientService().creer(dict_ingredient)
        
        liste_origines = OrigineClient().get_origine()
        for dict_origine in liste_origines:
            print(dict_origine)
            OrigineService().creer(dict_origine)

        liste_categories = CategorieClient().get_categorie()
        for dict_categorie in liste_categories:
            print(dict_categorie)
            CategorieService().creer(dict_categorie)
        
        liste_recettes = RecetteClient().get_recette()
        for dict_recette in liste_recettes:
            print(dict_recette)
            RecetteService().creer(dict_recette)


if __name__ == "__main__":
    ResetDatabase().lancer()
    ResetDatabase().remplir()
