from src.client.ingredient_client import IngredientClient
from src.client.categorie_client import CategorieClient
from src.client.origine_client import OrigineClient
from src.client.recette_client import RecetteClient
from src.service.origine_service import OrigineService
from src.service.ingredient_service import IngredientService
from src.service.categorie_service import CategorieService
from src.service.recette_service import RecetteService


test = RecetteClient()
test_bis = RecetteService
a = test.get_recette()
b = a[0]
c = test_bis.creer("test", recette=b)
print(c)
