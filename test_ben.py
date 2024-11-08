from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient

from service.origine_service import OrigineService
from service.avis_service import AvisService
from service.ingredient_service import IngredientService
from service.liste_course_service import ListeCourseService
from service.recette_favorite_service import RecetteFavoriteService
from service.categorie_service import CategorieService
from service.recette_service import RecetteService
from service.utilisateur_service import UtilisateurService
from service.ingredient_recette_service import IngredientRecetteService

from dao.origine_dao import OrigineDao
from dao.avis_dao import AvisDao
from dao.liste_course_dao import ListeCourseDao
from dao.ingredient_dao import IngredientDao
from dao.recette_favorite_dao import RecetteFavoriteDao
from dao.categorie_dao import CategorieDao
from dao.recette_dao import RecetteDao
from dao.utilisateur_dao import UtilisateurDao
from dao.ingredient_recette_dao import IngredientRecetteDao

from dao.db_connection import DBConnection

#print(UtilisateurService().se_connecter('thomas','12345'))

#print(OrigineDao().get_id_origine_by_name('mexican'))

print(RecetteService().creer({
        "id_recette": "0",
        "nom_recette": "Salade estivale",
        "instructions_recette": "Mélanger",
        "categorie_recette": "Dessert",
        "origine_recette": "French",
        "ingredients_recette": ["Butter", "Cumin"]
        }))