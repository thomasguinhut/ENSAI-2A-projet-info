from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class InviteVue(VueAbstraite):
    """Vue du mode invité."""
    def __init__(self, message=""):
        super().__init__(message)

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
                from view.menu_liste_recettes_vue import MenuListeRecettes

                return MenuListeRecettes()
