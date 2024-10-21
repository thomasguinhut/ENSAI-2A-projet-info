-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur   VARCHAR PRIMARY KEY,
    mdp VARCHAR
);


-----------------------------------------------------
-- Origine
-----------------------------------------------------
DROP TABLE IF EXISTS origine CASCADE ;
CREATE TABLE origine(
    id_origine   VARCHAR PRIMARY KEY,
    nom_origine   VARCHAR 
);

-----------------------------------------------------
-- Categorie
-----------------------------------------------------
DROP TABLE IF EXISTS categorie CASCADE ;
CREATE TABLE categorie(
    id_categorie    VARCHAR PRIMARY KEY,
    nom_categorie   VARCHAR
);


-----------------------------------------------------
-- Recette
-----------------------------------------------------
DROP TABLE IF EXISTS recette CASCADE ;
CREATE TABLE recette(
    id_recette   VARCHAR PRIMARY KEY,
    nom_recette          VARCHAR,
    instructions_recette VARCHAR,
    id_origine   VARCHAR,
    FOREIGN KEY(id_origine) REFERENCES origine(id_origine),
    id_categorie VARCHAR,
    FOREIGN KEY(id_categorie) REFERENCES categorie(id_categorie)

);


-----------------------------------------------------
-- Avis
-----------------------------------------------------
DROP TABLE IF EXISTS avis CASCADE ;
CREATE TABLE avis(
    id_avis             VARCHAR PRIMARY KEY,
    commentaire         VARCHAR,
    note                NUMERIC,
    id_utilisateur      VARCHAR,
    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    id_recette          VARCHAR,
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette)
);


-----------------------------------------------------
-- Ingrédient
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient CASCADE ;
CREATE TABLE ingredient(
    id_ingredient    VARCHAR PRIMARY KEY,
    nom_ingredient    VARCHAR
);


-----------------------------------------------------
-- Ingrédient recette
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient_recette CASCADE ;
CREATE TABLE ingredient_recette(
    id_recette        VARCHAR,
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette),
    id_ingredient     VARCHAR,
    FOREIGN KEY(id_ingredient) REFERENCES ingredient(id_ingredient)
);


-----------------------------------------------------
-- Recette favorite
-----------------------------------------------------
DROP TABLE IF EXISTS recette_favorite CASCADE ;
CREATE TABLE recette_favorite(
    id_utilisateur    VARCHAR,
    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    id_recette        VARCHAR,
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette)
);


-----------------------------------------------------
-- Liste de courses
-----------------------------------------------------
DROP TABLE IF EXISTS liste_course CASCADE ;
CREATE TABLE liste_course(
    id_utilisateur    VARCHAR,
    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    id_ingredient     VARCHAR,
    FOREIGN KEY(id_ingredient) REFERENCES ingredient(id_ingredient)
);