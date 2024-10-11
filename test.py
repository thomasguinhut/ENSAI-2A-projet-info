from src.client.ingredient_client import IngredientClient
from src.client.categorie_client import CategorieClient
from src.client.origine_client import OrigineClient


test = OrigineClient()
print(test.get_origine())
