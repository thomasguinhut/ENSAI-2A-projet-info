from utils.log_decorator import log

from business_object.recette import Recette
from business_object.origine import Origine
from business_object.categorie import Categorie
from business_object.ingredient import Ingredient
from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient

from dao.recette_dao import RecetteDao


class RecetteService:

    """

    Création de classe RecetteService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'pplication en objet de classes métiers. Cela facilite
    ensuite la manipulation des informations.

    """

    @log
    def creer(recette: dict) -> Recette:
        liste_ingredients = []
        for nom_ingredient in recette["ingredients_recette"]:
            id_ingredient = IngredientClient.get_id_ingredient_by_name(
                nom_ingredient)
            if id_ingredient:
                ingredient = Ingredient(id_ingredient, nom_ingredient)
                liste_ingredients.append(ingredient)

        id_categorie = CategorieClient.get_id_categorie_by_name(
            recette["categorie_recette"])
        if id_categorie:
            categorie = Categorie(id_categorie, recette["categorie_recette"])

        id_origine = OrigineClient.get_id_origine_by_name(
            recette["origine_recette"])
        if id_origine:
            origine = Origine(id_origine, recette["origine_recette"])

        nouvelle_recette = Recette(
            id_recette=recette["id_recette"],
            nom_recette=recette["nom_recette"],
            ingredients_recette=liste_ingredients,
            instructions_recette="test",
            categorie_recette=categorie,
            origine_recette=origine,
        )
        if RecetteDao().creer(nouvelle_recette):
            return nouvelle_recette
        else:
            return None

    @log
    def lister_recettes_par_ingredient(self, ingredient) -> list[Recette]:
        res = RecetteDao().lister_recettes_par_ingredient(self, ingredient)
        liste_recettes = []
        if res:
            for row in res:
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recettes"],
                    id_origine=row["id_origine"],
                    id_categorie=row["id_categorie"],
                )
                liste_recettes.append(recette)
        return liste_recettes

    @log
    def lister_recettes_par_categorie(self, categorie) -> list[Recette]:
        res = RecetteDao().lister_recettes_par_categorie(self, categorie)
        liste_recettes = []
        if res:
            for row in res:
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recettes"],
                    id_origine=row["id_origine"],
                    id_categorie=row["id_categorie"],
                )
                liste_recettes.append(recette)
        return liste_recettes

    @log
    def lister_recettes_par_origine(self, origine) -> list[Recette]:
        res = RecetteDao().lister_recettes_par_origine(self, origine)
        liste_recettes = []
        if res:
            for row in res:
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recettes"],
                    id_origine=row["id_origine"],
                    id_categorie=row["id_categorie"],
                )
                liste_recettes.append(recette)
        return liste_recettes
