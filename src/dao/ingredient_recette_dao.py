import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


class IngredientRecetteDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux ingrédient
    d'une recette de la base de données"""

    @log
    def creer(self, recette) -> bool:
        """Creation d'une table qui associe chaque ingredient à sa recette dans la base de données

         Parameters
         ----------
        recette : Recette

         Returns
         -------
         created : bool
             True si la création est un succès
             False sinon
        """

        for ingredient in recette.ingredients_recette:

            res = None
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO ingredient_recette(id_recette, id_ingredient) VALUES"
                            "(%(id_recette)s, %(nom_ingredient)s)             "
                            "  RETURNING id_recette, id_ingredient;              ",
                            {
                                "id_recette": recette.id_recette,
                                "id_ingredient": ingredient.id_ingredient,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)
            created = False
            if res:
                recette.id_recette = res["id_recette"]
                created = True
            return created
