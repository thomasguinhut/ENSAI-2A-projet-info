import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


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
                        "INSERT INTO recette(id_recette, nom, instructions, id_origine, id_categorie) VALUES        "
                        "(%(id_origine)s, %(nom)s, %(instructions)s, %(id_origine)s, %(id_categorie)s)             "
                        "  RETURNING id_recette;                                ",
                        {
                            "id_recette": recette.id_recette,
                            "nom": recette.nom,
                            "instructions": recette.instructions,
                            "id_origine": recette.id_origine,
                            "id_categorie": recette.id_categorie,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            recette.id_recette = res["id_recette"]
            created = True

        return created
