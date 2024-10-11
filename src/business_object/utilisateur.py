class Utilisateur:

    def __init__(self, id_utilisateur: str, mdp: str, favoris: list):
        self.id_utilisateur = id_utilisateur
        self.mdp = mdp
        self.favoris = favoris
