from tabulate import tabulate

from utils.log_decorator import log
from utils.securite import hash_password

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao


class UtilisateurService:
    """


    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'pplication en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

    """

    @log
    def creer(self, id_utilisateur, mdp) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        nouveau_utilisateur = Utilisateur(
            id_utilisateur=id_utilisateur,
            mdp=hash_password(mdp, id_utilisateur),
        )
        return nouveau_utilisateur if UtilisateurDao().creer(nouveau_utilisateur) else None

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """Trouver un utilisateur à partir de son id"""
        res = UtilisateurDao().trouver_par_id(id_utilisateur)
        if res is not None:
            utilisateur = Utilisateur(
                id_utilisateur=id_utilisateur,
                mdp=res["mdp"],
            )
            return utilisateur
        return None

    @log
    def existence_id(self, id_utilisateur) -> bool:
        """Se connecter à partir de id_utilisateur et mdp"""
        return UtilisateurDao().existence_id(id_utilisateur)

    @log
    def se_connecter(self, id_utilisateur, mdp) -> Utilisateur:
        """Se connecter à partir de id_utilisateur et mdp"""
        return UtilisateurDao().se_connecter(id_utilisateur, mdp)

    @log
    def id_utilisateur_deja_utilise(self, id_utilisateur) -> bool:
        """Vérifie si l'id est déjà utilisé
        Retourne True si l'id existe déjà en BDD"""
        return UtilisateurService().trouver_par_id(id_utilisateur) is not None
