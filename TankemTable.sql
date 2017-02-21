-- Mettre un commentaire
-- Pour exécuter ce script dans sqlplus: start creationTable.sql (ou chemin relatif)
-- DROP TABLE test_cx_oracle;
CREATE TABLE tankem_values(
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	description VARCHAR2(200) UNIQUE,
	valMin NUMBER NOT NULL,
	valMax NUMBER NOT NULL,
	defaut NUMBER NOT NULL,
	current_value NUMBER NOT NULL
);
CREATE TABLE tankem_text(
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	message_acceuil VARCHAR2(60),
	message_start VARCHAR2(50)
);
-- Insertion de valeurs dans la table

INSERT INTO tankem_values (description, valMin, valMax,defaut,current_value) VALUES ('vitesse_char',4,12,7,7);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('vitesse_rotation',1000,2000,1500,1500);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('vie',100,2000,200,200);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('temps_mouvement_blocs',0.2,2,0.8,0.8);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('canon_vitesse_balle',4,30,14,14);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('canon_reload',0.2,10,1.2,1.2);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('mitraillette_vitesse_balle',4,30,18,18);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('mitraillette_reload',0.2,10,0.4,0.4);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('grenade_vitesse_balle',10,25,16,16);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('grenade_reload',0.2,10,0.8,0.8);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('shotgun_vitesse_balle',4,30,13,13);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('shotgun_reload',0.2,10,1.8,1.8);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('shotgun_spread',0.1,1.5,0.4,0.4);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('piege_vitesse_balle'0.2,4,1,1);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('piege_reload',0.2,10,0.8,0.8);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('missile_vitesse_balle',20,40,30,30);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('missile_reload',0.2,10,3,3);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('spring_vitesse_saut',6,20,10,10);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('spring_reload',0.2,10,0.5,0.5);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('rayon_explosion',1,30,8,8);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('message_acceuil_duree',1,10,3,3);
INSERT INTO tankem_values (description,min, max,default,current_value) VALUES ('message_countdown_duree',1,10,3,3);

INSERT INTO tankem_text (message_acceuil,message_start) VALUES ('Es ist Zeit für Reich!','Wir müssen die Juden ausrotten!');


-- Ne pas oublier le commit pour que les données soient vraiment dans la table

-- requête pour voir les tables
SELECT table_name FROM user_tables;

-- Destruction de table
-- DROP TABLE tankem_values;
COMMIT;