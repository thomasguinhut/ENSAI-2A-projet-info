from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite

class ListeRecettesVue(VueAbstraite):
    """Vue de la liste des recettes avec pagination."""

    def __init__(self, liste_recettes, recettes_par_page=5):
        self.liste_recettes = liste_recettes
        self.recettes_par_page = recettes_par_page
        self.page_actuelle = 0

    def diviser_en_pages(self):
        """Divise la liste des recettes en pages."""
        return [self.liste_recettes[i:i + self.recettes_par_page] for i in range(0, len(self.liste_recettes), self.recettes_par_page)]

    def choisir_menu(self):
        pages = self.diviser_en_pages()
        while True:
            choix = inquirer.select(
                message="Choisissez une recette ou une option :",
                choices=self.creer_options_menu(pages)
            ).execute()

            if choix == "Retourner au menu principal":
                from view.accueil.accueil_vue import AccueilVue
                return AccueilVue("Retour au menu principal")
            elif choix == "Page suivante":
                self.page_actuelle = min(self.page_actuelle + 1, len(pages) - 1)
            elif choix == "Page précédente":
                self.page_actuelle = max(self.page_actuelle - 1, 0)
            else:
                self.afficher_recette(choix)

    def creer_options_menu(self, pages):
        """Crée les options de menu incluant la pagination."""
        options = [recette["nom"] for recette in pages[self.page_actuelle]] + ["Page précédente", "Page suivante", "Retourner au menu principal"]
        return options

    def afficher_recette(self, nom_recette):
        """Affiche les détails de la recette sélectionnée."""
        # Trouver le dictionnaire correspondant à la recette sélectionnée
        recette = next((item for item in self.liste_recettes if item["nom_recette"] == nom_recette), None)
        
        print(f"\nDétails de la recette '{recette['nom_recette']}':")
        print("Ingrédients:", ", ".join(recette["ingredients"]))
        print("Instructions:", recette["instructions"])
        print("Catégorie:", recette.get("categorie", "Non spécifiée"))
        print("Origine:", recette.get("origine", "Non spécifiée"))
        print("Avis:", recette.get("avis", "Aucun avis"))
        
        input("\nAppuyez sur 'Entrée' pour retourner à la liste des recettes.")
