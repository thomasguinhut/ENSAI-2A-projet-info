from view.vue_abstraite import VueAbstraite
from view.session import Session
from view.historique_vues import HistoriqueVues

from service.recette_service import RecetteService
from service.recette_favorite_service import RecetteFavoriteService
from service.avis_service import AvisService
from service.liste_course_service import ListeCourseService

from view.utilisateur.liste_recettes_utilisateur_vue import ListeRecettesUtilisateurVue

from business_object.avis import Avis

from InquirerPy import inquirer


class RecetteUtilisateurVue(VueAbstraite):
    """Classe pour afficher et gérer une recette pour un utilisateur connecté."""

    def __init__(self, nom_recette, message=""):
        """
        Initialise la vue de la recette pour un utilisateur.

        Args:
            nom_recette (str): Nom de la recette à afficher.
            message (str): Message à afficher (par défaut: "").
        """
        super().__init__(message)
        self.nom_recette = nom_recette
        self.recette = RecetteService().trouver_recette(nom_recette)

    def choisir_menu(self):
        """Affiche le menu des options disponibles pour l'utilisateur connecté."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        HistoriqueVues().ajouter_vue(self)

        while True:
            choix = inquirer.select(
                message="Que souhaitez-vous faire ?",
                choices=[
                    "Afficher la recette",
                    "Ajouter aux favoris",
                    "Retirer des favoris",
                    "Ajouter un avis",
                    "Retirer un avis",
                    "Ajouter les ingrédients à la liste de courses",
                    "Retourner au menu précédent",
                    "Retourner au menu principal",
                ],
            ).execute()

            if choix == "Afficher la recette":
                ListeRecettesUtilisateurVue().afficher_recette(self.nom_recette)

                HistoriqueVues().retirer_vue()

                return self

            elif choix == "Ajouter aux favoris":
                if RecetteFavoriteService().get_id_recette_favorite(id_utilisateur) is None:
                    RecetteFavoriteService().ajouter_favori(id_utilisateur, self.nom_recette)
                    print(f"\nLa recette '{self.nom_recette}' a été ajoutée aux favoris.\n")
                elif self.recette.id_recette not in (
                    RecetteFavoriteService().get_id_recette_favorite(id_utilisateur)
                ):
                    RecetteFavoriteService().ajouter_favori(id_utilisateur, self.nom_recette)
                    print(f"\nLa recette '{self.nom_recette}' a été ajoutée aux favoris.\n")
                else:
                    print(f"\nLa recette '{self.nom_recette}' est déjà dans les favoris.\n")

            elif choix == "Retirer des favoris":
                RecetteFavoriteService().retirer_favori(id_utilisateur, self.nom_recette)
                print(f"\nLa recette '{self.nom_recette}' a été retirée des favoris.\n")

            elif choix == "Ajouter un avis":
                if (
                    AvisService().get_id_avis_by_id_utilisateur_id_recette(
                        id_utilisateur, self.recette.id_recette
                    )
                    != "None"
                ):
                    print(f"\nVous avez déjà un avis sur la recette '{self.nom_recette}'\n")
                else:
                    commentaire = input("Entrez un commentaire : ")
                    note = input("Entrez une note entre 1 et 5 : ")
                    try:
                        note = int(note)
                        if note > 5 or note < 0:
                            print("\nLa note doit être un entier compris entre 1 et 5\n")
                        else:
                            id_avis = AvisService().get_id_avis_by_id_utilisateur_id_recette(
                                id_utilisateur, self.recette.id_recette
                            )
                            if self.recette.avis_recette is not None:
                                ancienne_liste = self.recette.avis_recette
                                self.recette.avis_recette = ancienne_liste + Avis(
                                    id_avis, commentaire, note
                                )
                                AvisService().ajouter_avis(
                                    note, commentaire, id_utilisateur, self.nom_recette
                                )
                            else:
                                self.recette.avis_recette = Avis(id_avis, commentaire, note)
                                AvisService().ajouter_avis(
                                    note, commentaire, id_utilisateur, self.nom_recette
                                )

                            print(f"\nVotre avis a été ajouté à la recette '{self.nom_recette}'\n")
                    except ValueError:
                        print("\nLa note doit être un entier compris entre 1 et 5\n")

            elif choix == "Retirer un avis":
                AvisService().retirer_avis(id_utilisateur, self.nom_recette)
                self.recette.avis_recette = None
                print(f"\nVotre avis a été retiré de la recette '{self.nom_recette}'\n")

            elif choix == "Ajouter les ingrédients à la liste de courses":
                ListeCourseService().ajouter_ingredients_courses(id_utilisateur, self.nom_recette)
                print(
                    f"\nLes ingrédients de la recette '{self.nom_recette}' "
                    "ont été ajoutés à la liste de courses.\n"
                )

            elif choix == "Retourner au menu précédent":
                return HistoriqueVues().historique[-2]

            else:
                from view.utilisateur.utilisateur_vue import UtilisateurVue

                return UtilisateurVue("Retour au menu principal")
