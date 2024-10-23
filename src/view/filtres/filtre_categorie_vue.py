from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.categorie_service import CategorieService
from view.session import Session
from InquirerPy import inquirer


class FiltreCategorieVue(FiltreAbstraitVue):
    def __init__(self):
        super().__init__()
        self.liste_criteres = CategorieService.trouver_liste_categories()

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=self.creer_options_menu(self.liste_criteres)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.filtres.ajouter_filtres_vue import AjouterFiltresVue
            return AjouterFiltresVue()
        else:
            Session().choix_filtres_categorie.append(choix)
            return self.choisir_menu
