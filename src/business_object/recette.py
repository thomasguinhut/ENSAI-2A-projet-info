from src.business_object.ingredient import Ingredient
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine


class Recette:

    def __init__(
        self,
        id_recette: str,
        nom_recette: str,
        instructions_recette: str,
        categorie_recette: Categorie,
        origine_recette: Origine,
        ingredients_recette: list[Ingredient],
    ):

        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")
        if not isinstance(nom_recette, str):
            raise TypeError("nom_recette doit être un str")
        if not isinstance(instructions_recette, str):
            raise TypeError("instructions_recette doit être un str")
        if not isinstance(categorie_recette, Categorie):
            raise TypeError("categorie_recette doit être une Catégorie")
        if not isinstance(origine_recette, Origine):
            raise TypeError("origine_recette doit être une Origine")
        if not isinstance(ingredients_recette, list):
            raise TypeError("ingredients_recette doit être une liste")
        for i in ingredients_recette:
            if not isinstance(i, Ingredient):
                raise TypeError(f"{i} doit être un Ingrédient")

        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.ingredients_recette = ingredients_recette
        self.instructions_recette = instructions_recette
        self.categorie_recette = categorie_recette
        self.origine_recette = origine_recette
