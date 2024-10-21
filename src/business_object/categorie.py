class Categorie:

    """

    Création de la classe Catégorie.

    La catégorie est une des trois infos caractéristiques d'une recette,
    avec l'origine et les ingrédients, qui mérite une classe à part.

    Parameters
    ----------
    id_categorie : str
    nom_categorie : str

    Raises
    ------
    TypeError
        id_categorie doit être un str
    TypeError
        nom_categorie doit être un str

    """

    def __init__(self, id_categorie: str, nom_categorie: str):
        """

        Constructeur de la classe.

        """

        if not isinstance(id_categorie, str):
            raise TypeError("id_categorie doit être un str")
        if not isinstance(nom_categorie, str):
            raise TypeError("nom_categorie doit être un str")

        self.id_categorie = id_categorie
        self.nom_categorie = nom_categorie
