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
                            "(%(id_recette)s, %(id_ingredient)s)             "
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

    @log
    def lister_recettes_par_ingredient(self, ingredient) -> list[dict]:
        """lister toutes les recettes par ingrédient

        Parameters
        ----------
        ingredient : Ingredient

        Returns
        -------
        res : list[dict]
            renvoie une liste de dictionnaire des recettes
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM recette; "
                        "  JOIN ingredient_recette USING(id_recette)"
                        "  JOIN ingredient USING(id_ingredient)"
                        "  WHERE id_ingredient=%(id_ingredient)s;                     ",
                        {"id_ingredient": ingredient.id_ingredient},
                    )

                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    @log
    def lister_ingredients_by_recette(self, id_recette) -> list[dict]:
        """lister toutes les recettes par ingrédient

        Parameters
        ----------
        id_recette : str

        Returns
        -------
        res : list[dict]
            renvoie une liste de dictionnaire d'ingrédients
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT ingredient.id_ingredient, ingredient.nom_ingredient "
                        "FROM ingredient "
                        "JOIN ingredient_recette USING(id_ingredient) "
                        "WHERE id_recette = %(id_recette)s;",
                        {'id_recette': id_recette}
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res
