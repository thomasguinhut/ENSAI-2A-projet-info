import os
import logging
import dotenv

from unittest import mock

from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from client.ingredient_client import IngredientClient
from service.ingredient_service import IngredientService

from service.joueur_service import JoueurService


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    @log
    def lancer(self, test_dao=False):
        """Lancement de la réinitialisation des données
        Si test_dao = True : réinitialisation des données de test"""
        if test_dao:
            mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_test_dao"}).start()
            pop_data_path = "data/pop_db_test.sql"
        else:
            pop_data_path = "data/pop_db.sql"

        dotenv.load_dotenv()

        schema = os.environ["POSTGRES_SCHEMA"]

        create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

        init_db = open("data/init_db.sql", encoding="utf-8")
        init_db_as_string = init_db.read()
        init_db.close()

        liste_ingredients = IngredientClient().get_ingredient()
        for nom_ingredient in liste_ingredients:
            IngredientService().creer(nom_ingredient)
        # pop_db = open(pop_data_path, encoding="utf-8")
        # pop_db_as_string = pop_db.read()
        # pop_db.close()

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(create_schema)
                    cursor.execute(init_db_as_string)
                    # cursor.execute(pop_db_as_string)
        except Exception as e:
            logging.info(e)
            raise

        return True


if __name__ == "__main__":
    ResetDatabase().lancer()
