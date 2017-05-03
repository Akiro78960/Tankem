<?php
	require_once("action/AjaxNiveauFavori.php");

	$action = new AjaxNiveauFavori();
	$action->execute();

	echo $action->result;