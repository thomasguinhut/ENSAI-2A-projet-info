from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.categorie_service import CategorieService
from view.session import Session
from InquirerPy import inquirer


class FiltreCategorieVue(FiltreAbstraitVue):
    """Classe pour gérer les filtres par catégorie dans l'interface utilisateur."""

    def __init__(self):
        """
        Initialise la vue des filtres par catégorie.
        """
        super().__init__()
        self.liste_criteres = CategorieService().trouver_liste_categories()

    def choisir_menu(self):
        """Affiche le menu de sélection des filtres par catégorie."""
        choix = inquirer.select(
            message="Choisissez vos filtres:", choices=self.creer_options_menu(self.liste_criteres)
        ).execute()

        if choix == "Retourner au menu des filtres":
            from view.filtres.ajouter_filtres_vue import AjouterFiltresVue

            return AjouterFiltresVue()
        else:
            Session().choix_filtres_categorie.append(choix)
            return self.choisir_menu

    def creer_options_menu(self, liste_criteres):
        """Génère les options de menu à partir de la liste des critères."""
        options = [critere.nom_categorie for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options
