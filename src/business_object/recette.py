from src.business_object.ingredient import Ingredient
from src.business_object.categorie import Categorie
from src.business_object.origine import Origine

class Recette:

    def __init__(
        self,
        id_recette: str,
        nom_rcette: str,
        liste_ingredient: dict[Ingredient, str],
        instructions: str,
        avis: dict[str, Avis],
        liste_categorie : list[Categorie],
        origine_recette : Origine
    )
