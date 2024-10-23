import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.origine import Origine


class OrigineDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Origines de la base de données"""

    @log
    def creer(self, origine) -> bool:
        """

        Creation d'une origine dans la base de données

        Parameters
        ----------
        origine : Origine

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
                        "INSERT INTO origine(id_origine, nom_origine) VALUES        "
                        "(%(id_origine)s, %(nom_origine)s)             "
                        "  RETURNING id_origine;                                ",
                        {"id_origine": origine.id_origine,
                            "nom_origine": origine.nom_origine},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        created = False
        if res:
            origine.id_origine = res["id_origine"]
            created = True
        return created

    def get_nom_origine_by_id(self, id_origine: str) -> str:
        """

        Donne le nom de l'origine à partir de son id.

        Parameters
        ----------
        id : str

        Returns
        -------
        str
            nom de l'origine recherchée

        Raises
        ------
        TypeError
            id_origine doit être un str

        """

        if not isinstance(id_origine, str):
            raise TypeError("id_origine doit être un str")

        id_origine = id_origine.lower()
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_origine "
                        "FROM origine "
                        "WHERE lower(id_origine) = %(id_origine)s;",
                        {'id_origine': id_origine}
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        if res:
            return res['nom_origine']
        else:
            return None
