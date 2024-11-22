from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues


class AjouterFiltresUtilisateurVue(VueAbstraite):
    """Classe pour gérer la vue d'ajout de filtres par l'utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue d'ajout de filtres.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de sélection pour l'utilisateur et gère le choix effectué."""
        HistoriqueVues().ajouter_vue(self)

        while True:
            choix = inquirer.select(
                message="Faites votre choix :",
                choices=[
                    "Sélectionner des filtres",
                    "Afficher les recettes filtrées",
                    "Réinitialiser les filtres",
                    "Retourner au menu principal",
                ],
            ).execute()

            if choix == "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue("Type du filtre")

            elif choix == "Afficher les recettes filtrées":
                from view.utilisateur.liste_recettes_utilisateur_vue import (
                    ListeRecettesUtilisateurVue,
                )

                return ListeRecettesUtilisateurVue("Affichage de la liste des recettes filtrées")

            elif choix == "Réinitialiser les filtres":
                Session().reset_filtres()
                print("\nLes filtres ont été réinitialisés\n")

            else:
                Session().reset_filtres()
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue("Retour au menu principal")
