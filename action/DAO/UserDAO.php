<?php
	
	class UserDAO {
		
		public static function authenticate($username, $password) {
			$today = new DateTime('now');

			$visibility = CommonAction::$VISIBILITY_PUBLIC;
			$connection = Connection::getConnection();

			$statement = $connection->prepare("SELECT * FROM joueur WHERE username = ?");
			$statement->bindParam(1, $username);
			$statement->setFetchMode(PDO::FETCH_ASSOC);
			$statement->execute();

			if ($row = $statement->fetch()) {
				// a changer plus tard au hashage
				if($row["BANNED"] == 1){
					$visibility = -1;
					$bannedDate = new DateTime($row["BANNEDSTART"]);
					$threeDays = date_add($bannedDate,date_interval_create_from_date_string('3 days'));
				
					if ($today >= $threeDays) {
						if(password_verify($password, $row["PASSWORD"])){
							$visibility = 1;
							$_SESSION["Row"] = $row;
							$_SESSION["Username"] = $row["USERNAME"];
							$statement = $connection->prepare("UPDATE joueur SET banned = ?,bannedStart = ?, logCounter = ? where username = ?");
							$banned = 0;
							$logCounter = 0;
							$bannedStart = NULL;
							$statement->bindParam(1,$banned);
							$statement->bindParam(2,$bannedStart);
							$statement->bindParam(3,$logCounter);
							$statement->bindParam(4,$username);
							$statement->execute();
							}
						}
					}
				elseif($row["LOGCOUNTER"] < 4){
					if (password_verify($password, $row["PASSWORD"])) {
						$visibility = 1;
						$_SESSION["Row"] = $row;
						$_SESSION["Username"] = $row["USERNAME"];

						$statement = $connection->prepare("UPDATE joueur SET logCounter = ? where username = ?");
						$reset = 0;
						$statement->bindParam(1,$reset);
						$statement->bindParam(2,$username);
						$statement->execute();
					}
					elseif($row["LOGCOUNTER"] + 1 == 4){
						$visibility = -1;
						$statement = $connection->prepare("UPDATE joueur SET banned = ?,bannedStart = ?, logCounter = ? where username = ?");
						$calc = $row["LOGCOUNTER"] + 1;
						$banned = 1;
						$todaystr = $today->format('y-m-d');
						$statement->bindParam(1,$banned);
						$statement->bindParam(2,$todaystr);
						$statement->bindParam(3,$calc);
						$statement->bindParam(4,$username);
						$statement->execute();
					}
					else{
						$visibility = 0;
						$statement = $connection->prepare("UPDATE joueur SET logCounter = ? where username = ?");
						$calc = $row["LOGCOUNTER"] + 1;
						$statement->bindParam(1,$calc);
						$statement->bindParam(2,$username);
						$statement->execute();
					}
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
					$statement->bindParam(1,$email);
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