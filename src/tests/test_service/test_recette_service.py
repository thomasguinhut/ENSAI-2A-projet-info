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
        origine_recette=Origine("2", "French"),
        ingredients_recette=[Ingredient("41", "Butter"), Ingredient("104", "Cumin")]
        ),
    Recette(
        id_recette="1",
        nom_recette="Recette1",
        instructions_recette="Verser",
        categorie_recette=Categorie("2", "Dessert"),
        origine_recette=Origine("2", "French"),
        ingredients_recette=[Ingredient("95", "Coriander"), Ingredient("154", "Ginger")]
        ),
    Recette(
        id_recette="2",
        nom_recette="Recette2",
        instructions_recette="Cuire",
        categorie_recette=Categorie("2", "Dessert"),
        origine_recette=Origine("2", "French"),
        ingredients_recette=[Ingredient("305", "Sugar"), Ingredient("333", "CuWatermin")]
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
        "ingredients_recette": ["Butter", "Cumin"]
        }
    RecetteDao().creer = MagicMock(return_value=True)

    # WHEN
    recette = RecetteService().creer(recette_dico)

    # THEN
    assert recette.id_recette == recette_dico["id_recette"]


# def test_creer_echec():
#     """Création de recette échouée
#     (car la méthode RecetteDao().creer retourne False)"""

#     # GIVEN
#     recette_dico = {
#         "id_recette": "0",
#         "nom_recette": "Salade estivale",
#         "instructions_recette": "Mélanger",
#         "categorie_recette": "Dessert",
#         "origine_recette": "French",
#         "ingredients_recette": ["Butter", "Cumin"]
#         }
#     RecetteDao().creer = MagicMock(return_value=True)

#     # WHEN
#     recette = RecetteService().creer(recette_dico)

#     # THEN
#     assert recette.id_recette == recette_dico["id_recette"]


# def test_trouver_liste_recettes():
#     """Lister toutes les recettes"""

#     # GIVEN
#     RecetteDao().trouver_liste_recettes = MagicMock(return_value=liste_recettes)

#     # WHEN
#     res = RecetteService().trouver_liste_recettes()

#     # THEN
#     assert len(res) == 3

# def test_lister_tous_inclure_mdp_true():
#     """Lister les recettes en incluant les mots de passe"""

#     # GIVEN
#     recetteDao().lister_tous = MagicMock(return_value=liste_recettes)

#     # WHEN
#     res = recetteService().lister_tous(inclure_mdp=True)

#     # THEN
#     assert len(res) == 3
#     for recette in res:
#         assert recette.mdp is not None


# def test_lister_tous_inclure_mdp_false():
#     """Lister les recettes en excluant les mots de passe"""

#     # GIVEN
#     recetteDao().lister_tous = MagicMock(return_value=liste_recettes)

#     # WHEN
#     res = recetteService().lister_tous()

#     # THEN
#     assert len(res) == 3
#     for recette in res:
#         assert not recette.mdp


# def test_pseudo_deja_utilise_oui():
#     """Le pseudo est déjà utilisé dans liste_recettes"""

#     # GIVEN
#     pseudo = "lea"

#     # WHEN
#     recetteDao().lister_tous = MagicMock(return_value=liste_recettes)
#     res = recetteService().pseudo_deja_utilise(pseudo)

#     # THEN
#     assert res


# def test_pseudo_deja_utilise_non():
#     """Le pseudo n'est pas utilisé dans liste_recettes"""

#     # GIVEN
#     pseudo = "chaton"

#     # WHEN
#     recetteDao().lister_tous = MagicMock(return_value=liste_recettes)
#     res = recetteService().pseudo_deja_utilise(pseudo)

#     # THEN
#     assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
