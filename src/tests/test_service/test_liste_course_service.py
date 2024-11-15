from unittest.mock import MagicMock

from service.recette_service import RecetteService
from service.liste_course_service import ListeCourseService

from dao.recette_dao import RecetteDao
from dao.liste_course_dao import ListeCourseDao

# from business_object.recette import Recette
from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.ingredient import Ingredient
from business_object.recette import Recette


def test_lister_ingredient_liste_course():
    """Lister les ingrédients de la liste de courses"""

    # GIVEN
    id_utilisateur = "thomas"

    # WHEN
    res = ListeCourseService().lister_ingredient_liste_course(id_utilisateur)

    # THEN
    assert len(res) == 1


def test_ajouter_ingredients_courses_ok():
    """Ajout des ingrédients à la liste de courses réussi"""

    # GIVEN
    id_utilisateur = "benjamin"
    nom_recette = "Apple Frangipan Tart"
    ListeCourseDao().ajouter_ingredients_courses = MagicMock(return_value=True)

    # WHEN
    res = ListeCourseService().ajouter_ingredients_courses(id_utilisateur, nom_recette)

    # THEN
    assert res


def test_ajouter_ingredients_courses_echec():
    """Ajout des ingrédients à la liste de courses non abouti"""

    # GIVEN
    id_utilisateur = "benjamin"
    nom_recette = "Apple Frangipan Tart"
    ListeCourseDao().ajouter_ingredients_courses = MagicMock(return_value=False)

    # WHEN
    res = ListeCourseService().ajouter_ingredients_courses(id_utilisateur, nom_recette)

    # THEN
    assert not res


def test_supprimer_ok():
    """Suppression d'un ingrédient d'une liste de courses réussie"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_ingredient = "Chicken Thighs"
    ListeCourseDao().supprimer = MagicMock(return_value=True)

    # WHEN
    res = ListeCourseService().retirer_ingredient_course(id_utilisateur, nom_ingredient)

    # THEN
    assert res


def test_supprimer_echec():
    """Suppression d'un ingrédient d'une liste de courses non aboutie"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_ingredient = "Chicken Thighs"
    ListeCourseDao().supprimer = MagicMock(return_value=False)

    # WHEN
    res = ListeCourseService().retirer_ingredient_course(id_utilisateur, nom_ingredient)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
