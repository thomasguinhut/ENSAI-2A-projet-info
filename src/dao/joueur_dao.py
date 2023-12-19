from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from dto.joueur import Joueur


class JoueurDao(metaclass=Singleton):
    @log
    def creer(self, joueur) -> bool:
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur

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
                        "INSERT INTO projet.joueur(pseudo, mdp, age, mail, fan_pokemon) VALUES "
                        "(%(pseudo)s, %(mdp)s, %(age)s, %(mail)s, %(fan_pokemon)s)             "
                        "  RETURNING id_joueur;                                                ",
                        {
                            "pseudo": joueur.pseudo,
                            "mdp": joueur.mdp,
                            "age": joueur.age,
                            "mail": joueur.mail,
                            "fan_pokemon": joueur.fan_pokemon,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            joueur.id = res["id_joueur"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_joueur) -> Joueur:
        """trouver un joueur grace à son id

        Parameters
        ----------
        id_joueur : int
            numéro id du joueur que l'on souhaite trouver

        Returns
        -------
        joueur : Joueur
            renvoie le joueur que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet.joueur               "
                        " WHERE id_joueur = %(id_joueur)s;  ",
                        {"id_joueur": id_joueur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        joueur = None
        if res:
            joueur = Joueur(
                pseudo=res["pseudo"],
                age=res["age"],
                mail=res["mail"],
                fan_pokemon=res["fan_pokemon"],
                id_joueur=res["id_joueur"],
            )

        return joueur

    @log
    def lister_tous(self) -> list[Joueur]:
        """lister tous les joueurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_joueurs : list[Joueur]
            renvoie la liste de tous les joueurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                   "
                        "   FROM projet.joueur      "
                        "  WHERE pseudo != 'admin'  "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            print(e)
            raise

        liste_joueurs = []

        if res:
            for row in res:
                joueur = Joueur(
                    id_joueur=row["id_joueur"],
                    pseudo=row["pseudo"],
                    age=row["age"],
                    mail=row["mail"],
                    fan_pokemon=row["fan_pokemon"],
                )

                liste_joueurs.append(joueur)

        return liste_joueurs

    @log
    def supprimer(self, joueur) -> bool:
        """Suppression d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur
            joueur à supprimer de la base de données

        Returns
        -------
            True si le joueur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un joueur
                    cursor.execute(
                        "DELETE FROM projet.joueur           "
                        " WHERE id_joueur=%(id_joueur)s      ",
                        {"id_joueur": joueur.id_joueur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    @log
    def se_connecter(self, pseudo, mdp) -> Joueur:
        """se connecter grâce à son pseudo et son mot de passe

        Parameters
        ----------
        pseudo : str
            pseudo du joueur que l'on souhaite trouver
        mdp : str
            mot de passe du joueur

        Returns
        -------
        joueur : Joueur
            renvoie le joueur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet.joueur               "
                        " WHERE pseudo = %(pseudo)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        joueur = None

        if res:
            joueur = Joueur(
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                age=res["age"],
                mail=res["mail"],
                fan_pokemon=res["fan_pokemon"],
                id_joueur=res["id_joueur"],
            )

        return joueur
