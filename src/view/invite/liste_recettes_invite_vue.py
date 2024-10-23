from InquirerPy import inquirer
from view.liste_recettes_abstraite_vue import ListeRecettesAbstraiteVue

"""def recuperer_choix_recettes(self):
        recettes_pages = self.liste_recettes[((self.page_actuelle-1)*self.recettes_par_page):(self.page_actuelle*self.recettes_par_page)]
        liste_options = []
        for recette in recettes_pages:
            liste_options.append(recette.nom)"""


class ListeRecettesInviteVue(ListeRecettesAbstraiteVue):

    def __init__(self, message=""):
        super().__init__(message)

    def choisir_menu(self):
        pages = self.diviser_en_pages()
        if not pages:
            print("Aucune recette disponible.")
            return

        while True:
            choix = inquirer.select(
                message="Choisissez une recette ou une option :",
                choices=ListeRecettesAbstraiteVue().creer_options_menu(pages)
            ).execute()

            if choix == "Retourner au menu principal":
                from view.accueil.accueil_vue import AccueilVue
                return AccueilVue("Retour au menu principal")
            elif choix == "Page suivante":
                if self.page_actuelle < len(pages) - 1:
                    self.page_actuelle += 1
                self.choisir_menu()
            elif choix == "Page précédente":
                if self.page_actuelle > 0:
                    self.page_actuelle -= 1
                self.choisir_menu()
            else:
                from view.invite.recette_invite_vue import RecetteInviteVue

                return RecetteInviteVue(choix, f"Affichage de la recette{choix}")
