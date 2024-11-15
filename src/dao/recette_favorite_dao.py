import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.utilisateur import Utilisateur


class RecetteFavoriteDao(metaclass=Singleton):
    """

    Création de la classe RecetteFavoriteDao.

    Cette classe fait le lien entre les objets des classes métiers
    et la table recette_favorite de la base de données.

    """

    @log
    def retirer_favori(self, utilisateur, recette) -> bool:
        """Suppression d'une recette de la liste des recettes favorites

        Parameters
        ----------
        recette : Recette
            recette à supprimer de la liste des recettes favorites

        Returns
        -------
            True si la recette a bien été supprimée
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer la recette de la liste des recettes favorites
                    cursor.execute(
                        "DELETE FROM recette_favorite                  "
                        " WHERE id_utilisateur=%(id_utilisateur)s      "
                        " AND id_recette=%(id_recette)s      ",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "id_recette": recette.id_recette,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def ajouter_favori(self, utilisateur, recette) -> bool:
        """Ajout d'une recette à la liste des recettes favorites d'un utilisateur donné

        Parameters
        ----------
        utilisateur : Utilisateur
        recette : Recette

        Returns
        -------
        created : bool
            True si l'ajout est un succès, False sinon
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO recette_favorite(id_utilisateur, id_recette) VALUES        "
                        "(%(id_utilisateur)s, %(id_recette)s)             "
                        "  RETURNING id_utilisateur;                                ",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "id_recette": recette.id_recette,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True
        return created

    @log
    def lister_recette_favorite(self, utilisateur) -> list[dict]:
        """lister toutes les recettes favorites pour un utilisateur donné

        Parameters
        ----------
        id_utilisateur : str

        Returns
        -------
        liste_recette : list[Recettes]
            renvoie la liste de toutes les recettes favorites de l'utilisateur
        """

        id_utilisateur = utilisateur.id_utilisateur

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "  SELECT *                              "
                        "  FROM recette_favorite  "
                        "  WHERE id_utilisateur = %(id_utilisateur)s;           ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res
