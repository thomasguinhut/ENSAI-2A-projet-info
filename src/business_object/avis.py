class Avis:
    def __init__(self, id_avis: str, commentaire: str, note: int):

        if not isinstance(id_avis, str):
            raise TypeError("id_avis doit être un str")
        if not isinstance(commentaire, str):
            raise TypeError("commentaire doit être un str")
        if not isinstance(note, str):
            raise TypeError("note doit être un int")

        self.id_avis = id_avis
        self.commentaire = commentaire
        self.note = note
