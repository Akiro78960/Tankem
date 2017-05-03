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
				nouvellePartie.style.margin = "0.5% 0%";
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
			var canvasY = window.innerHeight*60/100
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
	ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);

	var scaleX = ctx.canvas.width/12;
	var scaleY = ctx.canvas.height/12;

	$(map).each(function(i){
		var y = this;
		$(y).each(function(j){
			var valeur = this[0];
			// console.log(i,j,this[0])
			// case vide
			if(valeur == 1){
				ctx.fillStyle="#060";
				ctx.fillRect(j*scaleX,i*scaleY,scaleX+1,scaleY+1)
			}
			else if(valeur == 2){
				ctx.fillStyle="#660";
				ctx.fillRect(j*scaleX,i*scaleY,scaleX+1,scaleY+1)
			}
			else if(valeur == 3){
				ctx.fillStyle="#600";
				ctx.fillRect(j*scaleX,i*scaleY,scaleX+1,scaleY+1)
			}
			else if(valeur == 4){
				ctx.fillStyle="#006";
				ctx.fillRect(j*scaleX,i*scaleY,scaleX+1,scaleY+1)
			}

		})
	})
}