<?php
	require_once("action/GestionPointsAction.php");

	$action = new GestionPointsAction();

	$action->execute();

	require_once("partial/header.php");
?>

<div class="container">
	<h1>Gestion des Attributs</h1>
	<div class="row rowGestionPts">
		<div class="col-md-8 col-md-push-4 blocGestionPts">
			<h4 class="text-center">Points à dépenser</h4>
			<div class="row rowPoints">
				<div class="col-md-6 cold-md-push-6">
					<p class="text-center">Vie</p>
					<p class="text-center">Force</p>
				</div>
				<div class="col-md-6 cold-md-pull-6">
					<p class="text-center">Agilité</p>
					<p class="text-center">Dextérité</p>
				</div>
			</div>
		</div>
		<div class="col-md-4 col-md-pull-8 blocGestionPts">
			<h4 class="text-center">Stats Tank</h4>
			<p>Vie</p>
			<p>Force</p>
			<p>Agilité</p>
			<p>Dextérité</p>
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");