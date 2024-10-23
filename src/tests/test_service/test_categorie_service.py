from unittest.mock import MagicMock

from service.categorie_service import CategorieService

from dao.categorie_dao import CategorieDao

from business_object.categorie import Categorie


liste_categories = [
    Categorie(id_categorie="0", nom_categorie="Francais"),
    Categorie(id_categorie="1", nom_categorie="Anglais"),
    Categorie(id_categorie="2", nom_categorie="Américain"),
]


def test_creer_ok():
    """ "Création de Categorie réussie"""

    # GIVEN
    id_categorie, nom_categorie = "3", "Espagnol"
    CategorieDao().creer = MagicMock(return_value=True)

    # WHEN
    categorie = CategorieService().creer({
        "id_categorie": id_categorie,
        "nom_categorie": nom_categorie})

    # THEN
    assert categorie.id_categorie == id_categorie


def test_creer_echec():
    """Création de Categorie échouée
    (car la méthode CategorieDao().creer retourne False)"""

    # GIVEN
    id_categorie, nom_categorie = "3", "Espagnol"
    CategorieDao().creer = MagicMock(return_value=False)

    # WHEN
    categorie = CategorieService().creer({
        "id_categorie": id_categorie,
        "nom_categorie": nom_categorie
                                        })

    # THEN
    assert categorie is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
