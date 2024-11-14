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
