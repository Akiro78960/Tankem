<?php

class DAOeditorOracle {
	private static $connection;

	public function __construct() {
		$this->connection = Connection::getConnection();
	}

	public function create($DTOmap){
		$statementMap = $this->connection->prepare("INSERT INTO editor_niveau (
													name,
													creation_date,
													status
													size_x
													size_y
													item_delay_min,
													item_delay_max)
													VALUES (
													:name,
													:creation_date,
													:status,
													:size_x,
													:size_y,
													:item_delay_min,
													:item_delay_max)");

		$statement->bindParam(':name',$DTOmap->name);
		$statement->bindParam(':creation_date',$DTOmap->creation_date);
		$statement->bindParam('status',$DTOmap->status);
		$statement->bindParam('size_x',$DTOmap->size_x);
		$statement->bindParam('size_y',$DTOmap->size_y);
		$statement->bindParam('item_delay_min',$DTOmap->item_delay_min);
		$statement->bindParam('item_delay_max',$DTOmap->item_delay_max);
		$statement->execute();
	}

	public function read(){
	}

	public function update(){
	}

	public function delete(){
	}
	
}
