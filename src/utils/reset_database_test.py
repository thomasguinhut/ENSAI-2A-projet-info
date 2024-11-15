import dotenv
import logging
import os

from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class ResetDatabaseTest(metaclass=Singleton):
    """

    Initialisation de la base de données test.

    """

    @log
    def lancer_et_remplir(self):
        """
        Crée le schéma et les tables SQL.

        Parameters
        ----------
        None

        """

        os.environ["POSTGRES_SCHEMA"] = "projet_test_dao"
        data_test_path = "data/data_test.sql"
        dotenv.load_dotenv()

        schema = os.environ["POSTGRES_SCHEMA"]

        create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE;" f"CREATE SCHEMA {schema};"

        try:
            with open("data/init_db.sql", encoding="utf-8") as init_db:
                init_db_as_string = init_db.read()

            with open(data_test_path, encoding="utf-8") as data_test:
                data_test_as_string = data_test.read()

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    logging.info("Création du schéma.")
                    cursor.execute(create_schema)
                    logging.info("Schéma créé avec succès.")

                    logging.info("Initialisation des tables.")
                    cursor.execute(init_db_as_string)
                    logging.info("Tables initialisées avec succès.")

                    logging.info("Insertion des données de test.")
                    cursor.execute(data_test_as_string)
                    logging.info("Données de test insérées avec succès.")
            print("La base de données test a bien été créée et remplie.")
        except FileNotFoundError as fnf_error:
            logging.error(f"Fichier manquant : {fnf_error}")
            raise
        except Exception as e:
            logging.error(f"Erreur lors de l'exécution des requêtes SQL : {e}")
            raise


if __name__ == "__main__":
    ResetDatabaseTest().lancer_et_remplir()
