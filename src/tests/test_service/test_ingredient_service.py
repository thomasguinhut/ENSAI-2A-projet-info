from unittest.mock import MagicMock

from service.ingredient_service import IngredientService

from dao.ingredient_dao import IngredientDao

# from business_object.ingredient import Ingredient


def test_creer_ok():
    """ "Création de Ingredient réussie"""

    # GIVEN
    id_ingredient, nom_ingredient = "0", "Pomme"
    IngredientDao().creer = MagicMock(return_value=True)

    # WHEN
    ingredient = IngredientService().creer({
        "id_ingredient": id_ingredient,
        "nom_ingredient": nom_ingredient})

    # THEN
    assert ingredient.id_ingredient == id_ingredient


def test_creer_echec():
    """Création de Ingredient échouée
    (car la méthode IngredientDao().creer retourne False)"""

    # GIVEN
    id_ingredient, nom_ingredient = "1", "Poire"
    IngredientDao().creer = MagicMock(return_value=False)

    # WHEN
    ingredient = IngredientService().creer({
        "id_ingredient": id_ingredient,
        "nom_ingredient": nom_ingredient
                                        })

    # THEN
    assert ingredient is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
