import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


class RecetteDao(metaclass=Singleton):

    """

    Création de la classe RecetteDao.

    Cette classe fait le lien entre les objets de la classe Recette,
    disponibles avec la classe Recette Service, et la table recette de la
    base de données.

    """

    @log
    def creer(self, recette) -> bool:
        """

        Creation d'une recette dans la base de données.

        Parameters
        ----------
        recette : Recette

        Returns
        -------
        created : bool
            True si la création est un succès, False sinon.

        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO recette(id_recette, nom_recette,"
                        "                    instructions_recette, id_origine,"
                        "                    id_categorie) VALUES"
                        "(%(id_recette)s, %(nom_recette)s,"
                        "%(instructions_recette)s, %(id_origine)s,"
                        "%(id_categorie)s)"
                        "RETURNING id_recette;",
                        {
                            "id_recette": recette.id_recette,
                            "nom_recette": recette.nom_recette,
                            "instructions_recette": (
                                recette.instructions_recette),
                            "id_origine": recette.origine_recette.id_origine,
                            "id_categorie": (
                                recette.categorie_recette.id_categorie),
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        created = False
        if res:
            recette.id_recette = res["id_recette"]
            created = True
        return created

    @log
    def trouver_liste_recettes(self) -> list[dict[
            "id": str, str, str, str, str, str]]:
        """

        Liste toutes les recettes de la base de donénes.

        Parameters
        ----------
        None

        Returns
        -------
        liste_recettes : list[dict[
            str, str, str, Origine, Categorie, list[Ingredient]]
            Renvoie la liste de toutes les recettes sous forme de dictionnaires

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *"
                        "   FROM recette;"
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def liste_recettes_par_filtres(self, filtres_ingredients: list[Ingredient],
                                   filtres_origines: list[Origine],
                                   filtres_categories: list[Categorie]
                                   ):
        for ingredient in filtres_ingredients:
            id_ingredient = ingredient.id_ingredient
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        req = "SELECT mmmmmmm FROm truc WHERE"
                        for filtre in filtres_ingredients:
                            req += "ir.id_ingredient = {id_ingredient}".format(
                                id_ingredient=filtre)
                        cursor.execute(
                            """
                            SELECT DISTINCT (r.id_recette, r.nom_recette,
                                            r.instructions_recette)
                            FROM recette r
                            JOIN ingredient_recette ir
                            ON r.id_recette = ir.id_recette
                            JOIN ingredient i
                            ON ir.id_ingredient = i.id_ingredient
                            JOIN origine o
                            ON r.id_origine = o.id_origine
                            JOIN categorie c
                            ON r.id_categorie = c.id_categorie
                            WHERE r.id_origine = 'id_origine_1')
                            AND r.id_categorie = 'id_categorie_1')
                            AND i.id_ingredient = 'id_ingredient_1');
                            """,
                            {"id_categorie": categorie.id_categorie},
                        )
                        res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    @log
    def lister_recettes_par_categorie(self, categorie) -> list[dict]:
        """lister toutes les recettes par catégorie

        Parameters
        ----------
        categorie : Categorie

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
                        "  JOIN categorie USING(id_categorie)"
                        "  WHERE id_categorie=%(id_categorie)s;                     ",
                        {"id_categorie": categorie.id_categorie},
                    )

                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    @log
    def lister_recettes_par_origine(self, origine) -> list[dict]:
        """lister toutes les recettes par origine

        Parameters
        ----------
        origine : Origine

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
                        "  JOIN origine USING(id_origine)"
                        "  WHERE id_origine=%(id_origine)s;                     ",
                        {"id_origine": origine.id_origine},
                    )

                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    @log
    def trouver_recette(self, nom_recette) -> dict[
            "id": str, str, str, str, str, str]:
        """

        Trouver une recette dans la base de données

        Parameters
        ----------
        nom_recette : str

        Returns
        -------
        recette : dict[
            str, str, str, Origine, Categorie, list[Ingredient]
            Renvoie une recette sous forme de dictionnaire

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *"
                        "   FROM recette"
                        "   WHERE nom_recette=%(nom_recette)s;                     ",
                        {"nom_recette": nom_recette},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res
