<?php
	require_once("action/CommonAction.php");

	class IndexAction extends CommonAction {
		
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {

		// if(isset($_POST["nom"])) {
		// 	$data = [];
		// 	$data["username"] = $_POST["nom"] ;
		// 	$data["pwd"] = $_POST["password"];

		// 	$_SESSION["key"] = $this->callAPI("signin", $data);
		// 	if(strlen($_SESSION["key"]) === 40){
		// 		$_SESSION["visibility"] = 1;
		// 		header('location:character.php');
		// 	}
		// }
	}
}
