<?php
	require_once("action/CommonAction.php");
	class SignupAction extends CommonAction {
		public $wrongInfo;
		public $errorMessage = "";
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {

			$connection = Connection::getConnection();
			$execute = true;
			if(isset($_POST["fieldUsername"])){

				$statement = $connection->prepare("INSERT INTO joueur (username,name,surname,couleurTank,password,banned,bannedStart,logCounter,email,niveau,experience,vie,force,agilite,dexterite,partieJoue,partieGagne) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
				if($_POST["fieldUsername"] != ""){
					$statement2 = $connection->prepare("SELECT * FROM joueur WHERE username = ?");
					$statement2->bindParam(1,$_POST["fieldUsername"]);
					$statement2->setFetchMode(PDO::FETCH_ASSOC);
					$statement2->execute();
					$count = $statement2->rowCount();

					if ($count == 0){
						$statement->bindParam(1, $_POST["fieldUsername"]);
					}
					else{
						$execute = false;
						echo "<div class='error'> Ce nom d'utilisateur est déjà utilisé </div>";
					}
				}

				if($_POST["fieldNom"] != ""){
					$statement->bindParam(2, $_POST["fieldNom"]);
				}
				else if($execute){
					$execute = false;
					echo "<div class='error'> Veuillez entrer un nom </div>";
				}
				if($_POST["fieldPrenom" ] != ""){
					$statement->bindParam(3, $_POST["fieldPrenom"]);
				}
				else if($execute){
					$execute = false;
					echo "<div class='error'> Veuillez entrer un prenom </div>";
				}
				$statement->bindParam(4, $_POST["fieldColor"]);
				if($_POST["fieldPassword"] != ""){
					if($_POST["fieldPassword"] == $_POST["fieldConfirmPassword"]){
						$hashedPwd = password_hash($_POST["fieldPassword"], PASSWORD_BCRYPT);
						$statement->bindParam(5,$hashedPwd);
					}
					else if($execute){
						$execute = false;
						echo "<div class='error'> Les mots de passe ne sont pas les mêmes </div>";
					}
				}
				else if($execute){
					$execute = false;
					echo "<div class='error'> Veuillez entrer un mot de passe </div>";
				}
				if($_POST["fieldEmail"] != ""){
					$statement2 = $connection->prepare("SELECT * FROM joueur WHERE email = ?");
					$statement2->bindParam(1,$_POST["fieldEmail"]);
					$statement2->setFetchMode(PDO::FETCH_ASSOC);
					$statement2->execute();
					$count = $statement2->rowCount();
					if($count == 0){
						$statement->bindParam(9, $_POST["fieldEmail"]);
					}
					else if($execute){
						$execute = false;
						echo "<div class='error'> Cet email est déjà utilisé </div>";
					}
				}
				else if($execute){
					$execute = false;
					echo "<div class='error'> Veuillez entrer un email </div>";
				}
				if($execute){
					$tmp = 0;
					$notBanned = null;
					$statement->bindParam(6, $tmp);
					$statement->bindParam(7, $notBanned);
					$statement->bindParam(8, $tmp);
					$statement->bindParam(10, $tmp);
					$statement->bindParam(11, $tmp);
					$statement->bindParam(12, $tmp);
					$statement->bindParam(13, $tmp);
					$statement->bindParam(14, $tmp);
					$statement->bindParam(15, $tmp);
					$statement->bindParam(16, $tmp);
					$statement->bindParam(17, $tmp);

					$statement->execute();


					echo "<div class='error'> L'enregistrement s'est bien effectué </div>";
				}
			}

		}
}
