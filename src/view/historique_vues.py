class HistoriqueVues:
    """Classe gérant l'historique de navigation."""

    _instance = None

    def __new__(cls):
        """Permet de stocker l'historique à travers l'application"""
        if cls._instance is None:
            cls._instance = super(HistoriqueVues, cls).__new__(cls)
            cls._instance.historique = []
        return cls._instance

    def ajouter_vue(self, vue):
        """Ajoute la vue actuelle à l'historique sans doublons."""
        self.historique.append(vue)

    def retirer_vue(self):
        """Retire la dernière vue visitée de l'historique."""
        if self.historique:
            self.historique.pop()

    def trouver_historique(self):
        return self.historique

    def effacer_historique(self):
        self.historique = []
