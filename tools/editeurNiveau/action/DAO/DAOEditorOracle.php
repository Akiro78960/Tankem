<?php

	require_once("action/DAO/Connection.php");

class DAOeditorOracle {
	private $connection;

	public function __construct() {
		$this->connection = Connection::getConnection();
	}

	public function create($DTOmap){
		$statementMap = $this->connection->prepare("INSERT INTO editor_niveau (
													name,
													creation_date,
													status,
													size_x,
													size_y,
													item_delay_min,
													item_delay_max)
													VALUES (?,?,?,?,?,?,?)");


		echo($DTOmap->name . "\n");
		$statementMap->bindParam(1,$DTOmap->name);
		echo($DTOmap->creation_date . "\n");
		$statementMap->bindParam(2,$DTOmap->creation_date);
		echo($DTOmap->status . "\n");
		$statementMap->bindParam(3,$DTOmap->status);
		echo($DTOmap->size_x . "\n");
		$statementMap->bindParam(4,$DTOmap->size_x);
		echo($DTOmap->size_y . "\n");
		$statementMap->bindParam(5,$DTOmap->size_y);
		echo($DTOmap->item_delay_min . "\n");
		$statementMap->bindParam(6,$DTOmap->item_delay_min);
		echo($DTOmap->item_delay_max . "\n");
		$statementMap->bindParam(7,$DTOmap->item_delay_max);
		try{
			$statementMap->execute();
		}catch(PDOException $e){
						echo 'Échec lors de la connexion : ' . $e->getMessage();
					}
	}

	public function read(){
	}

	public function update(){
	}

	public function delete(){
	}

}
