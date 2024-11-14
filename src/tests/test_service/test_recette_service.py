from unittest.mock import MagicMock

from service.recette_service import RecetteService

from dao.recette_dao import RecetteDao

# from business_object.recette import Recette
from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.ingredient import Ingredient
from business_object.recette import Recette


liste_recettes = [
    Recette(
        id_recette="0",
        nom_recette="Recette0",
        instructions_recette="Mélanger",
        categorie_recette=Categorie("2", "Dessert"),
        origine_recette=Origine("17", "Mexican"),
        ingredients_recette=[Ingredient("41", "Butter"), Ingredient("104", "Cumin")],
    ),
    Recette(
        id_recette="1",
        nom_recette="Recette1",
        instructions_recette="Verser",
        categorie_recette=Categorie("2", "Dessert"),
        origine_recette=Origine("2", "Canadian"),
        ingredients_recette=[Ingredient("95", "Coriander"), Ingredient("154", "Ginger")],
    ),
    Recette(
        id_recette="2",
        nom_recette="Recette2",
        instructions_recette="Cuire",
        categorie_recette=Categorie("2", "Dessert"),
        origine_recette=Origine("2", "Canadian"),
        ingredients_recette=[Ingredient("305", "Sugar"), Ingredient("95", "Coriander")],
    ),
]


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
    RecetteDao().creer = MagicMock(return_value=True)

    # WHEN
    recette = RecetteService().creer(recette_dico)

    # THEN
    assert recette.id_recette == recette_dico["id_recette"]


def test_creer_echec():
    """Création de recette échouée
    (car la méthode RecetteDao().creer retourne False)"""

    # GIVEN
    recette_dico = {
        "id_recette": "0",
        "nom_recette": "Salade estivale",
        "instructions_recette": "Mélanger",
        "categorie_recette": "Dessert",
        "origine_recette": "Mexican",
        "ingredients_recette": ["Butter", "Cumin"],
    }
    RecetteDao().creer = MagicMock(return_value=False)

    # WHEN
    recette = RecetteService().creer(recette_dico)

    # THEN
    assert recette is None


def test_trouver_liste_recettes():
    """Lister toutes les recettes"""

    # WHEN
    res = RecetteService().trouver_liste_recettes()

    # THEN
    assert len(res) == 2


def test_filtrer_recettes():
    """Renvoyer liste des recettes avec les filtres"""

    # GIVEN
    filtres_ingredients = ["Butter"]
    filtres_origines = ["Canadian"]
    filtres_categories = ["Lamb"]

    # WHEN
    res = RecetteService().filtrer_recettes(
        filtres_ingredients, filtres_origines, filtres_categories
    )

    # THEN
    assert len(res) == 1


def test_trouver_recette():
    """Trouver une recette"""

    # GIVEN
    nom_recette = "Apple Frangipan Tart"

    # WHEN
    res = RecetteService().trouver_recette(nom_recette)

    # THEN
    assert res.id_recette == "52768"


def test_get_nom_recette_by_id():
    """Renvoyer le nom de la recette à partir de son id"""

    # GIVEN
    id_recette = "53050"

    # WHEN
    res = RecetteService().get_nom_recette_by_id(id_recette)

    # THEN
    assert res == "Ayam Percik"


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
