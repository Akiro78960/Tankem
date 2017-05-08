// Variables globales
var canvas = null;
var ctx = null;
var scaleX = 0;
var scaleY = 0;
var game = null;
var play = false;
var iter = 0;
var tick = 0;

// Images Map
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
			console.log(listeParties);

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
				nouvellePartie.onmousedown = function(){updateGame(partie);}

				containerListe.appendChild(nouvellePartie);
			});

			containerPage.appendChild(containerListe);

			// Creation Canvas
			canvas = document.createElement("canvas");
			var canvasX = window.innerWidth*60/100
			var canvasY = window.innerHeight*80/100
			canvas.setAttribute("id", "canvas");
			canvas.setAttribute("width", canvasX);
			canvas.setAttribute("height", canvasY);
			canvas.style.backgroundColor = "#181818";
			canvas.style.float = "right";

			ctx = canvas.getContext('2d');

			containerPage.appendChild(canvas);

			// Infos de la partie
			var divInfos = document.createElement("div");
			divInfos.style.margin = "5% 0%";

			var button = document.createElement("button");
			button.onclick = function(){buttonPlay();}
			button.innerHTML = "Play";

			var slider = document.createElement("input");
			slider.setAttribute("id", "slider");
			slider.setAttribute("type", "range");
			slider.setAttribute("min", "0");
			slider.setAttribute("max", "100");
			slider.setAttribute("value", "0");
			slider.style.margin = "0% 3%";

			// slider.onchange = function() {tick = slider.value;}
			$(document).on('input', '#slider', function() {
				play = false;
				tick = this.value;
			});

			divInfos.appendChild(button);
			divInfos.appendChild(slider);
			containerListe.appendChild(divInfos);

			// Clear float
			var clear = document.createElement("p");
			clear.style.clear = "both";
			containerPage.appendChild(clear);
			drawGame();
		})
}

// button function
function buttonPlay(){
	if(play){
		play = false;
	}
	else {
		play = true;
	}
}

// affichage de la partie
function updateGame(partie){
	tick = 0;
	play = false;
	game = partie;
	$("#slider").attr({"min" : 0, "max" : getGameMaxTime(partie), "value" : 0});
	console.log(getGameMaxTime(game))
}

function drawGame(){
	iter++;
	$("#slider").val(tick);
	if(game != null && iter >= 5){
		iter = 0;
		drawMap(game.map);
		drawPlayerOne(game, tick);
		drawPlayerTwo(game, tick);
		drawWeapon(game,tick);
		drawProjectiles(game,tick);
		if(play){
			tick++;
		}
	}
	console.log(tick)
	window.requestAnimationFrame(drawGame);
}

// Dessine la map dans le canvas selon les infos donnees
function drawMap(map){
	scaleX = ctx.canvas.width/map[0].length;
	scaleY = ctx.canvas.height/map.length;


	$(map).each(function(i){
		var y = this;
		$(y).each(function(j){
			var valeur = this[0];
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

//
function drawPlayerOne(game, time_sec){
	var arrayJoueur1 = game.arrayJoueur1;

	// Trouver infos au bon temps
	var joueur = infoAtTick(arrayJoueur1, tick);

	// afficher infos
	if(joueur){
		ctx.fillStyle="#5AC";
		ctx.fillRect(positionX(joueur.pos_x, game.map[0].length)-(scaleX/2),
					positionY(joueur.pos_y, game.map.length)-(scaleY/2),
					scaleX,scaleY)

	}

}

function drawPlayerTwo(game, time_sec){
	var arrayJoueur2 = game.arrayJoueur2;

	// Trouver infos au bon temps
	var joueur = infoAtTick(arrayJoueur2, tick);

	// afficher infos
	if(joueur){
		ctx.fillStyle="#CA5";
		ctx.fillRect(positionX(joueur.pos_x, game.map[0].length)-(scaleX/2),
					positionY(joueur.pos_y, game.map.length)-(scaleY/2),
					scaleX,scaleY)

	}

}

function drawWeapon(game, time_sec){
	var arrayArmes = game.arrayArmes;

	// Trouver infos au bon temps
	var arme = infoAtTick(arrayArmes, tick);

	// afficher infos
	if(arme){
		ctx.fillStyle="#333";
		ctx.fillRect(positionX(arme.pos_x, game.map[0].length)-(scaleX/4),
					positionY(arme.pos_y, game.map.length)-(scaleY/4),
					scaleX/2,scaleY/2)

	}

}
 function drawProjectiles(game, time){
	 var arrayProjectiles = game.arrayProjectiles;
	 var projectiles = [];

	 for(var i=0; i<arrayProjectiles.length; i++){
		 if(arrayProjectiles[i].time_sec == time){
			 projectiles.push(arrayProjectiles[i]);
		 }
	 }

	 if(projectiles.length > 0){
		 for(var j=0; j<projectiles.length; j++){
			ctx.fillStyle="#000";
			ctx.fillRect(positionX(projectiles[j].pos_x, game.map[0].length)-(scaleX/10),
						positionY(projectiles[j].pos_y, game.map.length)-(scaleY/10),
						scaleX/5,scaleY/5)

		 }
	 }
 }

function infoAtTick(array, time){
	var result = false;

	for(var i=0; i<array.length; i++){
		if(array[i].time_sec == time){
			result = array[i];
			break;
		}
	}

	return result;

}

function positionX(posX,lengthX){
	var posX = posX.replace(",", ".");
	var totalX = parseFloat(posX) + lengthX;
	var width = ctx.canvas.width;

	return totalX*width/(lengthX*2);
}

function positionY(posY,lengthY){
	var posY = posY.replace(",", ".");
	var totalY = parseFloat(posY) + lengthY;
	var height = ctx.canvas.height;

	return totalY*height/(lengthY*2);
}

function getGameMaxTime(game){
	var result = 0;

	for( var i=0; i<game.arrayJoueur1.length; i++){
		var time = parseInt(game.arrayJoueur1[i].time_sec);
		if(result < time){
			result = time;
		}
	}

	for( var i=0; i<game.arrayJoueur2.length; i++){
		var time = parseInt(game.arrayJoueur2[i].time_sec);
		if(result < time){
			result = time;
		}
	}

	return result
}