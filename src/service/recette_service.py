from utils.log_decorator import log

from business_object.recette import Recette
from business_object.origine import Origine
from business_object.categorie import Categorie
from business_object.ingredient import Ingredient

from dao.recette_dao import RecetteDao
from dao.origine_dao import OrigineDao
from dao.ingredient_dao import IngredientDao
from service.ingredient_recette_service import IngredientRecetteService
from service.ingredient_service import IngredientService
from service.categorie_service import CategorieService
from service.origine_service import OrigineService


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
            id_ingredient = IngredientDao().get_id_ingredient_by_name(
                nom_ingredient)
            if id_ingredient:
                ingredient = Ingredient(id_ingredient, nom_ingredient)
                liste_ingredients.append(ingredient)
        id_categorie = CategorieService().get_id_categorie_by_name(
            recette["categorie_recette"])
        id_origine = OrigineService().get_id_origine_by_name(
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
                    nom_categorie=CategorieService().get_nom_categorie_by_id(row["id_categorie"]))
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

    @ log
    def filtrer_recettes(
        self,
            filtres_ingredients: list[str] = None,
            filtres_origines: list[str] = None,
            filtres_categories: list[str] = None
    ) -> list[Recette]:

        liste_filtres_ingredients = None
        liste_filtres_origines = None
        liste_filtres_categories = None

        if filtres_ingredients:
            liste_filtres_ingredients = []
            for ingredient in filtres_ingredients:
                objet_ingredient = Ingredient(
                    id_ingredient=(
                        IngredientService().get_id_ingredient_by_name(
                            ingredient)),
                    nom_ingredient=ingredient)
                liste_filtres_ingredients.append(objet_ingredient)

        if filtres_origines:
            liste_filtres_origines = []
            for origine in filtres_origines:
                objet_origine = Origine(
                    id_origine=OrigineService().get_id_origine_by_name(
                        origine),
                    nom_origine=origine)
                liste_filtres_origines.append(objet_origine)

        if filtres_categories:
            liste_filtres_categories = []
            for categorie in filtres_categories:
                objet_categorie = Categorie(
                    id_categorie=CategorieService().get_id_categorie_by_name(
                        categorie),
                    nom_categorie=categorie)
                liste_filtres_categories.append(objet_categorie)
        res = RecetteDao().filtrer_recettes(liste_filtres_ingredients,
                                            liste_filtres_origines,
                                            liste_filtres_categories)
        liste_recettes = []
        if res:
            for row in res:
                origine = Origine(id_origine=row["id_origine"],
                                  nom_origine=OrigineDao().get_nom_origine_by_id(row["id_origine"]))
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=CategorieService().get_nom_categorie_by_id(row["id_categorie"]))
                recette = Recette(
                    id_recette=row[0]["id_recette"],
                    nom_recette=row[0]["nom_recette"],
                    instructions_recette=row[0]["instructions_recette"],
                    origine_recette=origine,
                    categorie_recette=categorie,
                    ingredients_recette=IngredientRecetteService(
                    ).lister_ingredients_by_recette(row[0]["id_recette"])
                )
                liste_recettes.append(recette)
        return liste_recettes

    @ log
    def trouver_recette(self, nom_recette):
        res = RecetteDao().trouver_recette(nom_recette)
        if res:
            for row in res:
                origine = Origine(id_origine=row["id_origine"],
                                  nom_origine=OrigineDao().get_nom_origine_by_id(row["id_origine"]))
                categorie = Categorie(
                    id_categorie=row["id_categorie"],
                    nom_categorie=CategorieService().get_nom_categorie_by_id(row["id_categorie"]))
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

    @log
    def get_nom_recette_by_id(self, id_recette: str) -> str:
        """

        Donne le nom de la catégorie à partir de son id.

        Parameters
        ----------
        id_recette: str

        Returns
        -------
        nom_recette: str
            nom de la recette recherchée

        Raises
        ------
        TypeError
            id_recette doit être un str

        """

        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")
        return RecetteDao().get_nom_recette_by_id(id_recette)
