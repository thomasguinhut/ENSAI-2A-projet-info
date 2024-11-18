from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.historique_vues import HistoriqueVues


class AccueilVue(VueAbstraite):
    """Vue d'accueil de l'application"""

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

        HistoriqueVues().ajouter_vue(self)

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Mode invité",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Se connecter":
                from view.accueil.connexion_vue import ConnexionVue

                return ConnexionVue("Connexion à l'application")

            case "Créer un compte":
                from view.accueil.inscription_vue import InscriptionVue

                return InscriptionVue("Création du compte utilisateur")

            case "Mode invité":
                from view.invite.menu_liste_recettes_invite_vue import MenuListeRecettesInviteVue

                return MenuListeRecettesInviteVue("Mode invité")
