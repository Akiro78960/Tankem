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


		$statementMap->bindParam(1,$DTOmap->name);
		$statementMap->bindParam(2,$DTOmap->creation_date);
		$statementMap->bindParam(3,$DTOmap->status);
		$statementMap->bindParam(4,$DTOmap->size_x);
		$statementMap->bindParam(5,$DTOmap->size_y);
		$statementMap->bindParam(6,$DTOmap->item_delay_min);
		$statementMap->bindParam(7,$DTOmap->item_delay_max);
		try{
			$statementMap->execute();
		}catch(PDOException $e){
			echo 'Valeurs invalides lors de la sauvegarde de la map';
		}
	}

	public function read(){
	}

	public function update(){
	}

	public function delete(){
	}

}
