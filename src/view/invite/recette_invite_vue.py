from view.vue_abstraite import VueAbstraite
from service.recette_service import RecetteService

from InquirerPy import inquirer


class RecetteInviteVue(VueAbstraite):
    """Classe pour afficher les détails d'une recette pour un utilisateur invité."""

    def __init__(self, nom_recette, message=""):
        """
        Initialise la vue de la recette pour un invité.

        Args:
            nom_recette (str): Nom de la recette à afficher.
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)
        self.nom_recette = nom_recette
        self.recette = RecetteService().trouver_recette(nom_recette)

    def afficher_recette_invite(self):
        """Affiche les détails de la recette sélectionnée."""
        self.afficher_recette(self.nom_recette)

    def choisir_menu(self):
        """Affiche le menu des options disponibles pour l'utilisateur invité."""
        while True:
            choix = inquirer.select(
                message="Que souhaitez-vous faire ?",
                choices=[
                    "Retourner à la liste des recettes"
                ]
            ).execute()

            if choix == "Retourner à la liste des recettes":
                from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue
                return ListeRecettesInviteVue()
