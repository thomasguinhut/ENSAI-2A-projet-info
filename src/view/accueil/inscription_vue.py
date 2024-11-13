from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator
from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class InscriptionVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo, mot de passe...
        id_utilisateur = inquirer.text(message="Entrez votre pseudo : ").execute()
        if UtilisateurService().id_utilisateur_deja_utilise(id_utilisateur):
            from view.accueil.accueil_vue import AccueilVue
            return AccueilVue(f"Le pseudo {id_utilisateur} est déjà utilisé.")

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        mdp2 = inquirer.secret(
            message="Confirmez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
            ),
        ).execute()

        # Appel du service pour créer l'utilisateur
        if mdp != mdp2:
            return InscriptionVue("Les deux mots de passe ne sont pas identiques.")
        else:
            utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

        # Si l'utilisateur a été créé
        if utilisateur:
            message = (
                f"Votre compte {utilisateur.id_utilisateur} a été créé. "
                "Vous pouvez maintenant vous connecter."
            )
        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
