from view.vue_abstraite import VueAbstraite
from service.recette_service import RecetteService
from view.session import Session


class ListeRecettesAbstraiteVue(VueAbstraite):
    """Classe abstraite pour les listes de recettes avec des fonctionnalités communes."""

    def __init__(self, message=""):
        """
        Initialise la vue des listes de recettes.

        Args:
            recettes_par_page (int): Nombre de recettes à afficher par page.
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message=message)
        self.liste_recettes = RecetteService().trouver_liste_recettes()
        self.page_actuelle = 0

    def filtrer_recettes(self):
        """Filtre la liste des recettes en fonction des filtres choisis."""
        if [
            Session().choix_filtres_ingredient,
            Session().choix_filtres_origine,
            Session().choix_filtres_categorie
        ] == [[], [], []]:
            return self.liste_recettes
        else:
            return RecetteService().filtrer_recettes(
                Session().choix_filtres_ingredient,
                Session().choix_filtres_origine,
                Session().choix_filtres_categorie
            )

    def diviser_en_pages(self):
        """Divise la liste des recettes filtrées en pages."""
        recettes_filtrees = self.filtrer_recettes()
        return [
            recettes_filtrees[i:(i + 5)]
            for i in range(0, len(recettes_filtrees), 5)
        ]

    def creer_options_menu(self, pages):
        """Crée les options de menu incluant la pagination."""
        options = [recette.nom_recette for recette in pages[self.page_actuelle]]

        if self.page_actuelle > 0:
            options.append("Page précédente")
        if self.page_actuelle < len(pages) - 1:
            options.append("Page suivante")

        options.append("Retourner au menu principal")

        return options

    def afficher_recette(self, nom_recette):
        """Affiche les détails de la recette sélectionnée."""
        recette = next(
            (item for item in self.liste_recettes if item.nom_recette == nom_recette), None)

        if recette is None:
            print(
                f"Erreur: La recette '{nom_recette}' n'a pas été trouvée.")
            return

        print(f"\nDétails de la recette '{recette.nom_recette}':")
        print("\nIngrédients:", recette.ingredients_recette)
        print("\nInstructions:", recette.instructions_recette)
        print("\nCatégorie:", recette.categorie_recette.nom_categorie or "Non spécifiée")
        print("\nOrigine:", recette.origine_recette.nom_origine or "Non spécifiée")
        print("\nAvis:", recette.avis_recette or "Aucun avis")

        input("\nAppuyez sur 'Entrée' pour retourner à la liste des recettes.\n")
