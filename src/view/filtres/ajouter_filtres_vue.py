from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class AjouterFiltresVue(VueAbstraite):
    def choisir_menu(self):
        choix = inquirer.select(
            message="Faites votre choix:",
            choices=[
                "Sélectionner des filtres",
                "Afficher les recettes filtrées",
                "Retourner au menu principal"
            ]
            ).execute()

        match choix:
            case "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue()

            case "Afficher les recettes filtrées":
                return

            case "Retourner au menu principal":
                Session().choix_filtres = []
                from view.utilisateur.utilisateur_vue import UtilisateurVue
                return UtilisateurVue()
