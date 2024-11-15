from InquirerPy import inquirer
from view.liste_recettes_abstraite_vue import ListeRecettesAbstraiteVue
from view.session import Session


class ListeRecettesInviteVue(ListeRecettesAbstraiteVue):
    """Classe pour gérer la vue de la liste des recettes pour un utilisateur invité."""

    def __init__(self, message=""):
        """
        Initialise la vue de la liste des recettes pour un invité.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu de sélection des recettes et gère les choix de l'utilisateur."""
        pages = self.diviser_en_pages()
        if not pages:
            print("Aucune recette disponible.")
            return

        while True:
            choix = inquirer.select(
                message="Choisissez une recette ou une option :",
                choices=self.creer_options_menu(pages),
            ).execute()

            if choix == "Retourner au menu principal":
                Session().reset_filtres()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue("Retour au menu principal")

            if choix == "Page suivante" and self.page_actuelle < len(pages) - 1:
                self.page_actuelle += 1
            elif choix == "Page précédente" and self.page_actuelle > 0:
                self.page_actuelle -= 1
            elif choix not in ["Page suivante", "Page précédente"]:
                self.afficher_recette(choix)
                self.choisir_menu()
            else:
                self.choisir_menu()
