from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class ConnexionVue(VueAbstraite):
    """Vue de Connexion (saisie de pseudo et mot de passe)"""
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo et mot de passe
        id_utilisateur = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver l'utilisateur
        try:
            utilisateur = UtilisateurService().se_connecter(id_utilisateur, mdp)

            # Si l'utilisateur a été trouvé à partir de ses identifiants de
            # connexion
            print(utilisateur)
            if utilisateur is not None:
                print(utilisateur)
                message = f"Vous êtes connecté sous le pseudo {utilisateur.id_utilisateur}"

                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue(message)

            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        except Exception as e:
            message = f"Une erreur s'est produite : {e}"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
