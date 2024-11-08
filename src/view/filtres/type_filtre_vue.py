from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class TypeFiltreVue(VueAbstraite):
    """Classe pour sélectionner le type de filtre dans l'interface utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue pour le choix du type de filtre.
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu pour choisir le type de filtre."""
        choix = inquirer.select(
            message="Choisissez votre type de filtre:",
            choices=[
                "Ingrédient",
                "Catégorie",
                "Origine"
            ]
        ).execute()

        match choix:
            case "Ingrédient":
                from view.filtres.filtre_ingredient_vue import FiltreIngredientVue
                return FiltreIngredientVue()

            case "Catégorie":
                from view.filtres.filtre_categorie_vue import FiltreCategorieVue
                return FiltreCategorieVue()

            case "Origine":
                from view.filtres.filtre_origine_vue import FiltreOrigineVue
                return FiltreOrigineVue()
