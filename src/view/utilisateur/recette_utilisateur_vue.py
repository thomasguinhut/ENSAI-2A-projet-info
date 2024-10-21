from view.vue_abstraite import VueAbstraite

from view.session import Session

class RecetteUtilisateurVue(VueAbstraite):
    def __init__(self, nom_recette):
        self.nom_recette = self.nom_recette

    def afficher_recette(self, nom_recette):
    """Affiche les détails de la recette sélectionnée et propose des options."""
    recette = trouver_recette(nom_recette)
    #recette = next((item for item in self.liste_recettes if item.nom == nom_recette), None)

    if recette is None:
        print(f"Erreur: La recette '{self.nom_recette}' n'a pas été trouvée.")
        return

    print(f"\nDétails de la recette '{recette.nom}':")
    print("Ingrédients:", ", ".join(recette.ingredients))
    print("Instructions:", recette.instructions)
    print("Catégorie:", recette.categorie or "Non spécifiée")
    print("Origine:", recette.origine or "Non spécifiée")
    print("Avis:", recette.avis or "Aucun avis")

    afficher_recette(self.nom_recette)

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
            ajouter_favori(id_utilisateur, recette)
            print(f"La recette '{recette.nom}' a été ajoutée aux favoris.")
        
        elif choix == "Retirer des favoris":
            retirer_favori(id_utilisateur, recette)
            print(f"La recette '{recette.nom}' a été retirée des favoris.")

        elif choix == "Ajouter un avis":
            note = input("Entrez une note entre 1 et 5 : ")
            commentaire = input("Entrez un commentaire : ")
            ajouter_avis(id_utilisateur, recette, note, commentaire)
            print(f"Votre avis a été ajouté à la recette '{recette.nom}'.")

        elif choix == "Retirer un avis":
            retirer_avis(id_utilisateur, recette)
            print(f"Votre avis a été retiré de la recette '{recette.nom}'.")

        elif choix == "Ajouter les ingrédients à la liste de courses":
            ajouter_ingredients_courses(id_utilisateur, recette)
            print(f"Les ingrédients de la recette '{recette.nom}' ont été ajoutés à la liste de courses.")

        elif choix == "Retourner à la liste des recettes":
            from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue()

            return ListeRecettesUtilisateurVue()
