from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues


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
        HistoriqueVues().ajouter_vue(self)

        while True:
            choix = inquirer.select(
                message="Faites votre choix :",
                choices=[
                    "Sélectionner des filtres",
                    "Afficher les recettes filtrées",
                    "Réinitialiser les filtres",
                    "Retour au menu d'accueil",
                ],
            ).execute()

            if choix == "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue()

            elif choix == "Afficher les recettes filtrées":
                from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue

                return ListeRecettesInviteVue()

            elif choix == "Réinitialiser les filtres":
                Session().reset_filtres()
                print("\nLes filtres ont été réinitialisés\n")

            else:
                Session().reset_filtres()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()
