import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de données"""

    @log
    def creer(self, utilisateur) -> bool:
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

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
                        "INSERT INTO utilisateur(id_utilisateur, mdp) VALUES        "
                        "(%(id_utilisateur)s, %(mdp)s)             "
                        "  RETURNING id_utilisateur;                                ",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "mdp": utilisateur.mdp,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """trouver un Utilisateur grace à son id

        Parameters
        ----------
        id_utilisateur : int
            numéro id de l'utilisateur que l'on souhaite trouver

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM utilisateur                      "
                        " WHERE id_utilisateur = %(id_utilisateur)s;  ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],
            )

        return utilisateur

    @log
    def se_connecter(self, id_utilisateur, mdp) -> Utilisateur:
        """se connecter grâce à son id et son mot de passe

        Parameters
        ----------
        id_utilisateur : str
            id de l'utilisateur que l'on souhaite trouver
        mdp : str
            mot de passe de l'utilisateur

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM utilisateur                      "
                        " WHERE id_utilisateur = %(id_utilisateur)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"id_utilisateur": id_utilisateur, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        utilisateur = None

        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],
                mdp=res["mdp"],
            )

        return utilisateur
