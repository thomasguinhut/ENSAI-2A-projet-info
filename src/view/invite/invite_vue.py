from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class InviteVue(VueAbstraite):
    """Vue du mode invité."""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Afficher la liste des recettes",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Afficher la liste des recettes":
                from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue

                return ListeRecettesInviteVue("Affichage de la liste des recettes")
