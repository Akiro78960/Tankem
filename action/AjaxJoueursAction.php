<?php
	require_once("action/CommonAction.php");

	class AjaxJoueursAction extends CommonAction{
		public $result = "Rien ne s'est passé";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			$str = $_POST["idJoueur"]
			try{
				$this->connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
				$this->connection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
                $this->connection->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
				$statement = $this->connection->prepare("SELECT * from joueur");
				$statement->execute();
				$this->tab1 = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->result = json_encode($this->tab1);
				$statement = $this->connection->prepare("SELECT name FROM editor_niveau INNER JOIN joueur_map ON editor_niveau.id = joueur_map.idNiveau WHERE MAX(SELECT nbFoisJouer FROM joueur_map WHERE idJoueur = ?) = joueur_map.nbFoisJouer");
				$statement->execute(Array($str));
			}catch(PDOException $e){
				echo "Échec lors de la connection : " + $e->getMessage();
			}
		}
	}