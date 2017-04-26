<?php
	require_once("action/AjaxJoueursAction.php");

	$action = new AjaxJoueursAction();
	$action->execute();

	echo json_encode($action->result);