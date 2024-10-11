import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator


from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class InscriptionVue(VueAbstraite):
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

    def verifier_2mdp(mdp, mdp2):
        if mdp != mdp2:
            return InscriptionVue(f"Les deux mots de passe ne sont pas identiques.")
        else:
            return True

        # Appel du service pour créer l'utilisateur
        if verifier_2mdp:
            utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

        # Si l'utilisateur a été créé
        if utilisateur:
            message = f"Votre compte {utilisateur.id_utilisateur} a été créé. Vous pouvez maintenant vous connecter."
        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
