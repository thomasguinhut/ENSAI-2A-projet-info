from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class GestionListesVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Recettes favorites",
                "Listes de courses",
                "Retour au menu principal"
            ]
            ).execute()

        match choix:
            case "Recettes favorites":
                
                return 

            case "Listes de courses":
                
                return

            case "Retour au menu principal":
                from view.utilisateur.utilisateur_vue import UtilisateurVue
                return UtilisateurVue()

