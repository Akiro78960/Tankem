<?php
	require_once("action/CommonAction.php");
	require_once("action/DAO/UserDAO.php");

	class IndexAction extends CommonAction {
		public $wrongLogin;
		
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			if ($_SESSION["visibility"] > CommonAction::$VISIBILITY_PUBLIC) {
				header("location:home.php");
				exit;
			}

			$this->wrongLogin = false;

			if (isset($_POST["username"])) {
				$visibility = UserDAO::authenticate($_POST["username"], $_POST["pwd"]);

				if ($visibility > CommonAction::$VISIBILITY_PUBLIC) {
					$_SESSION["username"] = $_POST["username"];
					$_SESSION["visibility"] = $visibility;

					header("location:Infos.php");
					exit;
				}
				else {
					$this->wrongLogin = true;
				}
			}
		}
	}
