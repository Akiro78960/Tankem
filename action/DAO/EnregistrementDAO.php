<?php
	require_once("Connection.php");
	require_once("DTO/DTOPartie.php");
	require_once("DTO/DTOJoueur.php");
	require_once("DTO/DTOProjectile.php");
	require_once("DTO/DTOArme.php");
	
	class EnregistrementDAO {

		public static function read() {
			$visibility = CommonAction::$VISIBILITY_PUBLIC;
			$connection = Connection::getConnection();
			$result = [];

			// Liste Parties
			$statement = $connection->prepare("SELECT * FROM enregistrement_partie");
			$statement->setFetchMode(PDO::FETCH_ASSOC);
			$statement->execute();

			foreach ($statement as $row){
				$id = array_values($row)[0];
				$id_map = array_values($row)[1];
				$creation_date = array_values($row)[2];
				$newDTO = new DTOpartie($id, $id_map, $creation_date);
				$result[] = $newDTO;
			}
			

			foreach($result as $DTOpartie){
				// Joueur 1
				$statement = $connection->prepare("SELECT * FROM enregistrement_joueur WHERE id_partie = ? AND no_joueur = 1");
				$statement->bindParam(1, $DTOpartie->id);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				foreach ($statement as $row){
					$time_sec = array_values($row)[2];
					$pos_x = array_values($row)[3];
					$pos_y = array_values($row)[4];
					$orientation = array_values($row)[5];
					$health = array_values($row)[6];
					$ball_shot = array_values($row)[7];

					$newDTO = new DTOjoueur($time_sec, $pos_x, $pos_y, $orientation, $health, $ball_shot);
					$DTOpartie->arrayJoueur1[] = $newDTO;
				}

				// Joueur 2
				$statement = $connection->prepare("SELECT * FROM enregistrement_joueur WHERE id_partie = ? AND no_joueur = 2");
				$statement->bindParam(1, $DTOpartie->id);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				foreach ($statement as $row){
					$time_sec = array_values($row)[2];
					$pos_x = array_values($row)[3];
					$pos_y = array_values($row)[4];
					$orientation = array_values($row)[5];
					$health = array_values($row)[6];
					$ball_shot = array_values($row)[7];

					$newDTO = new DTOjoueur($time_sec, $pos_x, $pos_y, $orientation, $health, $ball_shot);
					$DTOpartie->arrayJoueur2[] = $newDTO;
				}

				// Projectiles
				$statement = $connection->prepare("SELECT * FROM enregistrement_projectile WHERE id_partie = ?");
				$statement->bindParam(1, $DTOpartie->id);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				foreach ($statement as $row){
					$time_sec = array_values($row)[1];
					$pos_x = array_values($row)[2];
					$pos_y = array_values($row)[3];
					$en_mouvement = array_values($row)[4];

					$newDTO = new DTOprojectile($time_sec, $pos_x, $pos_y, $en_mouvement);
					$DTOpartie->arrayProjectiles[] = $newDTO;
				}

				// Armes
				$statement = $connection->prepare("SELECT * FROM enregistrement_arme WHERE id_partie = ?");
				$statement->bindParam(1, $DTOpartie->id);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				foreach ($statement as $row){
					$type_arme = array_values($row)[0];
					$time_sec = array_values($row)[2];
					$pos_x = array_values($row)[3];
					$pos_y = array_values($row)[4];

					$newDTO = new DTOarme($type_arme, $time_sec, $pos_x, $pos_y);
					$DTOpartie->arrayArmes[] = $newDTO;
				}

				// Map
				$statement = $connection->prepare("SELECT pos_x, pos_y, type_tuile FROM editor_tuile WHERE id_niveau = ?");
				$statement->bindParam(1, $DTOpartie->id_map);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				foreach ($statement as $row){
					$pos_x = array_values($row)[0];
					$pos_y = array_values($row)[1];
					$type_tuile = array_values($row)[2];
					$DTOpartie->map[$pos_y][$pos_x] = $type_tuile;
				}
			}

			return $result;
		}
	}