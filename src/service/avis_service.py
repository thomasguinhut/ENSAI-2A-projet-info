from utils.log_decorator import log

from service.recette_service import RecetteService
from service.utilisateur_service import UtilisateurService

from dao.avis_dao import AvisDao


class AvisService:
    """

    Création de la classe AvisService

    """

    @log
    def retirer_avis(self, id_utilisateur: str, nom_recette: str) -> bool:
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
        utilisateur = UtilisateurService().trouver_par_id(id_utilisateur)
        recette = RecetteService().trouver_recette(nom_recette)
        return AvisDao().retirer_avis(utilisateur, recette)

    @log
    def ajouter_avis(
        self, note: int, commentaire: str, id_utilisateur: str, nom_recette: str
    ) -> bool:
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
        utilisateur = UtilisateurService().trouver_par_id(id_utilisateur)
        recette = RecetteService().trouver_recette(nom_recette)
        return AvisDao().ajouter_avis(note, commentaire, utilisateur, recette)
