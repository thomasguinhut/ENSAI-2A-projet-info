from InquirerPy import inquirer
from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.categorie_service import CategorieService


class FiltreCategorieVue(FiltreAbstraitVue):
    def __init__(self, liste_categories):
        self.liste_categories = CategorieService.trouver_liste_categories()

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=FiltreAbstraitVue().creer_options_menu(self.liste_categories)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.accueil.accueil_vue import AccueilVue
            return AccueilVue("Retour au menu principal")
        else:
            FiltreAbstraitVue().filtres.append(choix)
            return self.choisir_menu

