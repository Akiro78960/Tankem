<?php
	require_once("action/AjaxNiveauFavoriAction.php");

	$action = new AjaxArmesFavoritesAction();
	$action->execute();

	echo $action->result;
