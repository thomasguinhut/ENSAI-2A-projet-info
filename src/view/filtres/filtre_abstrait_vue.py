from view.vue_abstraite import VueAbstraite


class FiltreAbstraitVue(VueAbstraite):
    def __init__(self, filtres=[]):
        self.filtres = self.filtres
      
    def creer_options_menu(self, liste_criteres):
        """Crée les options de menu."""
        options = [critere.nom for critere in self.liste_criteres]
        options.append("Retourner au menu des filtres")
        return options

"""from service.recette_service import RecetteService"""
"""self.recettes_filtrees = RecetteService.trouver_recettes_filtrees(filtres)"""