from InquirerPy import inquirer
from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.origine_service import OrigineService


class FiltreOrigineVue(FiltreAbstraitVue):
    def __init__(self, liste_origines):
        self.liste_origines = OriginesService.trouver_liste_origines()

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=FiltreAbstraitVue().creer_options_menu(self.liste_origines)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.accueil.accueil_vue import AccueilVue
            return AccueilVue("Retour au menu principal")
        else:
            FiltreAbstraitVue().filtres.append(choix)
            return self.choisir_menu
