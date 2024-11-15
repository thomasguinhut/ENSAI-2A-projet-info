from utils.log_decorator import log

from business_object.recette import Recette
from business_object.origine import Origine
from business_object.categorie import Categorie
from business_object.ingredient import Ingredient
from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient

from dao.ingredient_recette_dao import IngredientRecetteDao
from dao.ingredient_dao import IngredientDao
from dao.categorie_dao import CategorieDao
from dao.origine_dao import OrigineDao


class IngredientRecetteService:
    """

    Création de classe RecetteService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    les recettes en objet de la classe Recette, uniquement pour être ensuite
    utilisé en lien avec la table ingrédients_recettes. Cela facilite
    la manipulation des informations.

    """

    @log
    def creer(self, recette: dict) -> Recette:
        """

        Crée une Recette.

        Parameters
        ----------
        recette : dict[id_recette: str, nom_recette: str,
                       instructions_recette: str,
                       categorie_recette: Categorie,
                       origine_recette: Origine,
                       ingredients_recette : list[Ingredient]]
            On utilise l'output de la méthode get_recette() présente dans
            la classe RecetteClient.

        Returns
        -------
        Recette

        """

        liste_ingredients = []
        for nom_ingredient in recette["ingredients_recette"]:
            id_ingredient = IngredientDao().get_id_ingredient_by_name(nom_ingredient)
            if id_ingredient:
                ingredient = Ingredient(id_ingredient, nom_ingredient)
                liste_ingredients.append(ingredient)

        id_categorie = CategorieDao().get_id_categorie_by_name(recette["categorie_recette"])
        id_origine = OrigineDao().get_id_origine_by_name(recette["origine_recette"])
        if id_categorie and id_origine:
            categorie = Categorie(id_categorie, recette["categorie_recette"])
            origine = Origine(id_origine, recette["origine_recette"])

            nouvelle_recette = Recette(
                id_recette=recette["id_recette"],
                nom_recette=recette["nom_recette"],
                ingredients_recette=liste_ingredients,
                instructions_recette=recette["instructions_recette"],
                categorie_recette=categorie,
                origine_recette=origine,
            )
            if IngredientRecetteDao().creer(nouvelle_recette):
                return nouvelle_recette
            else:
                return None

    # @log
    # def lister_recettes_par_ingredient(self, ingredient) -> list[Recette]:
    #     res = IngredientRecetteDao().lister_recettes_par_ingredient(ingredient)
    #     print(res)
    #     liste_recettes = []
    #     if res:
    #         for row in res:
    #             id_origine = row["id_origine"]
    #             origine = Origine(id_origine, OrigineDao().get_nom_origine_by_id(id_origine))
    #             id_categorie = row["id_categorie"]
    #             categorie = Categorie(
    #                 id_categorie, CategorieDao().get_nom_categorie_by_id(id_categorie)
    #             )
    #             res_ingredients = IngredientRecetteDao().lister_ingredients_by_recette(row["id_recette"])
    #             liste_ingredients_recette = []
    #             for ingredient in res_ingredients.keys():
    #                 ingredient = Ingredient(ingredient, res_ingredients[ingredient])
    #             recette = Recette(
    #                 id_recette=row["id_recette"],
    #                 nom_recette=row["nom_recette"],
    #                 instructions_recette=row["instructions_recette"],
    #                 origine_recette=origine,
    #                 categorie_recette=categorie,
    #                 ingredients_recette=
    #             )
    #             liste_recettes.append(recette)
    #     return liste_recettes

    @log
    def lister_ingredients_by_recette(self, id_recette) -> list[dict]:
        """lister toutes les recettes par ingrédient

        Parameters
        ----------
        id_recette : str

        Returns
        -------
        res : list[dict]
            renvoie une liste de dictionnaire d'ingrédients
        """
        res = IngredientRecetteDao().lister_ingredients_by_recette(id_recette)
        liste_ingredient = []
        if res:
            for row in res:
                ingredient = Ingredient(row["id_ingredient"], row["nom_ingredient"])
                liste_ingredient.append(ingredient)
        return liste_ingredient

    @log
    def liste_str_ingredient_pour_une_recette(self, recette) -> str:
        """renvoie une chaîne de caractère contenant la liste des ingrédients d'une recette

        Parameters
        ----------
        recette : Recette

        Returns
        -------
        res : str
            chaîne de caractères énumérant les différents ingrédients
        """
        liste = IngredientRecetteService().lister_ingredients_by_recette(recette.id_recette)
        res = " a"
        print(liste)
        for ingredient in liste:
            res = res + ingredient.nom_ingredient
        return res
