from unittest.mock import MagicMock

from service.utilisateur_service import UtilisateurService

from dao.utilisateur_dao import UtilisateurDao

from business_object.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(id_utilisateur="Ben", mdp="1234"),
    Utilisateur(id_utilisateur="John", mdp="0000"),
    Utilisateur(id_utilisateur="Alice", mdp="abcd"),
]


def test_creer_ok():
    """ Création de l'Utilisateur réussie"""

    # GIVEN
    id_utilisateur, mdp = "Tom", "1235"
    UtilisateurDao().creer = MagicMock(return_value=True)

    # WHEN
    utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

    # THEN
    assert utilisateur is not None


def test_creer_echec():
    """Création de l'Utilisateur échouée
    (car la méthode UtilisateurDao().creer retourne False)"""

    # GIVEN
    id_utilisateur, mdp = "Ben", "1234"
    UtilisateurDao().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

    # THEN
    assert utilisateur is None

def test_trouver_par_id():
    """ Recherche de l'Utilisateur par son id """

    # GIVEN
    id_utilisateur, mdp = "Ben", "1234"
    UtilisateurDao().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(id_utilisateur, mdp)

    # THEN
    assert utilisateur is None


# def test_lister_tous_inclure_mdp_true():
#     """Lister les Joueurs en incluant les mots de passe"""

#     # GIVEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

#     # WHEN
#     res = JoueurService().lister_tous(inclure_mdp=True)

#     # THEN
#     assert len(res) == 3
#     for joueur in res:
#         assert joueur.mdp is not None


# def test_lister_tous_inclure_mdp_false():
#     """Lister les Joueurs en excluant les mots de passe"""

#     # GIVEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

#     # WHEN
#     res = JoueurService().lister_tous()

#     # THEN
#     assert len(res) == 3
#     for joueur in res:
#         assert not joueur.mdp


# def test_pseudo_deja_utilise_oui():
#     """Le pseudo est déjà utilisé dans liste_joueurs"""

#     # GIVEN
#     pseudo = "lea"

#     # WHEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
#     res = JoueurService().pseudo_deja_utilise(pseudo)

#     # THEN
#     assert res


# def test_pseudo_deja_utilise_non():
#     """Le pseudo n'est pas utilisé dans liste_joueurs"""

#     # GIVEN
#     pseudo = "chaton"

#     # WHEN
#     JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
#     res = JoueurService().pseudo_deja_utilise(pseudo)

#     # THEN
#     assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
