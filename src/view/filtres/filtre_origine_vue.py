from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.origine_service import OrigineService
from view.session import Session
from InquirerPy import inquirer


class FiltreOrigineVue(FiltreAbstraitVue):
    def __init__(self):
        super().__init__()
        self.liste_criteres = OrigineService.trouver_liste_origines()

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=self.creer_options_menu(self.liste_criteres)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.filtres.ajouter_filtres_vue import AjouterFiltresVue
            return AjouterFiltresVue()
        else:
            Session().choix_filtres_origine.append(choix)
            return self.choisir_menu
