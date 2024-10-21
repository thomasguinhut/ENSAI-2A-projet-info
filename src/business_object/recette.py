from src.business_object.ingredient import Ingredient
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine
from src.business_object.avis import Avis


class Recette:

    def __init__(
        self,
        id_recette: str,
        nom_recette: str,
        instructions_recette: str,
        categorie_recette: Categorie,
        origine_recette: Origine,
        ingredients_recette: list[Ingredient],
        avis_recette: dict[str, Avis] = None,
    ):
        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.liste_ingredient = ingredients_recette
        self.instructions = instructions_recette
        self.avis = avis_recette
        self.liste_categorie = categorie_recette
        self.origine_recette = origine_recette
