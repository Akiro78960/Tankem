<?php
	
	class UserDAO {

		public static function authenticate($username, $password) {
			$visibility = CommonAction::$VISIBILITY_PUBLIC;
			$connection = Connection::getConnection();

			$statement = $connection->prepare("SELECT * FROM joueur WHERE ingamename = ?");
			$statement->bindParam(1, $username);
			$statement->setFetchMode(PDO::FETCH_ASSOC);
			$statement->execute();

			if ($row = $statement->fetch()) {
				// a changer plus tard au hashage
				// if (password_verify($password, $row["PASSWORD"])) {
				if ($password == $row["PASSWORD"]) {
					
					$visibility = 1;
				}
			}
			echo $row["PASSWORD"];
			echo $password;
			return $visibility;
		}

		public function updateProfile() {
			$connection = Connection::getConnection();
			// ...
			// ...
		}

	}