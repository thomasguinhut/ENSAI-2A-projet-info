-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur   VARCHAR PRIMARY KEY,
    mdp VARCHAR NOT NULL
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
    instructions_recette TEXT,
    id_origine   VARCHAR,
    id_categorie VARCHAR,
    FOREIGN KEY(id_origine) REFERENCES origine(id_origine),
    FOREIGN KEY(id_categorie) REFERENCES categorie(id_categorie)

);


-----------------------------------------------------
-- Avis
-----------------------------------------------------
DROP TABLE IF EXISTS avis CASCADE;

CREATE TABLE avis (
    id_avis SERIAL PRIMARY KEY,            -- Auto-incrémentation de id_avis
    commentaire TEXT,
    note NUMERIC,
    id_utilisateur VARCHAR,                -- Clé étrangère vers la table utilisateur
    id_recette VARCHAR,                    -- Clé étrangère vers la table recette
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette)
);

-----------------------------------------------------
-- Aligner la séquence de id_avis avec les données existantes
-----------------------------------------------------
SELECT setval('avis_id_avis_seq', (SELECT COALESCE(MAX(id_avis), 1) FROM avis) + 1);



-----------------------------------------------------
-- Ingrédient
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient CASCADE ;
CREATE TABLE ingredient(
    id_ingredient    VARCHAR PRIMARY KEY,
    nom_ingredient    VARCHAR NOT NULL
);


-----------------------------------------------------
-- Ingrédient recette
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient_recette CASCADE;
CREATE TABLE ingredient_recette (
    id_recette    VARCHAR,
    id_ingredient VARCHAR,
    PRIMARY KEY (id_recette, id_ingredient),
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette),
    FOREIGN KEY (id_ingredient) REFERENCES ingredient(id_ingredient)
);


-----------------------------------------------------
-- Recette favorite
-----------------------------------------------------
DROP TABLE IF EXISTS recette_favorite CASCADE ;
CREATE TABLE recette_favorite(
    id_utilisateur    VARCHAR,
    id_recette        VARCHAR,
    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    PRIMARY KEY (id_utilisateur, id_recette),
    FOREIGN KEY(id_recette) REFERENCES recette(id_recette)
);


-----------------------------------------------------
-- Liste de courses
-----------------------------------------------------
DROP TABLE IF EXISTS liste_course CASCADE ;
CREATE TABLE liste_course(
    id_utilisateur    VARCHAR,
    id_ingredient     VARCHAR,
    PRIMARY KEY (id_utilisateur, id_ingredient),
    FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY(id_ingredient) REFERENCES ingredient(id_ingredient)

);
