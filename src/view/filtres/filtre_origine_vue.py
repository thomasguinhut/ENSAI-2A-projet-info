from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.origine_service import OrigineService
from view.session import Session
from InquirerPy import inquirer


class FiltreOrigineVue(FiltreAbstraitVue):
    """Classe pour gérer les filtres par origine dans l'interface utilisateur."""

    def __init__(self):
        """
        Initialise la vue des filtres par origine.
        """
        super().__init__()
        self.liste_criteres = OrigineService().trouver_liste_origines()

    def choisir_menu(self):
        """Affiche le menu de sélection des filtres par origine."""
        choix = inquirer.select(
            message="Choisissez vos filtres:", choices=self.creer_options_menu(self.liste_criteres)
        ).execute()

        if choix == "Retourner au menu des filtres":
            from view.filtres.ajouter_filtres_vue import AjouterFiltresVue

            return AjouterFiltresVue()
        else:
            Session().choix_filtres_origine.append(choix)
            return self.choisir_menu

    def creer_options_menu(self, liste_criteres):
        """Génère les options de menu à partir de la liste des critères."""
        options = [critere.nom_origine for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options
