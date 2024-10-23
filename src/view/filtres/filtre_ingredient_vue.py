from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.ingredient_service import IngredientService


class FiltreIngredientVue(FiltreAbstraitVue):
    def __init__(self):
        super().__init__()
        self.liste_criteres = IngredientsService.trouver_liste_ingredients()
