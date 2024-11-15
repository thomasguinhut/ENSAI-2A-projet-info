from InquirerPy import inquirer
from view.liste_recettes_abstraite_vue import ListeRecettesAbstraiteVue
from view.session import Session


class ListeRecettesUtilisateurVue(ListeRecettesAbstraiteVue):
    """Classe pour gérer la vue des recettes d'un utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue de la liste des recettes pour un utilisateur.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de sélection des recettes et gère les choix de l'utilisateur."""
        pages = self.diviser_en_pages()

        if not pages:
            print("Aucune recette disponible.")
            from view.utilisateur.utilisateur_vue import UtilisateurVue

            return UtilisateurVue("Retour au menu principal")

        while True:
            choix = inquirer.select(
                message="Choisissez une recette ou une option :",
                choices=self.creer_options_menu(pages),
            ).execute()

            if choix == "Retourner au menu principal":
                Session().reset_filtres()
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue("Retour au menu principal")
            elif choix == "Page suivante":
                if self.page_actuelle < len(pages) - 1:
                    self.page_actuelle += 1
                self.choisir_menu()
            elif choix == "Page précédente":
                if self.page_actuelle > 0:
                    self.page_actuelle -= 1
                self.choisir_menu()
            else:
                from view.utilisateur.recette_utilisateur_vue import RecetteUtilisateurVue

                return RecetteUtilisateurVue(choix, f"Recette {choix}")
