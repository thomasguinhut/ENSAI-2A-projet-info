import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils.log_init import initialiser_logs

from service.utilisateur_service import UtilisateurService

app = FastAPI(title="Mon webservice")


initialiser_logs("Webservice")

utilisateur_service = UtilisateurService()


@app.get("/utilisateur/", tags=["Utilisateurs"])
async def lister_tous_utilisateurs():
    """Lister tous les utilisateurs
    GET http://localhost/utilisateur
    """
    logging.info("Lister tous les utilisateurs")
    liste_utilisateurs = utilisateur_service.lister_tous()

    liste_model = []
    for utilisateur in liste_utilisateurs:
        liste_model.append(utilisateur)

    return liste_model


@app.get("/utilisateur/{id_utilisateur}", tags=["utilisateurs"])
async def utilisateur_par_id(id_utilisateur: int):
    """Trouver un utilisateur à partir de son id
    GET http://localhost/utilisateur/3
    """
    logging.info("Trouver un utilisateur à partir de son id")
    return utilisateur_service.trouver_par_id(id_utilisateur)


class UtilisateurModel(BaseModel):
    """Définir un modèle Pydantic pour les Utilisateurs"""

    id_utilisateur: int | None = None
    mdp: str


@app.post("/utilisateur/", tags=["Utilisateurs"])
async def creer_utilisateur(j: UtilisateurModel):
    """Créer un utilisateur"""
    logging.info("Créer un utilisateur")
    if utilisateur_service.id_utilisateur_deja_utilise(u.id_utilisateur):
        raise HTTPException(status_code=404, detail="Pseudo déjà utilisé")

    utilisateur = utilisateur_service.creer(u.pseudo, u.mdp)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Erreur lors de la création du utilisateur")

    return utilisateur


@app.put("/utilisateur/{id_utilisateur}", tags=["Utilisateurs"])
def modifier_utilisateur(id_utilisateur: int, u: UtilisateurModel):
    """Modifier un utilisateur"""
    logging.info("Modifier un utilisateur")
    utilisateur = utilisateur_service.trouver_par_id(id_utilisateur)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    utilisateur.pseudo = u.id_utilisateur
    utilisateur.mdp = j.mdp
    utilisateur = utilisateur_service.modifier(utilisateur)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Erreur lors de la modification du utilisateur")

    return f"Utilisateur {u.id_utilisateur} modifié"


@app.delete("/utilisateur/{id_utilisateur}", tags=["Utilisateurs"])
def supprimer_utilisateur(id_utilisateur: int):
    """Supprimer un utilisateur"""
    logging.info("Supprimer un utilisateur")
    utilisateur = utilisateur_service.trouver_par_id(id_utilisateur)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    utilisateur_service.supprimer(utilisateur)
    return f"Utilisateur {utilisateur.pseudo} supprimé"


@app.get("/hello/{name}")
async def hello_name(name: str):
    """Afficher Hello"""
    logging.info("Afficher Hello")
    return f"message : Hello {name}"


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

    logging.info("Arret du Webservice")
