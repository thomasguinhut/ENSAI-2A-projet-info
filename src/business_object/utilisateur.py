from src.business_object.recette import Recette
from src.business_object.ingredient import Ingredient


class Utilisateur:

    """

    Création de la classe Utilisateur.

    Parameters
    ----------
    id_utilisateur : str
    mdp : str
    favoris : list[Recette]
    courses : list[Ingredient]

    Raises
    ------
    TypeError
        id_utilisateur doit être un str
    TypeError
        mdp doit être un str
    TypeError
        favoris doit être une liste
    TypeError
        tout élément de favoris doit être une Recette
    TypeError
        courses doit être une liste
    TypeError
        tout élément de courses doit être un Ingredient

    """

    def __init__(self, id_utilisateur: str, mdp: str,
                 favoris: list[Recette], courses: list[Ingredient]):
        """
        Constructeur de la classe.

        """

        if not isinstance(id_utilisateur, str):
            raise TypeError("id_utilisateur doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("mdp doit être un str")
        if not isinstance(favoris, list):
            raise TypeError("favoris doit être une liste")
        for i in favoris:
            if not isinstance(i, Recette):
                raise TypeError(f"{i} doit être une Recette")
        if not isinstance(courses, list):
            raise TypeError("courses doit être une liste")
        for i in courses:
            if not isinstance(i, Ingredient):
                raise TypeError(f"{i} doit être un Ingredient")

        self.id_utilisateur = id_utilisateur
        self.mdp = mdp
        self.favoris = favoris
        self.courses = courses
