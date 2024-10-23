-- Insertion des utilisateurs
INSERT INTO utilisateur (id_utilisateur, mdp) VALUES
('1', 'thomas'),
('2', 'benjamin'),
('3', 'akmal'),
('4', 'fany'),
('5', 'toussaint');

-- Insertion des catégories
INSERT INTO categorie (id_categorie, nom_categorie) VALUES
('2', 'Dessert'),
('3', 'Plat Principal');

-- Insertion des origines
INSERT INTO origine (id_origine, nom_origine) VALUES
('2', 'France'),
('17', 'Japon');

-- Insertion des ingrédients
INSERT INTO ingredient (id_ingredient, nom_ingredient) VALUES
('33', 'Bramley Apples'),
('41', 'Butter'),
('52', 'Caster Sugar'),
('53', 'Cayenne Pepper'),
('57', 'Challots'),
('70', 'Chicken Thighs'),
('91', 'Coconut Milk'),
('95', 'Coriander'),
('104', 'Cumin'),
('112', 'Digestive Biscuits'),
('135', 'Flaked Almonds'),
('141', 'Free-range Eggs, Beaten'),
('150', 'Garlic Clove'),
('154', 'Ginger'),
('169', 'Ground Almonds'),
('305', 'Sugar'),
('309', 'Tamarind Paste'),
('320', 'Turmeric'),
('333', 'Water'),
('393', 'Fennel'),
('550', 'Almond Extract');

-- Insertion des recettes
INSERT INTO recette (id_recette, nom_recette, instructions_recette,
                     id_origine, id_categorie) VALUES
('52768',
'Apple Frangipan Tart',
'Preheat the oven to 200C/180C Fan/Gas 6.
Put the biscuits in a large re-sealable freezer bag and bash with a rolling
pin into fine crumbs. Melt the butter in a small pan, then add the biscuit
crumbs and stir until coated with butter. Tip into the tart tin and, using
the back of a spoon, press over the base and sides of the tin to give an even
layer. Chill in the fridge while you make the filling.
Cream together the butter and sugar until light and fluffy. You can do this
in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs,
then add the ground almonds and almond extract and blend until well combined.
Peel the apples, and cut thin slices of apple. Do this at the last minute to
prevent the apple going brown. Arrange the slices over the biscuit base.
Spread the frangipane filling evenly on top. Level the surface and sprinkle
with the flaked almonds.
Bake for 20-25 minutes until golden-brown and set.
Remove from the oven and leave to cool for 15 minutes. Remove the sides of the
tin. An easy way to do this is to stand the tin on a can of beans and push
down gently on the edges of the tin.
Transfer the tart, with the tin base attached, to a serving plate. Serve warm
with cream, crème fraiche or ice cream.',
'2',
'3'),
('53050',
'Ayam Percik',
'In a blender, add the ingredients for the spice paste and blend until smooth.
Over medium heat, pour the spice paste in a skillet or pan and fry for
10 minutes until fragrant. Add water or oil 1 tablespoon at a time if the
paste becomes too dry. Don''t burn the paste. Lower the fire slightly if needed.
Add the cloves, cardamom, tamarind pulp, coconut milk, water, sugar and salt.
Turn the heat up and bring the mixture to boil. Turn the heat to medium low
and simmer for 10 minutes. Stir occasionally. It will reduce slightly. This
is the marinade/sauce, so taste and adjust seasoning if necessary. Don''t worry
if it''s slightly bitter. It will go away when roasting.
When the marinade/sauce has cooled, pour everything over the chicken and
marinate overnight to two days.
Preheat the oven to 425 F.
Remove the chicken from the marinade. Spoon the marinade onto a greased
(or aluminum lined) baking sheet. Lay the chicken on top of the sauce (make
sure the chicken covers the sauce and the sauce isn''t exposed or it''ll burn)
and spread the remaining marinade on the chicken. Roast for 35-45 minutes or
until internal temp of the thickest part of chicken is at least 175 F.
Let chicken rest for 5 minutes. Brush the chicken with some of the oil. Serve
chicken with the sauce over steamed rice (or coconut rice).',
'17',
'2');

-- Insertion des relations ingredient_recette
INSERT INTO ingredient_recette (id_recette, id_ingredient) VALUES
('52768', '112'),
('52768', '41'),
('52768', '33'),
('52768', '52'),
('52768', '141'),
('52768', '169'),
('52768', '550'),
('52768', '135'),
('53050', '70'),
('53050', '57'),
('53050', '154'),
('53050', '150'),
('53050', '53'),
('53050', '320'),
('53050', '104'),
('53050', '95'),
('53050', '393'),
('53050', '309'),
('53050', '91'),
('53050', '305'),
('53050', '333');

-- Insertion des avis
INSERT INTO avis (id_avis, commentaire, note, id_utilisateur,
                  id_recette) VALUES
('1', 'Délicieux !', 5, '3', '52768'),
('2', 'Bonne recette, mais un peu long à faire.', 4, '5', '53050');

-- Insertion des recettes favorites
INSERT INTO recette_favorite (id_utilisateur, id_recette) VALUES
('2', '52768'),
('4', '52768'),
('4', '53050');

-- Insertion des ingrédients dans la liste de courses
INSERT INTO liste_course (id_utilisateur, id_ingredient) VALUES
('1', '33'),
('3', '70'),
('5', '70'),
('5', '33');
