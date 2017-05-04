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
		$(tabParties).each(function(i) {
			if(i == 5){
				return false;
			}
			var newElement = document.createElement("div");
			newElement.innerHTML = template;
			newElement.querySelector('.nomNiveau').innerHTML = "Nom du niveau : " + tabParties[i].NOMNIVEAU;
			newElement.querySelector('.nomJoueur1').innerHTML = "Nom du joueur 1 : " + tabParties[i].NOMJOUEUR1;
			newElement.querySelector('.couleurTank1').style="background-color:"+tabParties[i].COULEURTANK1;
			newElement.querySelector('.nomJoueur2').innerHTML = "Nom du joueur 2 : " + tabParties[i].NOMJOUEUR2;
			newElement.querySelector('.couleurTank2').style="background-color:"+tabParties[i].COULEURTANK2;			
			newElement.querySelector('.vainqueur').innerHTML = "Gagnant : " + tabParties[i].NOMGAGNANT;
			document.getElementById("contDernPart").appendChild(newElement);
		})
		setTimeout(function(){
			ajaxDernParties();
		}, 10000);
	})
}