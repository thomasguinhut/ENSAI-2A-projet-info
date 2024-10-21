from src.client.ingredient_client import IngredientClient
from src.client.categorie_client import CategorieClient
from src.client.origine_client import OrigineClient
from src.client.recette_client import RecetteClient
from src.service.ingredient_service import IngredientService
from src.service.origine_service import OrigineService


test = IngredientClient()
test_bis = IngredientService
a = test.get_ingredient()
b = a[0]
c = test_bis.creer(self="test", nom_ingredient=b)
print(c)
