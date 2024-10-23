from view.vue_abstraite import VueAbstraite


class FiltreAbstraitVue(VueAbstraite):
    """Classe abstraite pour les filtres dans l'interface utilisateur."""

    def __init__(self, message=""):
        """
        Initialise la vue des filtres.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)
        self.liste_criteres = []

    def creer_options_menu(self, liste_criteres):
        """Génère les options de menu à partir de la liste des critères."""
        options = [critere.nom for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options
