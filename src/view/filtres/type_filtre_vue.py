from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.historique_vues import HistoriqueVues


class TypeFiltreVue(VueAbstraite):
    """Classe pour sélectionner le type de filtre dans l'interface utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue pour le choix du type de filtre.
        """
        super().__init__(message)

    def choisir_menu(self):
        """Affiche le menu pour choisir le type de filtre."""
        HistoriqueVues().ajouter_vue(self)
        choix = inquirer.select(
            message="Choisissez votre type de filtre:\n\nAttention: les filtres sont inclusifs dans"
            " un même type de filtre et exclusifs entre deux types de filtres différents. Exemple: "
            "les filtres Challots et Butter affichent les recettes contenant du beurre ou des "
            "échallotes tandis que les filtres Butter et Mexican affichent les recettes qui "
            "contiennent du beurre et qui sont mexicaines.\n",
            choices=["Ingrédient", "Catégorie", "Origine", "Retour"],
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
