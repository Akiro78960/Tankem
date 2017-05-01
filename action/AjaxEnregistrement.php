<?php
	require_once("CommonAction.php");
	require_once("DAO/EnregistrementDAO.php");

	// class AjaxAction extends CommonAction{
	// 	 public function __construct() {
	// 		 parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
	// 	 }

			 // protected function executeAction() {
				 $DAO = new EnregistrementDAO();
				 $ListeParties = $DAO->readListeParties();
				 foreach ($ListeParties as $partie){
				 	echo $partie->id . " " . $partie->id_map . " " . $partie->creation_date . "<br>";
				 }

				 echo "Lecture partie id:4" . "<br>";

				foreach ($ListeParties as $partie){
					if($partie->id == 2){
						$DAO->readPartie($partie);
						foreach ($partie->map as $y){
							foreach ($y as $x){
								echo $x . " ";
							}
							echo "<br>";
						}
					}
				 }

				 
	// 	 }
	// }