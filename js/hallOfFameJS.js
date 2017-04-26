window.onload = function(){
	afficherJoueurs();
	console.log("Ehh");
}

function afficherJoueurs() {
	// var template = document.querySelector("#mon-template").innerHTML;
	ajaxJoueurs();
}

function ajaxJoueurs() {
	$.ajax({
		type : "POST",
		url : "ajaxJoueurs.php",
		data : {

		}
	})
	.done(function(data) {
		tabJoueur = JSON.parse(data);
		console.log(tabJoueur);
		console.log(tabJoueur[0].name);
	})
}

