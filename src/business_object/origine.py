class Origine:

    """

    Création de la classe Origine.

    L'origine est une des trois infos caractéristiques d'une recette,
    avec la catégorie et les ingrédients, qui mérite une classe à part.

    Parameters
    ----------
    id_origine : str
    nom_origine : str

    Raises
    ------
    TypeError
        id_origine doit être un str
    TypeError
        nom_origine doit être un str

    """

    def __init__(self, id_origine: str, nom_origine: str):
        """

        Constructeur de la classe

        """

        if not isinstance(nom_origine, str):
            raise TypeError("id_origine doit être un str")
        if not isinstance(id_origine, str):
            raise TypeError("nom_origine doit être un str")

        self.id_origine = id_origine
        self.nom_origine = nom_origine
