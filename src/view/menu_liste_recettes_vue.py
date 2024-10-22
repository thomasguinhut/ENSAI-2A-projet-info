from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.session import Session


class MenuListeRecettes(VueAbstraite):
    def choisir_menu(self):
        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Afficher toutes les recettes",
                "Ajouter des filtres",
                "Retour au menu principal"
            ]
            ).execute()

        match choix:
            case "Afficher toutes les recettes":
                if Session().utilisateur is None:
                    from view.invite.liste_recettes_invite_vue import ListeRecettesInviteVue

                    return ListeRecettesInviteVue()
                else:
                    from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue

                    return ListeRecettesUtilisateurVue()

            case "Ajouter des filtres":
                from view.filtres.ajouter_filtres_vue import AjouterFiltresVue

                return AjouterFiltresVue()

            case "Retour au menu principal":
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue()
