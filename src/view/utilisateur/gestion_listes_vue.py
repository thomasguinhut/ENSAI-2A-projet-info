from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class GestionListesVue(VueAbstraite):
    """Classe pour gérer la vue des listes et recettes de l'utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue de gestion des listes.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de choix pour la gestion des listes."""
        choix = inquirer.select(
            message="Faites votre choix :",
            choices=["Recettes favorites", "Liste de courses", "Retour au menu principal"],
        ).execute()

        match choix:
            case "Recettes favorites":
                from view.utilisateur.recettes_favorites_vue import RecettesFavoritesVue

                return RecettesFavoritesVue("Liste des recettes favorites")

            case "Liste de courses":
                from view.utilisateur.liste_courses_vue import ListeCoursesVue

                return ListeCoursesVue("Liste des courses")

            case "Retour au menu principal":
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue("Retour au menu principal")
