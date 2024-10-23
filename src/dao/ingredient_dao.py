import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.ingredient import Ingredient


class IngredientDao(metaclass=Singleton):

    """

    Création de la classe IngredientDao.

    Cette classe fait le lien entre les objets de la classe Ingredient,
    disponibles avec la classe IngredientService, et la table ingredient de la
    base de données.

    """

    @log
    def creer(self, ingredient) -> bool:
        """

        Creation d'un ingrédient dans la base de données

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
                        "INSERT INTO ingredient(id_ingredient, nom_ingredient) "
                        "VALUES (%(id_ingredient)s, %(nom_ingredient)s) "
                        "RETURNING id_ingredient;",
                        {
                            "id_ingredient": ingredient.id_ingredient,
                            "nom_ingredient": ingredient.nom_ingredient,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        created = False
        if res:
            ingredient.id_ingredient = res["id_ingredient"]
            created = True
        return created

    @log
    def trouver_liste_ingredients(self) -> list[dict[str, str]]:
        """

        Liste tous les ingrédients de la base de donénes.

        Parameters
        ----------
        None

        Returns
        -------
        liste_categories : list[dict[
            "id_ingredient": str, "nom_ingredient": str]]
            Renvoie la liste de tous les ingrédients sous forme de
            dictionnaires

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *"
                        "   FROM ingredient;"
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def get_nom_ingredient_by_id(self, id_ingredient: str) -> str:
        """

        Donne le nom de l'ingrédient à partir de son id.

        Parameters
        ----------
        id_ingredient : str

        Returns
        -------
        nom_ingrédient: str
            nom de l'ingrédient recherchée

        Raises
        ------
        TypeError
            id_ingredient doit être un str

        """

        if not isinstance(id_ingredient, str):
            raise TypeError("id_ingredient doit être un str")

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_ingredient "
                        "FROM ingredient "
                        "WHERE id_ingredient = %(id_ingredient)s;",
                        {'id_ingredient': id_ingredient}
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res['nom_ingredient']
        else:
            return None

    def get_id_ingredient_by_name(self, nom_ingredient: str) -> str:
        """

        Donne l'id de l'ingrédient à partir de son nom.

        Parameters
        ----------
        nom_ingredient: str

        Returns
        -------
        id_ingredient str
            id de l'ingrédient recherché

        Raises
        ------
        TypeError
            nom_ingredient doit être un str

        """

        if not isinstance(nom_ingredient, str):
            raise TypeError("nom_origine doit être un str")

        nom_ingredient = nom_ingredient.lower()
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_ingredient "
                        "FROM ingredient "
                        "WHERE lower(nom_ingredient) = %(nom_ingredient)s;",
                        {'nom_ingredient': nom_ingredient}
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res['id_ingredient']
        else:
            return None
