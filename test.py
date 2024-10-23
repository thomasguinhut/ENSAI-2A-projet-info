from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient
from business_object.utilisateur import Utilisateur

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

recette = RecetteService().trouver_recette("Apple Frangipan Tart")
print(recette)
# utilisateur = UtilisateurService().trouver_par_id("1")
# print(utilisateur)
utilisateur = Utilisateur("1", "thomas")
print(RecettesFavoritesDao().ajouter_recette_a_liste(utilisateur, recette))
