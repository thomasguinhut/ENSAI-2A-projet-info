from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.ingredient_service import IngredientService
from view.session import Session
from InquirerPy import inquirer
from view.historique_vues import HistoriqueVues


class FiltreIngredientVue(FiltreAbstraitVue):
    """Classe pour gérer les filtres par ingrédient dans l'interface utilisateur."""

    def __init__(self):
        """Initialise la vue des filtres par ingrédient."""
        super().__init__()
        self.liste_criteres = IngredientService().trouver_liste_ingredients()

    def choisir_menu(self):
        """Affiche le menu de sélection des filtres par ingrédient."""
        HistoriqueVues().ajouter_vue(self)
        choix = inquirer.select(
            message="Choisissez vos filtres:", choices=self.creer_options_menu(self.liste_criteres)
        ).execute()

        if choix == "Retourner au menu des filtres":
            if Session().utilisateur:
                from view.utilisateur.ajouter_filtres_utilisateur_vue import (
                    AjouterFiltresUtilisateurVue,
                )

                return AjouterFiltresUtilisateurVue()

            else:
                from view.invite.ajouter_filtres_invite_vue import AjouterFiltresInviteVue

                return AjouterFiltresInviteVue()
        else:
            Session().choix_filtres_ingredient.append(choix)
            return self.choisir_menu()

    def creer_options_menu(self, liste_criteres):
        """Génère les options de menu à partir de la liste des critères."""
        options = [critere.nom_ingredient for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options
