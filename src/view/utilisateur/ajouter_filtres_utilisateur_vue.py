from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class AjouterFiltresUtilisateurVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        choix = inquirer.select(
            message="Faites votre choix:",
            choices=[
                "Sélectionner des filtres",
                "Afficher les recettes",
                "Retourner au menu principal"
            ]
            ).execute()

        match choix:
            case "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue("Type du filtre")

            case "Afficher les recettes":
                return

            case "Retourner au menu principal":
                Session().choix_filtres = []
                from view.utilisateur.utilisateur_vue import UtilisateurVue
                return UtilisateurVue("Retour au menu principal")
