from unittest.mock import MagicMock

from service.origine_service import OrigineService

from dao.origine_dao import OrigineDao

# from business_object.origine import Origine


def test_creer_ok():
    """ "Création de origine réussie"""

    # GIVEN
    id_origine, nom_origine = "0", "Pomme"
    OrigineDao().creer = MagicMock(return_value=True)

    # WHEN
    origine = OrigineService().creer({
        "id_origine": id_origine,
        "nom_origine": nom_origine})

    # THEN
    assert origine.id_origine == id_origine


def test_creer_echec():
    """Création de origine échouée
    (car la méthode OrigineDao().creer retourne False)"""

    # GIVEN
    id_origine, nom_origine = "1", "Poire"
    OrigineDao().creer = MagicMock(return_value=False)

    # WHEN
    origine = OrigineService().creer({
        "id_origine": id_origine,
        "nom_origine": nom_origine
                                        })

    # THEN
    assert origine is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
