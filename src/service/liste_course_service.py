from utils.log_decorator import log

from business_object.ingredient import Ingredient

from service.utilisateur_service import UtilisateurService

from dao.liste_course_dao import ListeCourseDao


class ListeCourseService:

    """

    Création de classe ListeCourseservice.

    """

    @log
    def lister_ingredient_liste_course(self, id_utilisateur) -> list[Ingredient]:
        utilisateur = UtilisateurService().trouver_par_id(id_utilisateur)
        res = ListeCourseDao().lister_ingredients_liste_course(utilisateur)
        liste_ingredients = []
        if res:
            for row in res:
                ingredient = Ingredient(
                    id_ingredient=row["id_ingredient"],
                    nom_ingredient=row["nom_ingredient"],
                )

                liste_ingredients.append(ingredient)
            return liste_ingredients
        else:
            return None
