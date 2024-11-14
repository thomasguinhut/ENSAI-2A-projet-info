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


def test_trouver_par_id():
    """ Recherche de l'Utilisateur par son id """

    # GIVEN
    id_utilisateur = "thomas"
    mdp = "12345"
    utilisateur_attendu = Utilisateur(id_utilisateur="thomas", mdp="1234")
    UtilisateurDao().trouver_par_id = MagicMock(return_value=utilisateur_attendu)

    # WHEN
    utilisateur_trouve = UtilisateurService().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur_trouve == utilisateur_attendu


def test_existence_id():
    """ Vérifie si un id existe dans la base de données """

    # GIVEN
    id_utilisateur = "thomas"
    utilisateur_attendu = Utilisateur(id_utilisateur="thomas", mdp="12345")
    print(utilisateur_attendu)
    # WHEN
    utilisateur_trouve = UtilisateurService().trouver_par_id(id_utilisateur)
    print(utilisateur_trouve)
    # THEN
    assert utilisateur_trouve == utilisateur_attendu


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
