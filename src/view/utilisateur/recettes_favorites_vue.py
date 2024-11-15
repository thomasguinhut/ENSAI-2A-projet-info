from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.recette_favorite_service import RecetteFavoriteService
from view.session import Session


class RecettesFavoritesVue(VueAbstraite):
    """Classe pour gérer l'affichage des recettes favorites d'un utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue des recettes favorites.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message=message)
        self.recettes_favorites = RecetteFavoriteService().lister_recette_favorite(
            Session().utilisateur.id_utilisateur
        )

    def choisir_menu(self):
        """Affiche le menu de sélection des recettes favorites."""
        choix = inquirer.select(
            message="Choisissez une recette ou une option :", choices=self.creer_options_menu()
        ).execute()

        if choix == "Retourner au menu principal":
            from view.utilisateur.utilisateur_vue import UtilisateurVue

            return UtilisateurVue("Retour au menu principal")

        else:
            from view.utilisateur.recette_utilisateur_vue import RecetteUtilisateurVue

            return RecetteUtilisateurVue(choix, f"Affichage de la recette {choix}")

    def creer_options_menu(self):
        """Génère la liste des options de menu à partir des recettes favorites."""
        options = [recette.nom_recette for recette in self.recettes_favorites]
        options.append("Retourner au menu principal")
        return options
