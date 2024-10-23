from view.vue_abstraite import VueAbstraite
from view.liste_recettes_abstraite_vue import ListeRecettesAbstraiteVue
from view.session import Session

from service.recette_service import RecetteService

from InquirerPy import inquirer


class RecetteUtilisateurVue(VueAbstraite):
    def __init__(self, nom_recette):
        self.nom_recette = nom_recette
        self.recette = trouver_recette(nom_recette)

    def afficher_recette_utilisateur(self):
        """Affiche les détails de la recette sélectionnée et propose des
        options pour l'utilisateur connecté."""

        ListeRecettesAbstraiteVue.afficher_recette(self.nom_recette)

        self.choisir_menu()

    def choisir_menu(self):
        id_utilisateur = Session().utilisateur.id_utilisateur

        while True:
            choix = inquirer.select(
                message="Que souhaitez-vous faire ?",
                choices=[
                    "Ajouter aux favoris",
                    "Retirer des favoris",
                    "Ajouter un avis",
                    "Retirer un avis",
                    "Ajouter les ingrédients à la liste de courses",
                    "Retourner à la liste des recettes"
                ]
            ).execute()

            if choix == "Ajouter aux favoris":
                ajouter_favori(id_utilisateur, self.recette)
                print(f"La recette '{self.recette.nom}' a été ajoutée aux favoris.")
            
            elif choix == "Retirer des favoris":
                retirer_favori(id_utilisateur, self.recette)
                print(f"La recette '{self.recette.nom}' a été retirée des favoris.")

            elif choix == "Ajouter un avis":
                note = input("Entrez une note entre 1 et 5 : ")
                commentaire = input("Entrez un commentaire : ")
                ajouter_avis(id_utilisateur, self.recette, note, commentaire)
                print(f"Votre avis a été ajouté à la recette '{self.recette.nom}'.")

            elif choix == "Retirer un avis":
                retirer_avis(id_utilisateur, self.recette)
                print(f"Votre avis a été retiré de la recette '{self.recette.nom}'.")

            elif choix == "Ajouter les ingrédients à la liste de courses":
                ajouter_ingredients_courses(id_utilisateur, self.recette)
                print(f"Les ingrédients de la recette '{self.recette.nom}' ont été ajoutés à la liste de courses.")

            elif choix == "Retourner à la liste des recettes":
                from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue

                return ListeRecettesUtilisateurVue()
