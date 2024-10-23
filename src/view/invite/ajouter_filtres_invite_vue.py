from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class AjouterFiltresInviteVue(VueAbstraite):
    """Classe pour gérer la vue d'ajout de filtres pour un utilisateur invité."""

    def __init__(self, message=""):
        """
        Initialise la vue d'ajout de filtres pour un invité.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de sélection pour l'utilisateur invité et gère le choix effectué."""
        choix = inquirer.select(
            message="Faites votre choix :",
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
                return ListeRecettesInviteVue("Affichage de la liste des recettes filtrées")

            case "Retourner au menu principal":
                Session().choix_filtres = []
                from view.invite.invite_vue import InviteVue
                return InviteVue("Retour au menu principal")
