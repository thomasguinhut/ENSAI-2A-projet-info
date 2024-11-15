from unittest.mock import MagicMock

from service.ingredient_recette_service import IngredientRecetteService

from dao.ingredient_recette_dao import IngredientRecetteDao

# from business_object.recette import Recette
from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.ingredient import Ingredient
from business_object.recette import Recette


def test_creer_ok():
    """ "Création de recette réussie"""

    # GIVEN
    recette_dico = {
        "id_recette": "0",
        "nom_recette": "Salade estivale",
        "instructions_recette": "Mélanger",
        "categorie_recette": "Dessert",
        "origine_recette": "Mexican",
        "ingredients_recette": ["Butter", "Cumin"],
    }
    IngredientRecetteDao().creer = MagicMock(return_value=True)

    # WHEN
    recette = IngredientRecetteService().creer(recette_dico)

    # THEN
    assert recette.id_recette == recette_dico["id_recette"]


def test_creer_echec():
    """Création de recette échouée
    (car la méthode IngredientRecetteDao().creer retourne False)"""

    # GIVEN
    recette_dico = {
        "id_recette": "0",
        "nom_recette": "Salade estivale",
        "instructions_recette": "Mélanger",
        "categorie_recette": "Dessert",
        "origine_recette": "Mexican",
        "ingredients_recette": ["Butter", "Cumin"],
    }
    IngredientRecetteDao().creer = MagicMock(return_value=False)

    # WHEN
    recette = IngredientRecetteService().creer(recette_dico)

    # THEN
    assert recette is None


def test_lister_ingredients_by_recette():
    "Lister tous les ingrédients contenus dans la recette indiquée"

    # GIVEN
    id_recette = "52768"

    # WHEN
    res = IngredientRecetteService().lister_ingredients_by_recette(id_recette)

    # THEN
    assert len(res) == 8


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
