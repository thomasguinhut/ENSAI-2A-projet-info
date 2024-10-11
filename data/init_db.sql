-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur    VARCHAR(30) PRIMARY KEY,
    mdp               VARCHAR(256)
);
