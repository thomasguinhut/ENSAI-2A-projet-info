class Categorie:
    def __init__(self, id_categorie: str, nom_categorie: str):

        if not isinstance(id_categorie, str):
            raise TypeError("id_categorie doit être un str")
        if not isinstance(nom_categorie, str):
            raise TypeError("nom_categorie doit être un str")

        self.id_categorie = id_categorie
        self.nom_categorie = nom_categorie
