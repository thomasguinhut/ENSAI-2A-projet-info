import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.origine import Origine


class OrigineDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Origines de la base de données"""

    @log
    def creer(self, origine) -> bool:
        """Creation d'une origine dans la base de données

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
                        "INSERT INTO origine(id_origine, nom) VALUES        "
                        "(%(id_origine)s, %(nom)s)             "
                        "  RETURNING id_origine;                                ",
                        {
                            "id_origine": origine.id_origine,
                            "nom": origine.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            origine.id_origine = res["id_origine"]
            created = True

        return created
