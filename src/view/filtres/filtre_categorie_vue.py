from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.categorie_service import CategorieService


class FiltreCategorieVue(FiltreAbstraitVue):
    def __init__(self):
        super().__init__()
        self.liste_criteres = CategorieService.trouver_liste_categories()
