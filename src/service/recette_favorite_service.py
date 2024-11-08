from utils.log_decorator import log

from business_object.recette import Recette

from dao.recette_favorite_dao import RecetteFavoriteDao
from service.recette_service import RecetteService


class RecetteFavoriteService:

    """

    Création de classe RecetteFavoriteService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

    """
    @log
    def supprimer(self, nom_recette: str) -> bool:
        """

        Suppression d'une recette de la liste des recettes favorites.

        Parameters
        ----------
        nom_recette : str
            recette à supprimer de la liste des recettes favorites

        Returns
        -------
            True si la recette a bien été supprimée
.
        """
        objet_recette = Recette().str_vers_recette(nom_recette)
        RecetteFavoriteDao().supprimer(objet_recette)

    @log
    def lister_recette_favorite(self, id_utilisateur) -> list[Recette]:
        res = RecetteFavoriteDao().lister_recette_favorite(id_utilisateur)
        liste_recette = []
        if res:
            for row in res:
                nom_recette = RecetteService().get_nom_recette_by_id(
                    row["id_recette"])
                recette = RecetteService().trouver_recette(nom_recette)
                liste_recette.append(recette)
        return liste_recette

    @log
    def ajouter_favori(self, id_utilisateur, nom_recette) -> bool:
        """
        Ajout d'une recette à la liste des recettes favorites de l'utilisateur.

        Parameters
        ----------
        recette : Recette
            recette à ajouter de la liste des recettes favorites
        utilisateur : Utilisateur
            utilisateur dont on modifie la liste des recetttes favorites

        Returns
        -------
            True si la recette a bien été ajoutée
.
        """
        RecetteFavoriteDao().ajouter_recette_a_liste(id_utilisateur, nom_recette)
