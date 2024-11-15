from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.liste_course_service import ListeCourseService
from view.session import Session


class ListeCoursesVue(VueAbstraite):
    """Classe pour gérer la vue des listes de courses."""

    def __init__(self, message=""):
        """
        Initialise la vue des listes de courses.

        Args:
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message=message)
        self.liste_courses = ListeCourseService().lister_ingredient_liste_course(
            Session().utilisateur.id_utilisateur
        )

    def choisir_menu(self):
        """Permet à l'utilisateur de choisir un ingrédient à retirer ou une option."""
        if self.liste_courses is None:
            from view.utilisateur.gestion_listes_vue import GestionListesVue

            return GestionListesVue("Aucun ingrédient dans la liste de courses")

        choix = inquirer.select(
            message="Choisissez un ingrédient à retirer de la liste ou une option :",
            choices=self.creer_options_menu(),
        ).execute()

        if choix == "Retourner au menu principal":
            from view.utilisateur.utilisateur_vue import UtilisateurVue

            return UtilisateurVue("Retour au menu principal")
        elif choix == "Retour au menu précédent":
            from view.utilisateur.gestion_listes_vue import GestionListesVue

            return GestionListesVue()
        else:
            ListeCourseService().retirer_ingredient_course(
                Session().utilisateur.id_utilisateur, choix
            )
            print(f"L'ingrédient {choix} a été retiré de votre liste de courses!\n")
            return ListeCoursesVue()

    def creer_options_menu(self):
        """Crée les options de menu à partir des ingrédients de la liste de courses."""
        options = [ingredient.nom_ingredient for ingredient in self.liste_courses]
        options.append("Retour au menu précédent")
        options.append("Retourner au menu principal")
        return options
