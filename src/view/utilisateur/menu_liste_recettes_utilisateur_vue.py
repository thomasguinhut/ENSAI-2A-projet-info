from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues


class MenuListeRecettesUtilisateurVue(VueAbstraite):
    """Classe pour gérer le menu des listes de recettes."""

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
                from view.utilisateur.liste_recettes_utilisateur_vue import (
                    ListeRecettesUtilisateurVue,
                )

                return ListeRecettesUtilisateurVue()

            case "Ajouter des filtres":
                from view.utilisateur.ajouter_filtres_utilisateur_vue import (
                    AjouterFiltresUtilisateurVue,
                )

                return AjouterFiltresUtilisateurVue()

            case "Retour au menu principal":

                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue()
