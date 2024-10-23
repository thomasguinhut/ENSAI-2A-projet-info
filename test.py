from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient

from service.origine_service import OrigineService
from service.ingredient_service import IngredientService
from service.categorie_service import CategorieService
from service.recette_service import RecetteService
from service.ingredient_recette_service import IngredientRecetteService
from dao.origine_dao import OrigineDao
from dao.ingredient_recette_dao import IngredientRecetteDao


print(IngredientRecetteService().lister_ingredients_by_recette("52768"))
