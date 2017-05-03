window.onload = function(){
	ajaxDernParties();
}

function ajaxDernParties(){
	$.ajax({
		type : "POST",
		url : "ajaxDernParties.php",
		data : {

		}
	})
	.done(function(data){
		var template = document.querySelector("#mon-template").innerHTML;
		document.getElementById("contDernPart").innerHTML = "";
		var tabParties = JSON.parse(data);
		console.log(tabParties);
		// console.log(tabParties[0][0]); Nom niveau, Nom joueur 1, couleur tank 1
		// console.log(tabParties[0][1]); Nom joueur 2, couleur tank 2
		// console.log(tabParties[0][2]); Nom gagnant
		$(tabParties[0]).each(function(i) {
			if(i == 5){
				return false;
			}
			var newElement = document.createElement("div");
			newElement.innerHTML = template;
			newElement.querySelector('.nomNiveau').innerHTML = "Nom du niveau : " + tabParties[0][i].NOMNIVEAU;
			newElement.querySelector('.nomJoueur1').innerHTML = tabParties[0][i].NOMJOUEUR1;
			newElement.querySelector('.couleurTank1').style="background-color:"+tabParties[0][i].COULEURTANK1;
			newElement.querySelector('.nomJoueur2').innerHTML = tabParties[1][i].NOMJOUEUR2;
			newElement.querySelector('.couleurTank2').style="background-color:"+tabParties[1][i].COULEURTANK2;			
			newElement.querySelector('.vainqueur').innerHTML = "Gagnant : " + tabParties[2][i].NOMGAGNANT;
			document.getElementById("contDernPart").appendChild(newElement);
		})
	})
}