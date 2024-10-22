from view.vue_abstraite import VueAbstraite
from service.recette_service import RecetteService


class ListeRecettesAbstraiteVue(VueAbstraite):
    """Classe abstraite pour les listes de recettes avec des fonctionnalités communes."""

    def __init__(self, recettes_par_page=5):
        self.liste_recettes = RecetteService.trouver_liste_recettes()
        self.recettes_par_page = recettes_par_page
        self.page_actuelle = 0

    def diviser_en_pages(self):
        """Divise la liste des recettes en pages."""
        return [
            self.liste_recettes[i:i + self.recettes_par_page]
            for i in range(0, len(self.liste_recettes), self.recettes_par_page)
        ]

    def creer_options_menu(self, pages):
        """Crée les options de menu incluant la pagination."""
        options = [recette.nom for recette in pages[self.page_actuelle]]
        options.append("Page précédente" if self.page_actuelle > 0 else "Fin")
        options.append("Page suivante" if self.page_actuelle < len(pages) - 1 else "Fin")
        options.append("Retourner au menu principal")
        return options

    def afficher_recette(self, nom_recette):
        """Affiche les détails de la recette sélectionnée."""
        recette = next((item for item in self.liste_recettes if item.nom == nom_recette), None)

        if recette is None:
            print(f"Erreur: La recette '{nom_recette}' n'a pas été trouvée.")
            return

        print(f"\nDétails de la recette '{recette.nom}':")
        print("Ingrédients:", ", ".join(recette.ingredients))
        print("Instructions:", recette.instructions)
        print("Catégorie:", recette.categorie or "Non spécifiée")
        print("Origine:", recette.origine or "Non spécifiée")
        print("Avis:", recette.avis or "Aucun avis")

        input("\nAppuyez sur 'Entrée' pour retourner à la liste des recettes.")
