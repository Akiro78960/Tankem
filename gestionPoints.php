<?php
	require_once("action/GestionPointsAction.php");

	$action = new GestionPointsAction();

	$action->execute();

	require_once("partial/header.php");
?>

<div class="container">
	<h1>Gestion des Attributs</h1>
	<div class="row">
		<div class="col-md-8 gpStatsJoueur">
			<h4 class="text-center">Stats Joueur</h4>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p id="gpHPTotal">HP TOTAL</p>
				</div>
				<div class="col-md-6 cold-md-pull-6">
					<p id="gpDEGATTotal">BONUS DÉGAT</p>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p id="gpDEPLACEMENTTotal">VITESSE DÉPLACEMENT</p>
				</div>
				<div class="col-md-6 cold-md-pull-6">
					<p id="gpTIRTotal">VITESSE TIR</p>
				</div>
			</div>
		</div>

		<div class="col-md-6 gpModifStats">
			<h4 class="text-center">Modifications des Stats</h4>
			<p class="text-center">Points disponibles : </p>
			<div class="row">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit">-</button>
				</div>
				<div class="col-md-9">
					<p class="text-center">HP : </p>
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit">-</button>
				</div>
				<div class="col-md-9">
					<p class="text-center">DEGAT : </p>
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit">-</button>
				</div>
				<div class="col-md-9">
					<p class="text-center">DEPLACEMENT : </p>
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit">-</button>
				</div>
				<div class="col-md-9">
					<p class="text-center">TIR : </p>
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit">+</button>
				</div>
			</div>
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");