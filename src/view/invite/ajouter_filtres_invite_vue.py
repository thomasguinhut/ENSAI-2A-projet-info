from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class AjouterFiltresInviteVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

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

                return TypeFiltreVue("Type du filtre")

            case "Afficher les recettes filtrées":
                from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue
                return ListeRecettesInviteVue("Affichage de la liste des recettes")

            case "Retourner au menu principal":
                Session().choix_filtres = []
                from view.invite.invite_vue import InviteVue
                return InviteVue("Retour au menu principal")
