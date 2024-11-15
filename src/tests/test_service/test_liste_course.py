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


def test_ajouter_ingredients_courses():
    """Ajouter des ingrédients à la liste de courses"""

    # GIVEN
    id_utilisateur = "benjamin"
    nom_recette = "Apple Frangipan Tart"
    ListeCourseDao().ajouter_ingredients_courses = MagicMock(return_value=True)

    # WHEN
    res = ListeCourseService().ajouter_ingredients_courses(id_utilisateur, nom_recette)

    # THEN
    assert res


def test_supprimer():
    """Supprime un ingrédient d'une liste de courses"""

    # GIVEN
    id_utilisateur = "akmal"
    nom_ingredient = "Chicken Thighs"
    ListeCourseDao().supprimer = MagicMock(return_value=True)

    # WHEN
    res = ListeCourseService().supprimer(id_utilisateur, nom_ingredient)

    # THEN
    assert res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
