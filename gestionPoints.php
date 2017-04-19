<?php
	require_once("action/GestionPointsAction.php");

	$action = new GestionPointsAction();

	$action->execute();

	require_once("partial/header.php");
?>

<div class="container">
	<h1>Gestion des Attributs</h1>
	<div class="row">
		<div class="col-md-8 col-md-push-4">
			<p>Points à dépenser</p>
			<div class="row">
				<div class="col-md-6 test">Vie</div>
				<div class="col-md-6">Force</div>
			</div>
			<div class="row">
				<div class="col-md-6">Agilité</div>
				<div class="col-md-6">Dextérité</div>
			</div>
		</div>
		<div class="col-md-4 col-md-pull-8">
			Stats Tank
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");