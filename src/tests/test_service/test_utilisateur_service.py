from unittest.mock import MagicMock

from service.utilisateur_service import UtilisateurService

from dao.utilisateur_dao import UtilisateurDao

from business_object.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(id_utilisateur="Ben", mdp="1234"),
    Utilisateur(id_utilisateur="John", mdp="0000"),
    Utilisateur(id_utilisateur="Alice", mdp="abcd"),
]


# def test_creer_ok():
#     """ Création de l'Utilisateur réussie"""

#     # GIVEN
#     id_utilisateur, mdp = "Tom", "1235"
#     UtilisateurDao().creer = MagicMock(return_value=True)

#     # WHEN
#     utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

#     # THEN
#     assert utilisateur is not None


# def test_creer_echec():
#     """Création de l'Utilisateur échouée
#     (car la méthode UtilisateurDao().creer retourne False)"""

#     # GIVEN
#     id_utilisateur, mdp = "Ben", "1234"
#     UtilisateurDao().creer = MagicMock(return_value=False)

#     # WHEN
#     utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

#     # THEN
#     assert utilisateur is None


# def test_trouver_par_id():
#     """ Recherche de l'Utilisateur par son id """

#     # GIVEN
#     id_utilisateur = "thomas"

#     # WHEN
#     utilisateur_trouve = UtilisateurService().trouver_par_id(id_utilisateur)

#     # THEN
#     assert utilisateur_trouve.id_utilisateur == id_utilisateur


# def test_existence_id():
#     """ Vérifie si un id existe dans la base de données """

#     # GIVEN
#     id_utilisateur = "thomas"
   
#     # WHEN
#     utilisateur_trouve = UtilisateurService().existence_id(id_utilisateur)
   
#     # THEN
#     assert utilisateur_trouve


# def test_lister_tous_inclure_mdp_true():
#     """Lister les Utilisateurs en incluant les mots de passe"""

#     # GIVEN
#     nbr_utilisateurs = 3

#     # WHEN
#     res = UtilisateurService().lister_tous()

#     # THEN
#     assert len(res) == nbr_utilisateurs
#     for utilisateur in res:
#         assert utilisateur.mdp is not None

# def test_lister_tous_inclure_mdp_false():
#     """Lister les Utilisateurs en excluant les mots de passe"""

#     # GIVEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

#     # WHEN
#     res = JoueurService().lister_tous()

#     # THEN
#     assert len(res) == 3
#     for joueur in res:
#         assert not joueur.mdp


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
