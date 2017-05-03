var block1 = new Image();
block1.src = "images/block1.png";
var block2 = new Image();
block2.src = "images/block2.jpg";
var block3 = new Image();
block3.src = "images/block3.jpg";
var block4 = new Image();
block4.src = "images/block4.png";

window.onload = function() {
	ajaxEnregistrement();
}

function ajaxEnregistrement() {
	$.ajax({
			type : "POST",
			url : "ajaxEnregistrement.php",
			data : {
			}
		})
		.done(function(data) {
			var listeParties = JSON.parse(data);
			var containerPage = document.getElementById("page-replay");
			containerPage.style.padding = "5%";


			// Creation liste des parties
			var containerListe = document.createElement("ul");
			containerListe.style.width = "25%";
			containerListe.style.listStyle = "none";
			containerListe.style.float = "left";

			$(listeParties).each(function(i) {
				var partie = this;
				var nouvellePartie = document.createElement("li");
				var textNum = document.createTextNode("Partie #" + partie.id);
				var textDate = document.createTextNode("Crée le: " + partie.creation_date);
				nouvellePartie.appendChild(textNum);
				nouvellePartie.appendChild(document.createElement("br"));
				nouvellePartie.appendChild(textDate);

				//Style
				nouvellePartie.style.marginBottom = "1%";
				nouvellePartie.style.padding = "0.5%";
				nouvellePartie.style.color = "#fff";
				nouvellePartie.style.backgroundColor = "#666";
				nouvellePartie.onmouseover = function() {
					this.style.backgroundColor = "#669";
				}
				nouvellePartie.onmouseleave = function() {
					this.style.backgroundColor = "#666";
				}
				nouvellePartie.style.display = "block";

				// Event
				nouvellePartie.onmousedown = function(){drawMap(partie.map);}

				containerListe.appendChild(nouvellePartie);
			});

			containerPage.appendChild(containerListe);

			// Creation Canvas
			var canvas = document.createElement("canvas");
			var canvasX = window.innerWidth*60/100
			var canvasY = window.innerHeight*80/100
			canvas.setAttribute("id", "canvas");
			canvas.setAttribute("width", canvasX);
			canvas.setAttribute("height", canvasY);
			// canvas.style.width = "70%";
			// canvas.style.height = "70%";
			canvas.style.backgroundColor = "#181818";
			canvas.style.float = "right";

			containerPage.appendChild(canvas);

			// Clear float
			var clear = document.createElement("p");
			clear.style.clear = "both";
			containerPage.appendChild(clear);
		})
}

function drawMap(map){
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext('2d');

	var scaleX = ctx.canvas.width/12;
	var scaleY = ctx.canvas.height/12;


	$(map).each(function(i){
		var y = this;
		$(y).each(function(j){
			var valeur = this[0];
			// console.log(i,j,this[0])
			// case vide
			if(valeur == 1){
				ctx.drawImage(block1,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 2){
				ctx.drawImage(block2,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 3){
				ctx.drawImage(block3,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 4){
				ctx.drawImage(block4,j*scaleX,i*scaleY,scaleX,scaleY);
			}

		})
	})
}