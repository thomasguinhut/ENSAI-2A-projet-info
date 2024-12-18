class Avis:
    """

    Création de la classe Avis.

    L'avis est une classe d'association entre Recette et Utilisateur,
    c'est-à-dire qu'elle apporte des infos supplémentaires à la relation
    entre ces deux classes.

    Parameters
    ----------
    id_avis : str
    commentaire : str
    note : int entre 0 et 5
        Note sur 5

    Raises
    ------
    TypeError
        id_avis doit être un str
    TypeError
        commentaire doit être un str
    TypeError
        note doit être un int
    ValueError
        La note doit être comprise entre 0 et 5

    """

    def __init__(self, id_avis: str, commentaire: str, note: int, id_utilisateur: str = None):
        """

        Constructeur de la classe.

        """

        if not isinstance(id_avis, str):
            raise TypeError("id_avis doit être un str")
        if not isinstance(commentaire, str):
            raise TypeError("commentaire doit être un str")
        if not isinstance(note, int):
            raise TypeError("note doit être un int")
        if note > 5 or note < 0:
            raise ValueError("La note doit être comprise entre 0 et 5")

        self.id_avis = str(id_avis)
        self.commentaire = str(commentaire)
        self.note = int(note)
        self.id_utilisateur = str(id_utilisateur)
