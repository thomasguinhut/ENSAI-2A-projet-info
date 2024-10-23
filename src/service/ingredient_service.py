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

    @log
    def get_nom_ingredient_by_id(self, id_ingredient: str) -> str:
        """

        Donne le nom de l'ingrédient à partir de son id.

        Parameters
        ----------
        id_ingredient: str

        Returns
        -------
        nom_ingredient: str
            nom de l'ingrédient recherché

        Raises
        ------
        TypeError
            id_ingredient doit être un str

        """

        if not isinstance(id_ingredient, str):
            raise TypeError("id_origine doit être un str")
        return IngredientDao().get_nom_ingredient_by_id(id_ingredient)

    @log
    def get_id_ingredient_by_name(self, nom_ingredient: str) -> str:
        """

        Donne l'id de l'ingrédient à partir de son nom.

        Parameters
        ----------
        nom_ingredient: str

        Returns
        -------
        id_ingredient: str
            id de l'ingrédient recherché

        Raises
        ------
        TypeError
            nom_ingredient doit être un str

        """

        if not isinstance(nom_ingredient, str):
            raise TypeError("nom_origine doit être un str")
        return IngredientDao().get_id_ingredient_by_name(nom_ingredient)
