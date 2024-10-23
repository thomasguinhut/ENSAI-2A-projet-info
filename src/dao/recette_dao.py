import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient
from business_object.origine import Origine
from business_object.categorie import Categorie


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
        print(res)

        return res

    def liste_recettes_par_filtres(
        self,
            filtres_ingredients: list[Ingredient],
            filtres_origines: list[Origine],
            filtres_categories: list[Categorie]
    ):
        liste_recettes = []
        if filtres_ingredients:
            recettes_ingredients = []
            id_recettes_ingredients = []
            for ingredient in filtres_ingredients:
                id_ingredient = ingredient.id_ingredient
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = ("SELECT * FROM recette r "
                                   "JOIN ingredient_recette ir "
                                   "ON r.id_recette = ir.id_recette "
                                   "JOIN ingredient i "
                                   "ON ir.id_ingredient = i.id_ingredient "
                                   "WHERE ")
                            req += ("ir.id_ingredient = CAST({id_ingredient} "
                                    "AS VARCHAR)".format(
                                        id_ingredient=id_ingredient))
                            cursor.execute(req)
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise
                recettes_ingredients.append(res)
                id_recettes_ingredients.append(res[0]["id_recette"])
        if filtres_origines:
            recettes_origines = []
            id_recettes_origines = []
            for origine in filtres_origines:
                id_origine = origine.id_origine
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = ("SELECT * FROM recette r "
                                   "JOIN origine o "
                                   "ON r.id_origine = o.id_origine "
                                   "WHERE ")
                            req += ("o.id_origine = CAST({id_origine} "
                                    "AS VARCHAR)".format(
                                        id_origine=id_origine))
                            cursor.execute(req)
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise
                recettes_origines.append(res)
                id_recettes_origines.append(res[0]["id_recette"])
        if filtres_categories:
            recettes_categories = []
            id_recettes_categories = []
            for categorie in filtres_categories:
                id_categorie = categorie.id_categorie
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = ("SELECT * FROM recette r "
                                   "JOIN categorie c "
                                   "ON r.id_categorie = c.id_categorie "
                                   "WHERE ")
                            req += ("c.id_categorie = CAST({id_categorie} "
                                    "AS VARCHAR)".format(
                                        id_categorie=id_categorie))
                            cursor.execute(req)
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise
                recettes_categories.append(res)
                id_recettes_categories.append(res[0]["id_recette"])
        id_liste_recettes = []
        if filtres_ingredients and filtres_origines and filtres_categories:
            recettes = (
                recettes_ingredients + recettes_origines + recettes_categories)
            id_liste_recettes = list(
                set(id_recettes_categories) &
                set(id_recettes_origines) &
                set(id_recettes_categories)
            )
        elif filtres_ingredients and filtres_origines:
            recettes = (
                recettes_ingredients + recettes_origines)
            id_liste_recettes = list(set(id_recettes_categories)
                                     & set(id_recettes_origines))
        elif filtres_ingredients and filtres_categories:
            recettes = (
                recettes_ingredients + recettes_categories)
            id_liste_recettes = list(set(id_recettes_categories)
                                     & set(id_recettes_categories))
        elif filtres_origines and filtres_categories:
            recettes = (
                recettes_origines + recettes_categories)
            id_liste_recettes = list(set(id_recettes_origines)
                                     & set(id_recettes_categories))
        elif filtres_ingredients:
            recettes = recettes_ingredients
            id_liste_recettes = id_recettes_categories
        elif filtres_origines:
            recettes = recettes_origines
            id_liste_recettes = id_recettes_origines
        elif filtres_categories:
            recettes = recettes_categories
            id_liste_recettes = id_recettes_categories
        else:
            id_liste_recettes = []

        ids_vus = set()
        recettes_filtrees = []
        for recette in recettes[0]:
            id_recette = recette["id_recette"]
            if id_recette in id_liste_recettes and id_recette not in ids_vus:
                recettes_filtrees.append(recette)
                ids_vus.add(id_recette)

        return recettes_filtrees

    @ log
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
