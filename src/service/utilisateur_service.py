from tabulate import tabulate

from utils.log_decorator import log
from utils.securite import hash_password

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao


class UtilisateurService:
    """Classe contenant les méthodes de service des Utilisateurs"""

    @log
    def creer(self, id_utilisateur, mdp1, mdp2, favoris) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        if trouver_par_id(self, id_utilisateur) is not None:
            print("Le pseudo existe déjà.")
        elif mdp1 != mdp2:
            print("Les deux mots de passe ne correspondent pas.")
        else:
            nouveau_utilisateur = Utilisateur(
                id_utilisateur=id_utilisateur,
                mdp=hash_password(mdp1, id_utilisateur),
                favoris=favoris,
            )
            return nouveau_utilisateur if UtilisateurDao().creer(nouveau_utilisateur) else None

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """Trouver un utilisateur à partir de son id"""
        return UtilisateurDao().trouver_par_id(id_utilisateur)

    @log
    def modifier(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""

        utilisateur.mdp = hash_password(utilisateur.mdp, utilisateur.id_utilisateur)
        return utilisateur if UtilisateurDao().modifier(Utilisateur) else None

    @log
    def supprimer(self, utilisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return UtilisateurDao().supprimer(utilisateur)

    @log
    def afficher_tous(self) -> str:
        """Afficher tous les utilisateurs
        Sortie : Une chaine de caractères mise sous forme de tableau
        """
        entetes = ["id_utilisateur"]

        utilisateurs = UtilisateurDao().lister_tous()

        for j in utilisateurs:
            if j.id_utilisateur == "admin":
                utilisateurs.remove(j)

        utilisateurs_as_list = [j.as_list() for j in utilisateurs]

        str_utilisateurs = "-" * 100
        str_utilisateurs += "\nListe des joueurs \n"
        str_utilisateurs += "-" * 100
        str_utilisateurs += "\n"
        str_utilisateurs += tabulate(
            tabular_data=utilisateurs_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_utilisateurs += "\n"

        return str_utilisateurs

    @log
    def se_connecter(self, id_utilisateur, mdp) -> Utilisateur:
        """Se connecter à partir de id_utilisateur et mdp"""
        return UtilisateurDao().se_connecter(id_utilisateur, hash_password(mdp, id_utilisateur))

    @log
    def id_utilisateur_deja_utilise(self, id_utilisateur) -> bool:
        """Vérifie si l'id est déjà utilisé
        Retourne True si l'id existe déjà en BDD"""
        utilisateurs = UtilisateurDao().lister_tous()
        return id_utilisateur in [j.id_utilisateur for j in utilisateurs]
