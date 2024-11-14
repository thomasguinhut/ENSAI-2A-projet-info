from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


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
        choix = inquirer.select(
            message="Faites votre choix :",
            choices=[
                "Sélectionner des filtres",
                "Afficher les recettes filtrées",
                "Retourner au menu principal",
            ],
        ).execute()

        match choix:
            case "Sélectionner des filtres":
                from view.filtres.type_filtre_vue import TypeFiltreVue

                return TypeFiltreVue("Type du filtre")

            case "Afficher les recettes filtrées":
                from view.utilisateur.liste_recettes_utilisateur_vue import (
                    ListeRecettesUtilisateurVue,
                )

                return ListeRecettesUtilisateurVue("Affichage de la liste des recettes filtrées")

            case "Retourner au menu principal":
                Session().choix_filtres_ingredient = []
                Session().choix_filtres_origine = []
                Session().choix_filtres_categorie = []
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue("Retour au menu principal")
