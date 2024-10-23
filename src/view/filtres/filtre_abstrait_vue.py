from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class FiltreAbstraitVue(VueAbstraite):
    def __init__(self):
        self.liste_criteres = []

    def choisir_menu(self):
        choix = inquirer.select(
            message="Choisissez vos filtres:",
            choices=self.creer_options_menu(self.liste_criteres)
            ).execute()

        if choix == "Retourner au menu des filtres":
            from view.accueil.accueil_vue import AccueilVue
            return AccueilVue("Retour au menu principal")
        else:
            Session().choix_filtres.append(choix)
            return self.choisir_menu

    def creer_options_menu(self, liste_criteres):
        """Crée les options de menu."""
        options = [critere.nom for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options

"""from service.recette_service import RecetteService"""
"""self.recettes_filtrees = RecetteService.trouver_recettes_filtrees(filtres)"""