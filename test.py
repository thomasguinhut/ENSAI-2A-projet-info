from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient
from business_object.utilisateur import Utilisateur
from business_object.ingredient import Ingredient

from service.origine_service import OrigineService
from service.ingredient_service import IngredientService
from service.categorie_service import CategorieService
from service.recette_service import RecetteService
from service.utilisateur_service import UtilisateurService
from service.ingredient_recette_service import IngredientRecetteService
from dao.origine_dao import OrigineDao
from dao.ingredient_recette_dao import IngredientRecetteDao
from dao.categorie_dao import CategorieDao
from dao.recette_favorite_dao import RecettesFavoritesDao
from dao.recette_dao import RecetteDao

<<<<<<< HEAD

ingredient = Ingredient("33", "Bramley Apples")
RecetteDao().liste_recettes_par_filtres(ingredient)
=======
recette = UtilisateurService().trouver_utilisateur("1")
>>>>>>> 96655387fd4417e8c24d1ee2779e0257d3ff6528
