-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur   SERIAL PRIMARY KEY,
    mdp VARCHAR
);


-----------------------------------------------------
-- Origine
-----------------------------------------------------
DROP TABLE IF EXISTS origine CASCADE ;
CREATE TABLE origine(
    id_origine   SERIAL PRIMARY KEY,
    nom          VARCHAR
);

-----------------------------------------------------
-- Categorie
-----------------------------------------------------
DROP TABLE IF EXISTS categorie CASCADE ;
CREATE TABLE categorie(
    id_categorie    SERIAL PRIMARY KEY,
    nom             VARCHAR
);


-----------------------------------------------------
-- Recette
-----------------------------------------------------
DROP TABLE IF EXISTS recette CASCADE ;
CREATE TABLE recette(
    id_recette   SERIAL PRIMARY KEY,
    nom          VARCHAR,
    instructions VARCHAR,
    id_origine   VARCHAR
    FOREIGN KEY(id_origine) REFERENCES origine(id_origine),
    id_categorie FOREIGN KEY(id_categorie) REFERENCES categorie

);


-----------------------------------------------------
-- Avis
-----------------------------------------------------
DROP TABLE IF EXISTS avis CASCADE ;
CREATE TABLE avis(
    id_avis             SERIAL PRIMARY KEY,
    commentaire         VARCHAR,
    note                NUMERIC,
    id_utilisateur      FOREIGN KEY(id_utilisateur) REFERENCES utilisateur,
    id_recette          FOREIGN KEY(id_recette) REFERENCES recette
);


-----------------------------------------------------
-- Ingrédient
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient CASCADE ;
CREATE TABLE ingredient(
    id_ingredient    SERIAL PRIMARY KEY,
    nom              VARCHAR
);


-----------------------------------------------------
-- Ingrédient recette
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient_recette CASCADE ;
CREATE TABLE ingredient_recette(
    id_recette        FOREIGN KEY(id_recette) REFERENCES recette,
    id_ingredient     FOREIGN KEY(id_ingredient) REFERENCES ingredient
);


-----------------------------------------------------
-- Recette favorite
-----------------------------------------------------
DROP TABLE IF EXISTS recette_favorite CASCADE ;
CREATE TABLE recette_favorite(
    id_utilisateur    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur,
    id_recette        FOREIGN KEY(id_recette) REFERENCES recette
);


-----------------------------------------------------
-- Liste de courses
-----------------------------------------------------
DROP TABLE IF EXISTS liste_course CASCADE ;
CREATE TABLE liste_course(
    id_utilisateur    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur,
    id_ingredient     FOREIGN KEY(id_ingredient) REFERENCES ingredient
);