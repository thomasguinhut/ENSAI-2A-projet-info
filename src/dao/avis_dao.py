import logging
import random
from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.utilisateur import Utilisateur
from business_object.recette import Recette
from business_object.avis import Avis

# from business_object.avis import Avis


class AvisDao(metaclass=Singleton):

    """

    Création de la classe AvisDao.

    Cette classe fait le lien entre les objets des classes métiers
    et la table avis de la base de données.

    """

    @log
    def supprimer_avis(self, utilisateur: Utilisateur,
                       recette: Recette) -> bool:
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
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_recette": id_recette
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def ajouter_avis(self, note: int, commentaire: str, utilisateur: Utilisateur,
                     recette: Recette) -> bool:
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
        id_avis = str(random.sample(range(1, 100), 1))
        avis = Avis(id_avis, commentaire, note)
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Récupération des avis de la recette
                    cursor.execute(
                        """
                        "SELECT a.id_avis  "
                        "FROM avis a    "
                       " WHERE id_recette = %(id_recette)s  "
                       " AND id_utilisateur = %(id_utilisateur)s
                        """,
                        {
                            "id_recette": recette.id_recette,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        }
                    )

                    if not cursor.fetchone():
                        cursor.execute(
                            " INSERT INTO avis(id_avis, note, commentaire, "
                            " id_utilisateur, id_recette) "
                            " VALUES (%(id_avis)s, %(note)s, %(commentaire)s, "
                            " %(id_utilisateur)s, %(id_recette)s)",
                            {
                                "id_avis": avis.id_avis,
                                "note": avis.note,
                                "commentaire": avis.commentaire,
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_recette": recette.id_recette,
                            }
                        )

        except Exception as e:
            logging.info(e)
            raise

        return True  # L'avis a bien été ajouté
