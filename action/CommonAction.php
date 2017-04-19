<?php
	session_start();
	// require_once("action/constants.php");
	require_once("action/DAO/Connection.php");
	
	abstract class CommonAction {
		public static $VISIBILITY_PUBLIC = 0;
		public static $VISIBILITY_MEMBER = 1;
		public static $VISIBILITY_MODERATOR = 2;
		public static $VISIBILITY_ADMINISTRATOR = 3;

		private $pageVisibility;

		public function __construct($pageVisibility) {
			$this->pageVisibility = $pageVisibility;
		}

		public function execute() {
			if (!empty($_GET["logout"])) {
				$data = [];
				$data["key"] = $_SESSION["key"] ;
				$this->callAPI("signout", $data);
				session_unset();
				session_destroy();
				session_start();
			}

			if (empty($_SESSION["visibility"])) {
				$_SESSION["visibility"] = CommonAction::$VISIBILITY_PUBLIC;
			}

			if ($_SESSION["visibility"] < $this->pageVisibility) {
				header("location:index.php");
				exit;
			}

			$this->executeAction();
			Connection::closeConnection();
		}

		public function getUsername() {
			$username = "Invité";

			if (!empty($_SESSION["username"])) {
				$username = $_SESSION["username"];
			}

			return $username;
		}

		public function isLoggedIn() {
			return $_SESSION["visibility"] > CommonAction::$VISIBILITY_PUBLIC;
		}

		protected abstract function executeAction();
		/**
 * data = array('key1' => 'value1', 'key2' => 'value2');
 */
protected function callAPI($service, $data) {
	$apiURL = "http://apps-de-cours.com/web-sirius/server/api/" . $service . ".php";

	$options = array(
	    'http' => array(
	        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
	        'method'  => 'POST',
	        'content' => http_build_query($data)
	    )
	);
	$context  = stream_context_create($options);
	$result = file_get_contents($apiURL, false, $context);

if (strpos($result, "<br") !== false) {
		var_dump($result);
		exit;
	}

return json_decode($result);
}
	}
