from view.filtres.filtre_abstrait_vue import FiltreAbstraitVue
from service.origine_service import OrigineService


class FiltreOrigineVue(FiltreAbstraitVue):
    def __init__(self):
        super().__init__()
        self.liste_criteres = OriginesService.trouver_liste_origines()
