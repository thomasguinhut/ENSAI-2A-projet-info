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

print(ListeCourseService().lister_ingredient_liste_course(
            "thomas"
            ))