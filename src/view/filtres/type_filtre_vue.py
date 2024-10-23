from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class TypeFiltreVue(VueAbstraite):
    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
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

                return FiltreIngredientVue("Ingrédients")

            case "Catégorie":
                from view.filtres.filtre_categorie_vue import FiltreCategorieVue

                return FiltreCategorieVue("Catégories")

            case "Origine":
                from view.filtres.filtre_origine_vue import FiltreOrigineVue

                return FiltreOrigineVue("Origines")
