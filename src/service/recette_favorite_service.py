from utils.log_decorator import log

from business_object.recette import Recette

from dao.recette_favorite_dao import RecetteFavoriteDao


class RecetteFavoriteService:

    """

    Création de classe RecetteFavoriteService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

    """
    @log
    def supprimer(self, recette: str) -> bool:
        """
        
        Suppression d'une recette de la liste des recettes favorites.

        Parameters
        ----------
        recette : str
            recette à supprimer de la liste des recettes favorites

        Returns
        -------
            True si la recette a bien été supprimée
.
        """
        objet_recette = Recette().str_vers_recette(recette)
        return RecetteFavoriteDao().supprimer(objet_recette)

    @log
    def lister_recettes_favorites(self, utilisateur) -> list[Recette]:
        res = RecetteFavoriteDao().lister_recettes_favorites(self, utilisateur)
        liste_recettes = []
        if res:
            for row in res:
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recettes"],
                    id_origine=row["id_origine"],
                    id_categorie=row["id_categorie"],
                )
                liste_recettes.append(recette)
        return liste_recettes
