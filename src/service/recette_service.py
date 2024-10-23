from utils.log_decorator import log

from business_object.recette import Recette
from business_object.origine import Origine
from business_object.categorie import Categorie
from business_object.ingredient import Ingredient
from client.ingredient_client import IngredientClient
from client.categorie_client import CategorieClient
from client.origine_client import OrigineClient

from dao.recette_dao import RecetteDao
from dao.origine_dao import OrigineDao
from service.ingredient_recette_service import IngredientRecetteService


class RecetteService:

    """

    Création de classe RecetteService.

    Cette classe, qui ne contient que des méthodes, transforme toute
    donnée de l'application qui sont des recettes en objet de la classe
    Recette. Cela facilite ensuite la manipulation des informations.

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
            id_ingredient = IngredientClient().get_id_ingredient_by_name(
                nom_ingredient)
            if id_ingredient:
                ingredient = Ingredient(id_ingredient, nom_ingredient)
                liste_ingredients.append(ingredient)
        id_categorie = CategorieClient().get_id_categorie_by_name(
            recette["categorie_recette"])
        id_origine = OrigineClient().get_id_origine_by_name(
            recette["origine_recette"]
            )
        if id_categorie and id_origine:
            print(id_categorie)
            print(id_origine)
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
            if RecetteDao().creer(nouvelle_recette):
                return nouvelle_recette
            else:
                return None

    @log
    def trouver_liste_recettes(self) -> list[Recette]:
        """

        Affiche toutes les recettes de la base de données.

        Returns
        -------
        list[Recette]

        """

        res = RecetteDao().trouver_liste_recettes()
        liste_recettes = []
        if res:
            for row in res:
                origine = Origine(id_origine=row["id_origine"],
                                  nom_origine=OrigineDao().get_nom_origine_by_id(row["id_origine"]))
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=CategorieClient().get_nom_categorie_by_id(row["id_categorie"]))
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recette"],
                    origine_recette=origine,
                    categorie_recette=categorie,
                    ingredients_recette=IngredientRecetteService(
                    ).lister_ingredients_by_recette(row["id_recette"])
                )
                liste_recettes.append(recette)
        return liste_recettes

    @log
    def liste_recettes_par_filtres(
        self,
            filtres_ingredients: list[Ingredient] = None,
            filtres_origines: list[Origine] = None,
            filtres_categories: list[Categorie] = None
    ) -> list[Recette]:
        res = RecetteDao().liste_recettes_par_filtres(filtres_ingredients,
                                                      filtres_origines,
                                                      filtres_categories)
        liste_recettes = []
        if res:
            for row in res:
                origine = Origine(id_origine=row["id_origine"],
                                  nom_origine=OrigineDao().get_nom_origine_by_id(row["id_origine"]))
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=CategorieClient().get_nom_categorie_by_id(row["id_categorie"]))
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recette"],
                    origine_recette=origine,
                    categorie_recette=categorie,
                    ingredients_recette=IngredientRecetteService(
                    ).lister_ingredients_by_recette(row["id_recette"])
                )
                liste_recettes.append(recette)
        return liste_recettes

    @log
    def trouver_recette(self, nom_recette):
        res = RecetteDao().trouver_recette(nom_recette)
        if res:
            for row in res:
                origine = Origine(id_origine=row["id_origine"],
                                  nom_origine=OrigineDao().get_nom_origine_by_id(row["id_origine"]))
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=CategorieClient().get_nom_categorie_by_id(row["id_categorie"]))
                recette = Recette(
                    id_recette=row["id_recette"],
                    nom_recette=row["nom_recette"],
                    instructions_recette=row["instructions_recette"],
                    origine_recette=origine,
                    categorie_recette=categorie,
                    ingredients_recette=IngredientRecetteService(
                    ).lister_ingredients_by_recette(row["id_recette"])
                )
        return recette
