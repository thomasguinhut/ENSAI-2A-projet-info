from src.business_object.ingredient import Ingredient
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine
from src.business_object.avis import Avis


class Recette:

    def __init__(
        self,
        id_recette: str,
        nom_recette: str,
        liste_ingredient: dict[Ingredient, str],
        instructions: str,
        avis: dict[str, Avis],
        liste_categorie: list[Categorie],
        origine_recette: Origine,
    ):
        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.liste_ingredient = liste_ingredient
        self.instructions = instructions
        self.avis = avis
        self.liste_categorie = liste_categorie
        self.origine_recette = origine_recette
