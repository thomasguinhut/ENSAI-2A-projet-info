from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class AjouterFiltresVue(VueAbstraite):
    def choisir_menu(self):
        choix = inquirer.select(
            message="Faites votre choix:",
            choices=[
                "Sélectionner des filtres",
                "Afficher les recettes filtrées",
                "Retour au menu principal"
            ]
            ).execute()

        match choix:
            case "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue()

            case "Afficher les recettes filtrées":
                return

            case "Retour au menu principal":
                from view.utilisateur.utilisateur_vue import UtilisateurVue
                return UtilisateurVue()
