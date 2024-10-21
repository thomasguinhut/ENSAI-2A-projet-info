class Ingredient:
    def __init__(self, id_ingredient: str, nom_ingredient: str):

        if not isinstance(id_ingredient, str):
            raise TypeError("id_ingredient doit être un str")
        if not isinstance(nom_ingredient, str):
            raise TypeError("nom_ingredient doit être un str")

        self.id_ingredient = id_ingredient
        self.nom_ingredient = nom_ingredient
