from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient
from client.recette_client import RecetteClient

from business_object.recette import Recette
from business_object.categorie import Categorie
from business_object.ingredient import Ingredient
from business_object.origine import Origine

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

exemple = Recette("52768",
"Apple Frangipan Tart", "Preheat the oven to 200C/180C Fan/Gas 6.
Put the biscuits in a large re-sealable freezer bag and bash with a rolling
pin into fine crumbs. Melt the butter in a small pan, then add the biscuit
crumbs and stir until coated with butter. Tip into the tart tin and, using
the back of a spoon, press over the base and sides of the tin to give an even
layer. Chill in the fridge while you make the filling.
Cream together the butter and sugar until light and fluffy. You can do this
in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs,
then add the ground almonds and almond extract and blend until well combined.
Peel the apples, and cut thin slices of apple. Do this at the last minute to
prevent the apple going brown. Arrange the slices over the biscuit base.
Spread the frangipane filling evenly on top. Level the surface and sprinkle
with the flaked almonds.
Bake for 20-25 minutes until golden-brown and set.
Remove from the oven and leave to cool for 15 minutes. Remove the sides of the
tin. An easy way to do this is to stand the tin on a can of beans and push
down gently on the edges of the tin.
Transfer the tart, with the tin base attached, to a serving plate. Serve warm
with cream, crème fraiche or ice cream.,
"2",
"3")

print(IngredientRecetteService().liste_str_ingredient_pour_une_recette(exemple))
print(IngredientRecetteService().lister_ingredients_by_recette("52768"))
