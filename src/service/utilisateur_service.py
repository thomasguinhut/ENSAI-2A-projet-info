from tabulate import tabulate

from utils.log_decorator import log
from utils.securite import hash_password

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
from service.recettes_favorites_service import RecettesFavoritesService
from service.liste_course_service import ListeCourseService


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
        return UtilisateurDao().trouver_par_id(id_utilisateur)

    @log
    def modifier(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""

        utilisateur.mdp = hash_password(
            utilisateur.mdp, utilisateur.id_utilisateur)
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
    def existence_id(self, id_utilisateur) -> bool:
        """Se connecter à partir de id_utilisateur et mdp"""
        return UtilisateurDao().existence_id(id_utilisateur)

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

    @log
    def trouver_utilisateur(self, id_utilisateur):
        res = UtilisateurDao().trouver_par_id(id_utilisateur)
        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],
                mdp_utilisateur=res["mdp_utilisateur"],
                favoris=RecettesFavoritesService().lister_recettes_favorites(res["id_utilisateur"]),
                courses=ListeCourseService().lister_ingredients_liste_course(res["id_utilisateur"])
            )
        return utilisateur