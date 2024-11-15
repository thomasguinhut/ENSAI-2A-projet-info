from unittest.mock import MagicMock

from service.recette_service import RecetteService
from service.avis_service import AvisService

from dao.recette_dao import RecetteDao
from dao.avis_dao import AvisDao

# from business_object.recette import Recette
from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.ingredient import Ingredient
from business_object.recette import Recette


def test_retirer_avis_ok():
    """Suppression d'avis réussie"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_recette = "Apple Frangipan Tart"
    AvisDao().retirer_avis = MagicMock(return_value=True)

    # WHEN
    res = AvisService().retirer_avis(id_utilisateur, nom_recette)

    # THEN
    assert res


def test_retirer_avis_echec():
    """Suppression d'avis non aboutie"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_recette = "Apple Frangipan Tart"
    AvisDao().retirer_avis = MagicMock(return_value=False)

    # WHEN
    res = AvisService().retirer_avis(id_utilisateur, nom_recette)

    # THEN
    assert not res


def test_ajouter_avis_ok():
    """Ajout d'avis réussi"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_recette = "Ayam Percik"
    AvisDao().retirer_avis = MagicMock(return_value=True)

    # WHEN
    res = AvisService().retirer_avis(id_utilisateur, nom_recette)

    # THEN
    assert res


def test_ajouter_avis_echec():
    """Ajout d'avis réussi"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_recette = "Ayam Percik"
    AvisDao().retirer_avis = MagicMock(return_value=False)

    # WHEN
    res = AvisService().retirer_avis(id_utilisateur, nom_recette)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
