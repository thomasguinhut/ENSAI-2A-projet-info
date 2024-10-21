import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.categorie import Categorie


class CategorieDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Categories de la base de données"""

    @log
    def creer(self, categorie) -> bool:
        """Creation d'une categorie dans la base de données

        Parameters
        ----------
        categorie : Categorie

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
                        "INSERT INTO categorie(id_categorie, nom) VALUES        "
                        "(%(id_categorie)s, %(nom)s)             "
                        "  RETURNING id_categorie;                                                ",
                        {
                            "id_categorie": categorie.id_categorie,
                            "nom": categorie.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            categorie.id_categorie = res["id_categorie"]
            created = True

        return created
