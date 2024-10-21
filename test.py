from src.client.ingredient_client import IngredientClient
from src.client.categorie_client import CategorieClient
from src.client.origine_client import OrigineClient
from src.client.recette_client import RecetteClient


test = IngredientClient()
print(test.get_ingredient())
