from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService
from view.session import Session
from utils.securite import hash_password
from view.historique_vues import HistoriqueVues


class ConnexionVue(VueAbstraite):
    """Vue de Connexion (saisie de pseudo et mot de passe)"""

    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        HistoriqueVues().ajouter_vue(self)

        # Demande à l'utilisateur de saisir pseudo et mot de passe
        id_utilisateur = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()
        mdp = hash_password(mdp, id_utilisateur)

        # Appel du service pour trouver l'utilisateur
        try:
            utilisateur = UtilisateurService().se_connecter(id_utilisateur, mdp)

            # Si l'utilisateur a été trouvé à partir de ses identifiants de
            # connexion
            if utilisateur is not None:
                Session().connexion(utilisateur)
                message = f"Vous êtes connecté sous le pseudo {utilisateur.id_utilisateur}"

                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue(message)

            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        except Exception as e:
            message = f"Une erreur s'est produite : {e}"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
