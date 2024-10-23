from utils.log_decorator import log

from business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao


class IngredientService:

    """

    Création de classe IngredientService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application en rapport avec les ingrédients des recettes
    en objet de la classe Ingrédient. Cela facilite ensuite la
    manipulation des informations.

    """

    @log
    def creer(self, ingredient: dict[str, str]) -> Ingredient:
        """

        Crée un Ingrédient.

        Parameters
        ----------
        ingredient : dict[id_ingredient: str, nom_ingredient: str]
            On utilise l'output de la méthode get_ingredient() présente dans
            la classe IngredientClient.

        Returns
        -------
        Ingredient

        """

        nouvel_ingredient = Ingredient(
            id_ingredient=ingredient["id_ingredient"],
            nom_ingredient=ingredient["nom_ingredient"]
        )
        if IngredientDao().creer(ingredient=nouvel_ingredient):
            return nouvel_ingredient
        else:
            return None

    @log
    def trouver_liste_ingredients(self) -> list[Ingredient]:
        """

        Affiche tous les ingrédients de la base de données.

        Returns
        -------
        list[Ingredient]

        """

        res = IngredientDao().trouver_liste_ingredients()
        liste_ingredients = []
        if res:
            for row in res:
                ingredient = Ingredient(
                    id_ingredient=row["id_ingredient"],
                    nom_ingredient=row["nom_ingredient"],
                )
                liste_ingredients.append(ingredient)
        return liste_ingredients
