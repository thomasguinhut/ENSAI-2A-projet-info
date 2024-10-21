from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.recette_service import RecetteService


"""def recuperer_choix_recettes(self):
        recettes_pages = self.liste_recettes[((self.page_actuelle-1)*self.recettes_par_page):(self.page_actuelle*self.recettes_par_page)]
        liste_options = []
        for recette in recettes_pages:
            liste_options.append(recette.nom)"""


class ListeRecettesInviteVue(VueAbstraite):
    """Vue de la liste des recettes avec pagination."""

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


    def choisir_menu(self):
        pages = self.diviser_en_pages()
        if not pages:  
            print("Aucune recette disponible.")
            return

        while True:
            choix = inquirer.select(
                message="Choisissez une recette ou une option :",
                choices=self.creer_options_menu(pages)
            ).execute()

            if choix == "Retourner au menu principal":
                from view.accueil.accueil_vue import AccueilVue
                return AccueilVue("Retour au menu principal")
            elif choix == "Page suivante":
                if self.page_actuelle < len(pages) - 1:
                    self.page_actuelle += 1
                self.choisir_menu()
            elif choix == "Page précédente":
                if self.page_actuelle > 0:
                    self.page_actuelle -= 1
                self.choisir_menu()
            else:
                self.afficher_recette(choix)

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