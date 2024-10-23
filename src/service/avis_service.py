from utils.log_decorator import log

from business_object.utilisateur import Utilisateur
from business_object.recette import Recette

from dao.avis_dao import AvisDao


class AvisService:

    """

    Création de la classe AvisService

    """
    @log
    def retirer_avis(self, utilisateur: Utilisateur, recette: Recette) -> bool:
        """

        Suppression d'un avis d'un utilisateur donné sur une recette donnée.

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur associé à l'avis à supprimer de la base de données

        recette : Recette
            recette associée à l'avis à supprimer de la base de données

        Returns
        -------
            True si l'avis a bien été supprimé

        """
        return AvisDao().supprimer_avis(utilisateur, recette)

    @log
    def ajouter_avis(self, note: int, commentaire: str, utilisateur: Utilisateur, recette: Recette)  -> bool:
        """

        Ajout d'un avis.

        Parameters
        ----------
        avis: Avis
        utilisateur : Utilisateur
        recette : Recette

        Returns
        -------
            True si l'avis a bien été ajouté

        """
        return AvisDao().ajouter_avis(note, commentaire, utilisateur, recette)
