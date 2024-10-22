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
from service.ingredient_recette_service import IngredientRecetteService


class ResetDatabase(metaclass=Singleton):
    """
    Initialisation de la base de données
    """

    @log
    def lancer(self, verif):

        """

        Crée le schéma et les tables SQL.

        Parameters
        ----------
        verif : bool
            Ne crée le schéma et les tables que si c'est voulu.

        """

        if verif:
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

    @log
    def remplir(self, ingredients, origines, categories, recettes, ingredients_recettes):

        """

        Remplit les tables SQL.

        Parameters
        ----------
        ingredients : bool
            Est-ce qu'on remplit la table ingrédients ?
        origines : bool
            Est-ce qu'on remplit la table origines ?
        categories : bool
            Est-ce qu'on remplit la table categories ?
        recettes : bool
            Est-ce qu'on remplit la table recettes ?
        ingredients_recettes : bool
            Est-ce qu'on remplit la table ingredients_recettes ?

        """
        
        if ingredients:
            liste_ingredients = IngredientClient().get_ingredient()
            for dict_ingredient in liste_ingredients:
                IngredientService().creer(dict_ingredient)

        if origines:
            liste_origines = OrigineClient().get_origine()
            for dict_origine in liste_origines:
                OrigineService().creer(dict_origine)

        if categories:
            liste_categories = CategorieClient().get_categorie()
            for dict_categorie in liste_categories:
                CategorieService().creer(dict_categorie)

        if recettes:
            liste_recettes = RecetteClient().get_recette()
            i = 1
            for dict_recette in liste_recettes:
                RecetteService().creer(dict_recette)
                print(f"Recette {i} ajoutée")
                i += 1

        if ingredients_recettes:
            liste_recettes = RecetteClient().get_recette()
            i = 1
            for dict_recette in liste_recettes:
                IngredientRecetteService().creer(dict_recette)
                print(f"Recette/ingredient {i} ajoutée")
                i += 1


if __name__ == "__main__":
    ResetDatabase().lancer(True)
    ResetDatabase().remplir(True, True, True, True, True)
