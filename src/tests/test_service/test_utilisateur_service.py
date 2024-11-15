from unittest.mock import MagicMock
from tabulate import tabulate

from service.utilisateur_service import UtilisateurService

from dao.utilisateur_dao import UtilisateurDao

from business_object.utilisateur import Utilisateur


def test_creer_ok():
    """Création de l'Utilisateur réussie"""

    # GIVEN
    id_utilisateur, mdp = "Tom", "1235"
    UtilisateurDao().creer = MagicMock(return_value=True)

    # WHEN
    utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

    # THEN
    assert utilisateur is not None


def test_creer_echec():
    """Création de l'Utilisateur échouée
    (car la méthode UtilisateurDao().creer retourne False)"""

    # GIVEN
    id_utilisateur, mdp = "Ben", "1234"
    UtilisateurDao().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

    # THEN
    assert utilisateur is None


def test_trouver_par_id():
    """Recherche de l'Utilisateur par son id"""

    # GIVEN
    id_utilisateur = "thomas"

    # WHEN
    utilisateur_trouve = UtilisateurService().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur_trouve.id_utilisateur == id_utilisateur


def test_existence_id():
    """Vérifie si un id existe dans la base de données"""

    # GIVEN
    id_utilisateur = "thomas"

    # WHEN
    utilisateur_trouve = UtilisateurService().existence_id(id_utilisateur)

    # THEN
    assert utilisateur_trouve


def test_se_connecter():
    """Connexion avec l'id et le mdp réussie"""

    # GIVEN
    id_utilisateur = "thomas"
    mdp = "12345"
    utilisateur = Utilisateur(id_utilisateur=id_utilisateur, mdp=mdp)
    UtilisateurDao().se_connecter = MagicMock(return_value=utilisateur)

    # WHEN
    res = UtilisateurService().se_connecter(id_utilisateur, mdp)

    # THEN
    assert res.id_utilisateur == id_utilisateur


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
