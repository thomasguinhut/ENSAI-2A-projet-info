from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class UtilisateurVue(VueAbstraite):
    """Vue du menu de l'utilisateur connecté.

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Joueur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Que souhaitez-vous faire : ",
            choices=[
                "Quitter",
                "Afficher la liste des recettes",
                "Gérer les listes",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Afficher la liste des recettes":
                from view.menu_liste_recettes_vue import MenuListeRecettes

                return MenuListeRecettes()

            case "Gérer les listes":
                from view.utilisateur.gestion_listes_vue import GestionListesVue

                return GestionListesVue()
