<?php
	require_once("action/DernieresPartiesAction.php");

	$action = new DernieresPartiesAction();

	$action->execute();

	require_once("partial/header.php");
?>

<div class="container">
	<h1>Dernières Parties</h1>
	<div class="row rowInfoPartie">
		<div class="col-md-12">
			<h4 class="text-center">NOM DU NIVEAU</h4>
			<div class="row">
				<div class="col-md-6 cold-md-push-6 blocPartieJoueur">
					<p class="text-center">NOM DU JOUEUR1</p>
					<p>TANK ET COULEUR DU JOUEUR1</p>
				</div>
				<div class="col-md-6 cold-md-pull-6 blocPartieJoueur">
					<p class="text-center">NOM DU JOUEUR2</p>
					<p>TANK ET COULEUR DU JOUEUR2</p>
				</div>
			</div>
			<h4 class="text-center">VAINQUEUR</h4>
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");