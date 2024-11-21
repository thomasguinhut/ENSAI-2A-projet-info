import logging
from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.utilisateur import Utilisateur
from business_object.recette import Recette


class AvisDao(metaclass=Singleton):
    """

    Création de la classe AvisDao.

    Cette classe fait le lien entre les objets des classes métiers
    et la table avis de la base de données.

    """

    @log
    def retirer_avis(self, utilisateur: Utilisateur, recette: Recette) -> bool:
        """

        Suppression d'un avis associé à un utilisateur et une recette dans
        la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur associé à l'avis à supprimer de la base de données

        recette : Recette
            recette associée à l'avis à supprimer de la base de données

        Returns
        -------
            True si l'avis a bien été supprimé

        """
        id_utilisateur = utilisateur.id_utilisateur
        id_recette = recette.id_recette
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer l'avis d'un utilisateur
                    cursor.execute(
                        "DELETE FROM avis                            "
                        " WHERE id_utilisateur=%(id_utilisateur)s    "
                        " AND id_recette=%(id_recette)s              ",
                        {"id_utilisateur": id_utilisateur, "id_recette": id_recette},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def ajouter_avis(
        self, note: int, commentaire: str, utilisateur: Utilisateur, recette: Recette
    ) -> bool:
        """

        Ajout d'un avis.

        Parameters
        ----------
        note: int
        commentaires : str
        utilisateur : Utilisateur
        recette : Recette

        Returns
        -------
        created : bool
            True si l'ajout est un succès, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Récupération des avis de la recette
                    cursor.execute(
                        "SELECT id_avis "
                        "FROM avis a "
                        "WHERE id_recette = %(id_recette)s "
                        "AND id_utilisateur = %(id_utilisateur)s",
                        {
                            "id_recette": recette.id_recette,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )

                    if not cursor.fetchone():
                        # Insérer l'avis sans spécifier id_avis
                        cursor.execute(
                            "INSERT INTO avis(note, commentaire, id_utilisateur, id_recette) "
                            "VALUES (%(note)s, %(commentaire)s, "
                            "%(id_utilisateur)s, %(id_recette)s)",
                            {
                                "note": note,
                                "commentaire": commentaire,
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_recette": recette.id_recette,
                            },
                        )
                    else:
                        raise Exception("Vous avez déjà mis un avis sur cette recette.")

        except Exception as e:
            logging.info(e)
            raise

        return True  # L'avis a bien été ajouté

    def get_id_avis_by_id_utilisateur_id_recette(self, id_utilisateur: str, id_recette: str) -> str:

        if not isinstance(id_utilisateur, str):
            raise TypeError("id_utilisateur doit être un str")
        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis "
                        "FROM avis "
                        "WHERE id_utilisateur = %(id_utilisateur)s AND "
                        "id_recette = %(id_recette)s;",
                        {"id_utilisateur": id_utilisateur, "id_recette": id_recette},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res["id_avis"]
        else:
            return None
