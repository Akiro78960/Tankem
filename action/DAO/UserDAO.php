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
					$_SESSION["Row"] = $row;
					$_SESSION["Username"] = $row["USERNAME"];
				}
			}
			return $visibility;
		}

		public static function updateProfile($email,$firstName,$lastName,$username,$color) {
			$connection = Connection::getConnection();
			$row = $_SESSION["Row"];
			if ($_POST["editPassword"] == "") {
				if(isset($_POST["editEmail"]) && isset($_POST["editPrenom"]) && isset($_POST["editEmail"]) && isset($_POST["editNom"]) && isset($_POST["editUsername"])){
					$previous = $_SESSION["Username"];
					$statement = $connection->prepare("UPDATE joueur SET email = ?,
																		surname = ?,
																		name = ?,
																		couleurTank = ?,
																		username = ? where username = ?");
					$statement->bindValue(1,$email);
					$statement->bindParam(2,$firstName);
					$statement->bindParam(3,$lastName);
					$statement->bindParam(4,$color);
					$statement->bindParam(5,$username);
					$statement->bindParam(6,$previous);
					$statement->execute();
					if($_SESSION["Success"]){
						$_SESSION["Username"] = $username;
					}
				}
			}
			elseif($_POST["editPassword"] != "" && $_POST["editConfirmPassword"] != ""){
				if(isset($_POST["editEmail"]) && isset($_POST["editPrenom"]) && isset($_POST["editEmail"]) && isset($_POST["editNom"]) && isset($_POST["editUsername"])){
					
					if($_POST["editPassword"] == $_POST["editConfirmPassword"]){
						$previous = $_SESSION["Username"];
						$password = $_POST["editPassword"];
						$hashed = password_hash($password,PASSWORD_BCRYPT);
						$statement = $connection->prepare("UPDATE joueur SET email = ?,
																			surname = ?,
																			name = ?,
																			couleurTank = ?,
																			password = ?,
																			username = ? where username = ?");

					
						$statement->bindParam(1,$email);
						$statement->bindParam(2,$firstName);
						$statement->bindParam(3,$lastName);
						$statement->bindParam(4,$color);
						$statement->bindParam(5,$hashed);
						$statement->bindParam(6,$username);
						$statement->bindParam(7,$previous);
						$statement->execute();
						if($_SESSION["Success"]){
							$_SESSION["Username"] = $username;
						}
					}
				}
			}
			
		}

	}