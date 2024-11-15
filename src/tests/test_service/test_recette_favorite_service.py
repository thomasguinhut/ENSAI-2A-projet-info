from unittest.mock import MagicMock

from service.recette_favorite_service import RecetteFavoriteService
from service.utilisateur_service import UtilisateurService
from service.recette_service import RecetteService

from dao.recette_favorite_dao import RecetteFavoriteDao
from dao.utilisateur_dao import UtilisateurDao
from dao.recette_dao import RecetteDao

from business_object.recette import Recette

from business_object.utilisateur import Utilisateur


recette_favorite1 = RecetteService().trouver_recette("Apple Frangipan Tart")
recette_favorite2 = RecetteService().trouver_recette("Ayam Percik")
liste = [recette_favorite1, recette_favorite2]


def test_retirer_favori_ok():
    """
    Suppression de recette en favori réussie
    (car la méthode RecetteFavoriteDao().retirer_favori retourne True)
    """

    # GIVEN
    id_utilisateur = "benjamin"
    nom_recette = "Apple Frangipan Tart"
    RecetteFavoriteDao().retirer_favori = MagicMock(return_value=True)

    # WHEN
    recette_favorite = RecetteFavoriteService().retirer_favori(id_utilisateur, nom_recette)

    # THEN
    assert recette_favorite


def test_retirer_favori_echec():
    """
    Suppression de recette en favori non aboutie
    (car la méthode RecetteFavoriteDao().retirer_favori retourne False)
    """

    # GIVEN
    id_utilisateur = "benjamin"
    nom_recette = "Apple Frangipan Tart"
    RecetteFavoriteDao().retirer_favori = MagicMock(return_value=False)

    # WHEN
    recette_favorite = RecetteFavoriteService().retirer_favori(id_utilisateur, nom_recette)

    # THEN
    assert not recette_favorite


def test_lister_recette_favorite():
    """Lister toutes les recettes favorites d'un utilisateur"""

    # GIVEN
    id_utilisateur = "fany"

    # WHEN
    res = RecetteFavoriteService().lister_recette_favorite(id_utilisateur)

    # THEN
    assert len(res) == 2


def test_ajouter_favori_ok():
    """
    Ajout de recette en favori réussi
    (car la méthode RecetteFavoriteDao().creer retourne True)
    """

    # GIVEN
    id_utilisateur = "toussaint"
    nom_recette = "Apple Frangipan Tart"
    RecetteFavoriteDao().ajouter_favori = MagicMock(return_value=True)

    # WHEN
    recette_favorite = RecetteFavoriteService().ajouter_favori(id_utilisateur, nom_recette)

    # THEN
    assert recette_favorite


def test_ajouter_favori_echec():
    """
    Ajout de recette en favori non abouti
    (car la méthode RecetteFavoriteDao().creer retourne False)
    """

    # GIVEN
    id_utilisateur = "toussaint"
    nom_recette = "Apple Frangipan Tart"
    RecetteFavoriteDao().ajouter_favori = MagicMock(return_value=False)

    # WHEN
    recette_favorite = RecetteFavoriteService().ajouter_favori(id_utilisateur, nom_recette)

    # THEN
    assert not recette_favorite


# def test_ajouter_favori_echec():
#     """
#     Ajout de recette en favori échoué
#     (car la méthode RecetteFavoriteDao().creer retourne False)
#     """

#     # GIVEN
#     id_utilisateur = "benjamin"
#     nom_recette = "Apple Frangipan Tart"
#     utilisateur = UtilisateurDao.trouver_par_id(id_utilisateur)
#     recette = RecetteDao().trouver_recette(nom_recette)
#     RecetteFavoriteDao().ajouter_favori = MagicMock(return_value=False)

#     # WHEN
#     recette_favorite = RecetteFavoriteService().ajouter_favori(utilisateur, recette)

#     # THEN
#     assert not recette_favorite


# def test_supprimer():
#     """ "Création de Joueur réussie"""

#     # GIVEN
#     pseudo, mdp, age, mail, fan_pokemon = "jp", "1234", 15, "z@mail.oo", True
#     JoueurDao().creer = MagicMock(return_value=True)

#     # WHEN
#     joueur = JoueurService().creer(pseudo, mdp, age, mail, fan_pokemon)

#     # THEN
#     assert joueur.pseudo == pseudo


# def test_lister_recette_favorite():
#     """Lister les Joueurs en incluant les mots de passe"""

#     # GIVEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

#     # WHEN
#     res = JoueurService().lister_tous(inclure_mdp=True)

#     # THEN
#     assert len(res) == 3
#     for joueur in res:
#         assert joueur.mdp is not None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
