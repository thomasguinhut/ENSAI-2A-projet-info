from view.vue_abstraite import VueAbstraite
from view.liste_recettes_abstraite_vue import ListeRecettesAbstraiteVue
from service.recette_service import RecetteService

import inquirer


class RecetteInviteVue(VueAbstraite):
    def __init__(self, nom_recette, message=""):
        super().__init__(message)
        self.nom_recette = nom_recette
        self.recette = RecetteService().trouver_recette(nom_recette)

    def afficher_recette_invite(self):
        """Affiche les détails de la recette sélectionnée."""
        ListeRecettesAbstraiteVue.afficher_recette(self.nom_recette)

    def choisir_menu(self):

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
