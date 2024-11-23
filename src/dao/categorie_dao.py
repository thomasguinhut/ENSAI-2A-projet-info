import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

# from business_object.categorie import Categorie


class CategorieDao(metaclass=Singleton):
    """

    Création de la classe CategorieDao.

    Cette classe fait le lien entre les objets de la classe Categorie,
    disponibles avec la classe CategorieService, et la table categorie de la
    base de données.

    """

    @log
    def creer(self, categorie) -> bool:
        """

        Creation d'une categorie dans la base de données

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
                        "INSERT INTO categorie(id_categorie, nom_categorie) VALUES        "
                        "(%(id_categorie)s, %(nom_categorie)s)             "
                        "  RETURNING id_categorie;                                                ",
                        {
                            "id_categorie": categorie.id_categorie,
                            "nom_categorie": categorie.nom_categorie,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        created = False
        if res:
            categorie.id_categorie = res["id_categorie"]
            created = True
        return created

    @log
    def trouver_liste_categories(self) -> list[dict[str, str]]:
        """

        Liste toutes les catégories de la base de donénes.

        Parameters
        ----------
        None

        Returns
        -------
        liste_categories : list[dict[
            "id_categorie": str, "nom_categorie": str]]
            Renvoie la liste de toutes les catégories sous forme de
            dictionnaires.

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT *" "   FROM categorie;")
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def get_nom_categorie_by_id(self, id_categorie: str) -> str:
        """

        Donne le nom de la catégorie à partir de son id.

        Parameters
        ----------
        id_categorie : str

        Returns
        -------
        str
            nom de la catégorie recherchée

        Raises
        ------
        TypeError
            id_categorie doit être un str

        """

        if not isinstance(id_categorie, str):
            raise TypeError("id_categorie doit être un str")

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_categorie "
                        "FROM categorie "
                        "WHERE id_categorie = %(id_categorie)s;",
                        {"id_categorie": id_categorie},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res["nom_categorie"]
        else:
            return None

    def get_id_categorie_by_name(self, nom_categorie: str) -> str:
        """

        Donne l'id de la catégorie à partir de son nom.

        Parameters
        nom_categorie
        nom_origine : str

        Returns
        -------
        id_categorie str
            id de la catégorie recherchée

        Raises
        ------
        TypeError
            nom_categorie doit être un str

        """

        if not isinstance(nom_categorie, str):
            raise TypeError("nom_origine doit être un str")

        nom_categorie = nom_categorie.lower()
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_categorie "
                        "FROM categorie "
                        "WHERE lower(nom_categorie) = %(nom_categorie)s;",
                        {"nom_categorie": nom_categorie},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            return res["id_categorie"]
        else:
            return None
