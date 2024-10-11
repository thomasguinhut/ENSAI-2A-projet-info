from view.vue_abstraite import VueAbstraite


class ListeRecettesVue(VueAbstraite):
    """Vue de la liste des recettes."""

    def __init__(self, recettes):
        self.recettes = recettes

    def choisir_menu(self):
        while True:
            # Affiche les recettes et permet à l'utilisateur d'en choisir une
            choix = inquirer.select(
                message="Choisissez une recette ou retournez au menu précédent :",
                choices=["Retourner au menu principal"] + self.recettes,
            ).execute()

            if choix == "Retourner au menu principal":
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue("Retour au menu principal")

            self.afficher_recette(choix)

    def afficher_recette(self, recette):
        # Affiche les détails de la recette sélectionnée
        print(f"\nDétails de la recette '{recette}':")
        print("Instructions : ")
        input("\nAppuyez sur 'Entrée' pour retourner à la liste des recettes.")
