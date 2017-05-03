<?php
	
	class UserDAO {

		public static function authenticate($username, $password) {
			$visibility = CommonAction::$VISIBILITY_PUBLIC;
			$connection = Connection::getConnection();

			$statement = $connection->prepare("SELECT * FROM joueur WHERE username = ?");
			$statement->bindParam(1, $username);
			$statement->setFetchMode(PDO::FETCH_ASSOC);
			$statement->execute();

			if ($row = $statement->fetch()) {
				// a changer plus tard au hashage
				if (password_verify($password, $row["PASSWORD"])) {
					$visibility = 1;
					$_SESSION["Username"] = $username;
				}
			}
			return $visibility;
		}

		public function updateProfile($email,$firstName,$lastName,$username,$color) {
			$connection = Connection::getConnection();

			$statement = $connection->prepare("UPDATE joueur SET email = :email,
													  			 surname = :prenom,
																 name = :name,
																 couleurTank = :couleur,
																 username = :username");
			$statement->bindValue(':email',$email,PDO::PARAM_STR);
			$statement->bindValue(':prenom',$firstName,PDO::PARAM_STR);
			$statement->bindValue(':name',$lastName,PDO::PARAM_STR);
			$statement->bindValue(':couleur',$color,PDO::PARAM_STR);
			$statement->bindValue(':couleur',$color,PDO::PARAM_STR);
		}

	}