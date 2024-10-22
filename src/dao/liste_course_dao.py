import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

class ListeCourseDao(metaclass=Singleton):
    """Classe contenant les méthodes pour gérer la liste de course"""

    @log
    def supprimer(self, ingredient) -> bool:
        """Suppression d'un ingrédient de la liste de courses dans la base de données

        Parameters
        ----------
        ingredient : Ingredient
            ingredient à supprimer de la liste de courses

        Returns
        -------
            True si l'ingredient a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer l'ingrédient de la liste de courses'
                    cursor.execute(
                        "DELETE FROM liste_course                  "
                        " WHERE id_ingredient=%(id_ingredient)s      ",
                        {"id_ingredient": ingredient.id_ingredient},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

