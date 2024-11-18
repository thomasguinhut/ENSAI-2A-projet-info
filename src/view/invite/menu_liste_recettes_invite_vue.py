from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues


class MenuListeRecettesInviteVue(VueAbstraite):
    """Classe pour gérer le menu des listes de recettes pour le mode invité."""

    def __init__(self, message=""):
        """
        Initialise le menu des listes de recettes.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de sélection des options pour les recettes."""
        HistoriqueVues().ajouter_vue(self)
        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Afficher toutes les recettes",
                "Ajouter des filtres",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Afficher toutes les recettes":
                Session().reset_filtres()
                from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue

                return ListeRecettesInviteVue()

            case "Ajouter des filtres":
                from view.invite.ajouter_filtres_invite_vue import AjouterFiltresInviteVue

                return AjouterFiltresInviteVue()

            case "Retour au menu principal":
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()
