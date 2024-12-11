import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient
from business_object.origine import Origine
from business_object.categorie import Categorie


class RecetteDao(metaclass=Singleton):
    @log
    def creer(self, recette):
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
                        """
                        INSERT INTO recette(
                            id_recette, nom_recette, instructions_recette, id_origine, id_categorie
                        ) VALUES (%(id_recette)s, %(nom_recette)s, %(instructions_recette)s, 
                                  %(id_origine)s, %(id_categorie)s)
                        RETURNING id_recette;
                        """,
                        {
                            "id_recette": recette.id_recette,
                            "nom_recette": recette.nom_recette,
                            "instructions_recette": recette.instructions_recette,
                            "id_origine": recette.origine_recette.id_origine,
                            "id_categorie": recette.categorie_recette.id_categorie,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            recette.id_recette = res["id_recette"]
            return True
        return False

    @log
    def trouver_liste_recettes(self):
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
                    cursor.execute("SELECT * FROM recette;")
                    return cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

    def filtrer_recettes(
        self,
        filtres_ingredients: list[Ingredient] = None,
        filtres_origines: list[Origine] = None,
        filtres_categories: list[Categorie] = None,
    ):
        """

        Filtre les recettes selon des ingrédients, des origines et des catégories.

        Attention : il y a une intersection entre ces trois types de filtre, mais il y a
        une union au sein de chacun de es types. Par exemple, chercher mettre dessert en
        catégorie et French en origine donne tous les desserts français. Si on ajoute
        Spanish en paramètre, cela affiche tous les désserts français et tous les desserts
        espagnols.

        Args:
            filtres_ingredients (list[Ingredient], optional). Defaults to None.
            filtres_origines (list[Origine], optional). Defaults to None.
            filtres_categories (list[Categorie], optional). Defaults to None.

        Returns:
            recettes_filtrees: list[dict[
            str, str, str, Origine, Categorie, list[Ingredient]]
            Renvoie la liste de toutes les recettes concernées par les filtres
            sous forme de dictionnaires

        """
        recettes_ingredients = []
        id_recettes_ingredients = []

        if filtres_ingredients:
            for ingredient in filtres_ingredients:
                id_ingredient = ingredient.id_ingredient
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = """
                                SELECT * 
                                FROM recette r
                                JOIN ingredient_recette ir ON r.id_recette = ir.id_recette
                                JOIN ingredient i ON ir.id_ingredient = i.id_ingredient
                                WHERE ir.id_ingredient = %s
                            """
                            cursor.execute(req, (id_ingredient,))
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise

                recettes_ingredients.extend(res)
                if res:
                    for i in range(len(res)):
                        id_recettes_ingredients.append(res[i]["id_recette"])
                else:
                    id_recettes_ingredients.append(None)
        if filtres_origines:
            for origine in filtres_origines:
                id_origine = origine.id_origine
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = (
                                "SELECT * FROM recette r "
                                "JOIN origine o "
                                "ON r.id_origine = o.id_origine "
                                "WHERE "
                            )
                            req += "o.id_origine = CAST({id_origine} " "AS VARCHAR)".format(
                                id_origine=id_origine
                            )
                            cursor.execute(req)
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise
                recettes_origines.append(res)
                if res:
                    for i in range(len(res)):
                        id_recettes_origines.append(res[i]["id_recette"])
                else:
                    id_recettes_origines.append(None)
        if filtres_categories:
            for categorie in filtres_categories:
                id_categorie = categorie.id_categorie
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            req = (
                                "SELECT * FROM recette r "
                                "JOIN categorie c "
                                "ON r.id_categorie = c.id_categorie "
                                "WHERE "
                            )
                            req += "c.id_categorie = CAST({id_categorie} " "AS VARCHAR)".format(
                                id_categorie=id_categorie
                            )
                            cursor.execute(req)
                            res = cursor.fetchall()
                except Exception as e:
                    logging.info(e)
                    raise
                recettes_categories.append(res)
                if res:
                    for i in range(len(res)):
                        id_recettes_categories.append(res[i]["id_recette"])
                else:
                    id_recettes_categories.append(None)
        id_liste_recettes = []
        if filtres_ingredients and filtres_origines and filtres_categories:
            recettes = recettes_ingredients + recettes_origines + recettes_categories
            id_liste_recettes = list(
                set(id_recettes_ingredients)
                & set(id_recettes_origines)
                & set(id_recettes_categories)
            )
        elif filtres_ingredients and filtres_origines:
            recettes = recettes_ingredients + recettes_origines
            id_liste_recettes = list(set(id_recettes_ingredients) & set(id_recettes_origines))
        elif filtres_ingredients and filtres_categories:
            recettes = recettes_ingredients + recettes_categories
            id_liste_recettes = list(set(id_recettes_ingredients) & set(id_recettes_categories))
        elif filtres_origines and filtres_categories:
            recettes = recettes_origines + recettes_categories
            id_liste_recettes = list(set(id_recettes_origines) & set(id_recettes_categories))
        elif filtres_ingredients:
            recettes = recettes_ingredients
            id_liste_recettes = id_recettes_ingredients
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
        if recettes[0]:
            for recette in recettes:
                id_recette = recette[0]["id_recette"]
                if id_recette in id_liste_recettes and id_recette not in ids_vus:
                    recettes_filtrees.append(recette)
                    ids_vus.add(id_recette)
        else:
            recettes_filtrees = []

        return recettes_filtrees

    @log
    def trouver_recette(self, nom_recette) -> dict["id":str, str, str, str, str, str]:
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

    def get_nom_recette_by_id(self, id_recette: str) -> str:
        """

        Donne le nom de la recette à partir de son id.

        Parameters
        ----------
        id : str

        Returns
        -------
        str
            nom de la recette recherchée

        Raises
        ------
        TypeError
            id_recette doit être un str

        """

        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_recette " "FROM recette " "WHERE id_recette = %(id_recette)s;",
                        {"id_recette": id_recette},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res["nom_recette"]
        else:
            return None
