import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.ingredient import Ingredient


class IngredientDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Ingrédients de la base de données"""

    @log
    def creer(self, ingredient) -> bool:
        """Creation d'un ingredient dans la base de données

         Parameters
         ----------
        ingredient : Ingredient

         Returns
         -------
         created : bool
             True si la création est un succès
             False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO ingredient(nom_ingredient) VALUES        "
                        "(%(nom_ingredient)s)             "
                        "  RETURNING nom_ingredient;                                ",
                        {
                            "nom_ingredient": ingredient.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            ingredient.nom = res["nom_ingredient"]
            created = True

        return created
