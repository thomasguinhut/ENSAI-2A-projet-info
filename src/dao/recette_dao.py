import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection
from business_object.recette import Recette


class RecetteDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Recettes de la base de données"""

    @log
    def creer(self, recette) -> bool:
        """Creation d'une recette dans la base de données

         Parameters
         ----------
        recette : Recette

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
                        "INSERT INTO recette(id_recette, nom_recette,"
                        "instructions_recette, id_origine, id_categorie) VALUES  "
                        "(%(id_recette)s, %(nom_recette)s, %(instructions_recette)s, "
                        "%(id_origine)s, %(id_categorie)s)             "
                        "  RETURNING id_recette;                                ",
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
        created = False
        if res:
            recette.id_recette = res["id_recette"]
            created = True
        return created

        @log
        def lister_toutes_recettes(self) -> list[Recette]:
            """lister toutes les recettes

            Parameters
            ----------
            None

            Returns
            -------
            liste_recettes : list[Recette]
                renvoie la liste de toutes les recettes dans la base de données
            """

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT *                              "
                            "  FROM recette;                        "
                        )
                        res = cursor.fetchall()
            except Exception as e:
                logging.info(e)
                raise

            liste_recettes = []

            if res:
                for row in res:
                    recette = Recette(
                        id_recette=row["id_recette"],
                        nom_recette=row["nom_recette"],
                        instructions_recette=row["instructions_recettes"],
                        id_origine=row["id_origine"],
                        id_categorie=row["id_categorie"],
                    )

                    liste_recettes.append(recette)

            return liste_recettes

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
                            "  JOIN recette_ingredient USING(id_recette)"
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
