from InquirerPy import inquirer
from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.ingredient_service import IngredientService


class FiltreIngredientVue(FiltreAbstraitVue):
    def __init__(self, liste_ingredients):
        self.liste_ingredients = IngredientsService.trouver_liste_ingredients()

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=FiltreAbstraitVue().creer_options_menu(self.liste_ingredients)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.accueil.accueil_vue import AccueilVue
            return AccueilVue("Retour au menu principal")
        else:
            FiltreAbstraitVue().filtres.append(choix)
            return self.choisir_menu

