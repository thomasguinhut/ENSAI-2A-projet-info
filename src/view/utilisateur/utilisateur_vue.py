from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues


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

    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        HistoriqueVues().ajouter_vue(self)

        choix = inquirer.select(
            message="Que souhaitez-vous faire : ",
            choices=[
                "Afficher la liste des recettes",
                "Gérer les listes",
                "Retour à l'écran d'accueil",
            ],
        ).execute()

        match choix:
            case "Afficher la liste des recettes":
                from view.utilisateur.menu_liste_recettes_utilisateur_vue import (
                    MenuListeRecettesUtilisateurVue,
                )

                return MenuListeRecettesUtilisateurVue()

            case "Gérer les listes":
                from view.utilisateur.gestion_listes_vue import GestionListesVue

                return GestionListesVue()

            case "Retour à l'écran d'accueil":
                Session().deconnexion()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()
