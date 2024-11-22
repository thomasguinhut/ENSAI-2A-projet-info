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

    def get_id_avis_by_id_utilisateur_id_recette(self, id_utilisateur: str, id_recette: str) -> str:
        if not isinstance(id_utilisateur, str):
            raise TypeError("id_utilisateur doit être un str")
        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")
        return str(AvisDao().get_id_avis_by_id_utilisateur_id_recette(id_utilisateur, id_recette))

    def get_avis_by_id_recette(self, id_recette: str):
        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")
        return AvisDao().get_avis_by_id_recette(id_recette)
