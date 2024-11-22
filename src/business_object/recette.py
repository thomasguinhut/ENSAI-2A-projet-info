from business_object.ingredient import Ingredient
from business_object.categorie import Categorie
from business_object.origine import Origine
from business_object.avis import Avis


class Recette:
    """

    Création de classe Recette.

    La classe Recette est la plus importante, puisqu'elle permet d'implémenter
    les objets les plus couramment utilisés dans l'application.

    Parameters
    ----------
    id_recette : str
    nom_recette : str
    instructions_recette : str
    categorie_recette : Categorie
    origine_recette : Origine
    ingredients_recette : list[Ingredient]
    avis_recette: list[Avis], by default None

    Raises
    ------
    TypeError
        id_recette doit être un str
    TypeError
        nom_recette doit être un str
    TypeError
        instructions_recette doit être un str
    TypeError
        categorie_recette doit être une Catégorie
    TypeError
        origine_recette doit être une Origine
    TypeError
        ingredients_recette doit être une liste
    TypeError
        tout élément de la liste d'ingrédients doit être un Ingrédient
    TypeError
        avis_recette doit être une liste
    TypeError
        tout élément de la liste avis_recette doit être un Avis
    """

    def __init__(
        self,
        id_recette: str,
        nom_recette: str,
        instructions_recette: str,
        categorie_recette: Categorie,
        origine_recette: Origine,
        ingredients_recette: list[Ingredient],
        avis_recette: list[Avis] = None,
    ):
        """

        Constructeur de la classe.

        """

        if not isinstance(id_recette, str):
            raise TypeError("id_recette doit être un str")
        if not isinstance(nom_recette, str):
            raise TypeError("nom_recette doit être un str")
        if not isinstance(instructions_recette, str):
            raise TypeError("instructions_recette doit être un str")
        if not isinstance(categorie_recette, Categorie):
            raise TypeError("categorie_recette doit être une Catégorie")
        if not isinstance(origine_recette, Origine):
            raise TypeError("origine_recette doit être une Origine")
        if not isinstance(ingredients_recette, list):
            raise TypeError("ingredients_recette doit être une liste")
        for i in ingredients_recette:
            if not isinstance(i, Ingredient):
                raise TypeError(f"{i} doit être un Ingrédient")
        if avis_recette:
            if not isinstance(avis_recette, list):
                raise TypeError("avis_recette doit être une liste")
            for i in ingredients_recette:
                if not isinstance(i, Avis):
                    raise TypeError(f"{i} doit être un Avis")

        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.ingredients_recette = ingredients_recette
        self.instructions_recette = instructions_recette
        self.categorie_recette = categorie_recette
        self.origine_recette = origine_recette
        self.avis_recette = avis_recette

    def liste_ingredient_forme_explicite(self):
        """

        Affiche les ingrédients d'une recette à la suite, séparés d'une barre horizontale.

        Returns:
            str: liste des ingrédients

        """
        affichage = ""
        for ingredient in self.ingredients_recette:
            affichage += ingredient.nom_ingredient.capitalize() + " | "
        return affichage[:-2]

    def liste_avis_forme_explicite(self):
        """

        Affiche les avis d'une recette à la suite, séparés d'une barre horizontale.

        Returns:
            str: liste des avis

        """
        affichage = ""
        for avis in self.avis_recette:
            affichage += (
                avis.commentaire + f" ({(avis.note)}/5, publié par {(avis.id_utilisateur)})" + " | "
            )
        return affichage[:-2]
