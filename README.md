# Groupe 20 - Projet info 2A Ensai

Application MyKitchen réalisée par Akmal Ayari,  Toussaint Boco, Thomas Guinhut, Benjamin Lizé et Fanilosoa Rajaona.

## :arrow_forward: Logiciels requis

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.10](https://www.python.org/)
- [Git](https://git-scm.com/)
- Une base de données [PostgreSQL](https://www.postgresql.org/)

---

## :arrow_forward: Clonez le dépôt

- [ ] Ouvrez **Git Bash**
- [ ] Après vous être positionné dans le dossier de votre choix, clonez ce dépôt
  - `git clone git@github.com:thomasguinhut/ENSAI-2A-projet-info.git`

---

## :arrow_forward: Ouvrez le dépôt avec VSCode

- [ ] Ouvrez **Visual Studio Code**
- [ ] File > Open Folder
- [ ] Cliquez une seule fois sur *ENSAI-2A-projet-info-groupe-20* et cliquez sur `Sélectionner un dossier`
  - :warning: Si le dossier parent dans l'explorer VSCode (à gauche) n'est pas *ENSAI-2A-projet-info-groupe-20*, l'application ne fonctionnera pas

### Fichiers de configuration

Ce dépôt contient de nombreux fichiers de configuration pour paramètrer les différents outils utilisés.

| Fichier                      | Description                                                         |
|------------------------------|---------------------------------------------------------------------|
| `.vscode/settings.json`      | Configuration spécifique à Visual Studio Code                       |
| `.github/workflows/ci.yml`   | Définition des workflows GitHub Actions                             |
| `logging_config.yml`         | Configuration du système de journalisation (logging)                |
| `.gitignore`                 | Liste des fichiers et répertoires à ignorer lors des opérations Git |
| `.coveragerc`                | Configuration de l'outil de couverture de code (coverage)           |
| `requirements.txt`           | Liste des dépendances Python requises pour le projet                |

---

## :arrow_forward: Installez les packages nécessaires

Dans VSCode :

- [ ] Ouvrez un terminal *Git Bash*
- [ ] Exécutez la commande ci-dessous

```bash
pip install -r requirements.txt
```

---

## :arrow_forward: Variables d'environnement

Il est nécessaire de définir les variables pour déclarer la base de données et le webservice auxquels vous allez connecter l'application.

À la racine du projet :

- [ ] Créez un fichier nommé `.env` 
- [ ] Collez-y le texte ci-dessous

```default
POSTGRES_HOST=sgbd-eleves.domensai.ecole
POSTGRES_PORT=5432
POSTGRES_DATABASE=idxxxx
POSTGRES_USER=idxxxx
POSTGRES_PASSWORD=idxxxx
POSTGRES_SCHEMA=projet
```

- [ ] Remplaçer les 'xxxx' par votre id Ensai
- [ ] Si vous prévoyez de faire des tests (et donc d'utiliser la base de données projet_test), il est indispensable de revenir à la base de données complètes (donc, de remensionner 'projet' pour la variable POSTGRES_SCHEMA)

---

## :arrow_forward: Lancer le programme

Cette application propose une interface graphique très basique pour naviguer entre différents menus.

- [ ] Dans Git Bash : `python src/__main__.py`
- [ ] Si cela n'a jamais été fait, initialiser les données
  - dans Git Bash : `python src/utils/reset_database.py`
  - vous pouvez faire de même lorsque vous souhaitez réinitialiser les données après avoir modifier la base (ajout d'utilisateurs, de favoris,...)

---

## :arrow_forward: Lancer les tests unitaires

### Initialisation des données tests

- [ ] Il est nécessaire d'initialiser les données test (les tests de cette application ne sont pas appliqués sur la base de données originelle)
  - dans Git Bash : `python src/utils/reset_database_test.py`
  - Ouvrez le fichier .env : pour POSTGRES_SCHEMA, remplaçer 'projet' par 'projet_test'
- [ ] Toujours dans Git Bash : `pytest -v` (ou `python -m pytest -v` si *pytest* n'a pas été ajouté au *PATH*)

### Couverture de tests

Il est également possible de générer la couverture de tests avec [Coverage](https://coverage.readthedocs.io/en/7.4.0/index.html)

:bulb: Le fichier `.coveragerc` permet de modifier le paramétrage

- [ ] dans le terminal python : `coverage run -m pytest`
