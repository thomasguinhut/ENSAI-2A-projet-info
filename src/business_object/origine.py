class Origine:
    def __init__(self, id_origine: str, nom_origine: str):

        if not isinstance(nom_origine, str):
            raise TypeError("id_origine doit être un str")
        if not isinstance(id_origine, str):
            raise TypeError("nom_origine doit être un str")

        self.id_origine = id_origine
        self.nom_origine = nom_origine
