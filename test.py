from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient
from business_object.utilisateur import Utilisateur
from business_object.ingredient import Ingredient
from business_object.origine import Origine
from business_object.categorie import Categorie

from service.origine_service import OrigineService
from service.ingredient_service import IngredientService
from service.categorie_service import CategorieService
from service.recette_service import RecetteService
from service.utilisateur_service import UtilisateurService
from service.ingredient_recette_service import IngredientRecetteService
from dao.origine_dao import OrigineDao
from dao.ingredient_recette_dao import IngredientRecetteDao
from dao.categorie_dao import CategorieDao
from dao.recette_favorite_dao import RecetteFavoriteDao
from dao.recette_dao import RecetteDao


ingredient = [Ingredient("33", "Bramley Apples")]
origine = [Origine("2", "France")]
categorie = [Categorie("2", "Dessert")]

print(RecetteService().liste_recettes_par_filtres(filtres_ingredients=None,
                                                  filtres_origines=origine,
                                                  filtres_categories=categorie))
