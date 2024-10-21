from src.business_object.ingredient import Ingredient
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine
from src.business_object.avis import Avis


class Recette:

    def __init__(
        self,
        id_recette: str,
        nom_recette: str,
        instructions: str,
        liste_categorie: str,
        origine_recette: Origine,
        liste_ingredient: list[Ingredient],
        avis: dict[str, Avis] = None,
    ):
        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.liste_ingredient = liste_ingredient
        self.instructions = instructions
        self.avis = avis
        self.liste_categorie = liste_categorie
        self.origine_recette = origine_recette
