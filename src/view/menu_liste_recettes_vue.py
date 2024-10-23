from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class MenuListeRecettes(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Afficher toutes les recettes",
                "Ajouter des filtres",
                "Retour au menu principal"
            ]
            ).execute()

        if Session().utilisateur is None:
            match choix:
                case "Afficher toutes les recettes":
                    from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue

                    return ListeRecettesInviteVue()

                case "Ajouter des filtres":
                    from view.invite.ajouter_filtres_invite_vue import AjouterFiltresInviteVue

                    return AjouterFiltresInviteVue()

                case "Retour au menu principal":
                    from view.invite.invite_vue import InviteVue

                    return InviteVue()

        else:
            match choix:
                case "Afficher toutes les recettes":
                    from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue

                    return ListeRecettesUtilisateurVue()

                case "Ajouter des filtres":
                    from view.utilisateur.ajouter_filtres_utilisateur_vue import AjouterFiltresUtilisateurVue

                    return AjouterFiltresUtilisateurVue()

                case "Retour au menu principal":
                    from view.utilisateur.utilisateur_vue import UtilisateurVue

                    return UtilisateurVue()
