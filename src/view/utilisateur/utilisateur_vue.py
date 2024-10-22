from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite

from service.utilisateur_service import UtilisateurService


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

                return AccueilVue()

            case "Afficher la liste des recettes":
                from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue()
                return ListeRecettesUtilisateurVue()

            case "Gérer les listes":
                from view.utilisateur.gestion_listes_vue import GestionListesVue

                return GestionListesVue()

