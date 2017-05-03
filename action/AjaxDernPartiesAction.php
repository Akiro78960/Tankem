<?php
	require_once("action/CommonAction.php");

	class AjaxDernPartiesAction extends CommonAction{
		public $result = "Aucun résultat des dernières parties";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			try{
				$this->connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
				$this->connection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
                $this->connection->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
				$statement = $this->connection->prepare("SELECT editor_niveau.name NomNiveau, joueur.username NomJoueur1, joueur.couleurTank CouleurTank1 FROM partie JOIN editor_niveau ON editor_niveau.id = partie.idNiveau JOIN joueur ON partie.idJoueur1 = joueur.id ORDER BY partie.id DESC");
				$statement->execute();
				$this->rows1 = $statement->fetchall(PDO::FETCH_ASSOC);
				$statement = $this->connection->prepare("SELECT joueur.username NomJoueur2, joueur.couleurTank Couleurtank2 FROM joueur JOIN partie ON joueur.id = partie.idJoueur2 ORDER BY partie.id DESC");
				$statement->execute();
				$this->rows2 = $statement->fetchall(PDO::FETCH_ASSOC);
				$statement = $this->connection->prepare("SELECT joueur.username NomGagnant FROM joueur JOIN partie ON joueur.id = partie.idGagnant ORDER BY partie.id DESC");
				$statement->execute();
				$this->rows3 = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->result = json_encode([$this->rows1,$this->rows2,$this->rows3]);
			}catch(PDOException $e){
				echo "Échec lors de la requête : " + $e->getMessage();
			}
		}
	}