from datetime import datetime

from utils.singleton import Singleton


class Session(metaclass=Singleton):
    """Stocke les données liées à une session."""

    def __init__(self):
        """Création de la session"""
        self.utilisateur = None
        self.debut_connexion = None
        self.choix_filtres_ingredient = []
        self.choix_filtres_origine = []
        self.choix_filtres_categorie = []

    def connexion(self, utilisateur):
        """Enregistement des données en session"""
        self.utilisateur = utilisateur
        self.debut_connexion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def deconnexion(self):
        """Suppression des données de la session"""
        self.utilisateur = None
        self.debut_connexion = None
        self.reset_filtres()

    def reset_filtres(self):
        self.choix_filtres_ingredient = []
        self.choix_filtres_origine = []
        self.choix_filtres_categorie = []

    def afficher(self) -> str:
        """Afficher les informations de connexion"""
        res = "Actuellement en session :\n"
        res += "-------------------------\n"
        for att in list(self.__dict__.items()):
            res += f"{att[0]} : {att[1]}\n"

        return res
