class Ingredient:
    """

    Création de la classe Ingrédient.

    Les ingrédients constituent une des trois infos caractéristiques d'une
    recette, avec l'origine et la catégorie, qui mérite une classe à part.

    Parameters
    ----------
    id_ingredient : str
    nom_ingredient : str

    Raises
    ------
    TypeError
        id_ingredient doit être un str
    TypeError
        nom_ingredient doit être un str

    """

    def __init__(self, id_ingredient: str, nom_ingredient: str):
        """

        Constructeur de la classe.

        """

        if not isinstance(id_ingredient, str):
            raise TypeError("id_ingredient doit être un str")
        if not isinstance(nom_ingredient, str):
            raise TypeError("nom_ingredient doit être un str")

        self.id_ingredient = id_ingredient
        self.nom_ingredient = nom_ingredient
