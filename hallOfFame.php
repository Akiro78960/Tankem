<?php
	require_once("action/HallOfFameAction.php");

	$action = new HallOfFameAction();

	$action->execute();

	require_once("partial/header.php");
?>

<script id="mon-template" type="x-template">
    <div class="row rowInfoJoueur">
		<div class="col-md-12">
			<div class="row">
				<div class="col-md-1 cold-md-push-11 numero"></div>
				<div class="col-md-11 cold-md-pull-1">
					<h4 class="text-center nomJoueur"></h4>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p class="niveauFavori"></p>
					<p class="ratio"></p>
					<p class="nbPartiesJoues"></p>
				</div>
				<div class="col-md-6 cold-md-push-6 imageTank"></div>
			</div>
		</div>
	</div>
</script>

<script type="text/javascript" src="js/hallOfFameJS.js"></script>


<div class="container">
	<h1>Hall of Fame</h1>
	<div class="row rowInfoJoueur">
		<div class="col-md-12">
			<div class="row">
				<div class="col-md-1 cold-md-push-11">NUMÉRO</div>
				<div class="col-md-11 cold-md-pull-1">
					<h4 class="text-center">NOM + NOM CALCULÉ</h4>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p>NIVEAU FAVORI</p>
					<p>RATIO VICTOIRES/DÉFAITES</p>
					<p>NOMBRE PARTIES JOUÉES</p>
				</div>
				<div class="col-md-6 cold-md-push-6">
					<p>IMAGE TANK AVEC COULEUR</p>
				</div>
			</div>
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");