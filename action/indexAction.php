<?php
	require_once("action/CommonAction.php");
	require_once("action/DAO/UserDAO.php");

	class IndexAction extends CommonAction {
		public $wrongLogin;
		public $banned;
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {

			$this->wrongLogin = false;
			$this->banned = false;
			if (isset($_POST["username"])) {
				$visibility = UserDAO::authenticate($_POST["username"], $_POST["pwd"]);
				if ($visibility > CommonAction::$VISIBILITY_PUBLIC) {
					$_SESSION["Username"] = $_POST["username"];
					$_SESSION["visibility"] = $visibility;

					header("location:Infos.php");
					exit;
				}
				elseif($visibility == -1) {
					$this->banned = true;
				}
				else{
					$this->wrongLogin = true;
				}
			}
		}
	}
