const AJOUT_HP = 10;
const AJOUT_DEGAT = 10;
const AJOUT_DEP = 5;
const AJOUT_TIR = 10;

var joueur = null;

window.onload = function(){
	joueur = new Joueur();
	initStats();
}

function initStats(){
	joueur.niveau = 5;
	joueur.hp = 1;
	joueur.degat = 7;
	joueur.deplacement = 5;
	joueur.tir = 2;
	retrieveHpTot(); //On peut pas retourner le hp total vu que c'est une requête Ajax
	document.getElementById("gpDEGATTotal").innerHTML = "BONUS DÉGAT : " + calcDegatTot().toFixed(2) + "%";
	document.getElementById("gpDEPTotal").innerHTML = "BONUS VITESSE DÉPLACEMENT : " + calcDepTot().toFixed(2) + "%";
	document.getElementById("gpTIRTotal").innerHTML = "BONUS VITESSE TIR : " + calcTirTot().toFixed(2) + "%";
	document.querySelector(".statModHP").innerHTML = joueur.hp;
	document.querySelector(".statModDEGAT").innerHTML = joueur.degat;
	document.querySelector(".statModDEP").innerHTML = joueur.deplacement;
	document.querySelector(".statModTIR").innerHTML = joueur.tir;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifHP(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.hp < 30)
		joueur.modifHP(++joueur.hp);
	else if(!plus && joueur.hp > 0)
		joueur.modifHP(--joueur.hp);
	document.querySelector(".statModHP").innerHTML = joueur.hp;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifDEGAT(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.degat < 30)
		joueur.modifDEGAT(++joueur.degat);
	else if(!plus && joueur.degat > 0)
		joueur.modifDEGAT(--joueur.degat);
	document.querySelector(".statModDEGAT").innerHTML = joueur.degat;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifDEP(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.deplacement < 30)
		joueur.modifDEP(++joueur.deplacement);
	else if(!plus && joueur.deplacement > 0)
		joueur.modifDEP(--joueur.deplacement);
	document.querySelector(".statModDEP").innerHTML = joueur.deplacement;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifTIR(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.tir < 30)
		joueur.modifTIR(++joueur.tir);
	else if(!plus && joueur.tir > 0)
		joueur.modifTIR(--joueur.tir);
	document.querySelector(".statModTIR").innerHTML = joueur.tir;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function calcHpTot(hp){
	return hp / 100 * (100 + AJOUT_HP * joueur.hp);
}

function calcDegatTot(){
	return AJOUT_DEGAT * joueur.degat;
}

function calcDepTot(){
	return AJOUT_DEP * joueur.deplacement;
}

function calcTirTot(){
	var tir = 100;
	for(var i = 0; i < joueur.tir; ++i){
		tir = tir / 100 * (100 - AJOUT_TIR);
	}
	return 100 - tir;
}

function retrieveHpTot(){
	var pts = 0
	$.ajax({
		type : "POST",
		url : "ajaxPtsVie.php",
		data : {

		}
	})
	.done(function(data){
		var pts = JSON.parse(data);
		document.getElementById("gpHPTotal").innerHTML = "HP TOTAL : " + calcHpTot(pts[0].VIE).toFixed(2);
	})
}

function retrieveInfoJoueur(){

}
/********************
 CLASSES
********************/

class Joueur{
	constructor(){
		this.hp = 0;
		this.degat = 0;
		this.deplacement = 0;
		this.tir = 0;
		this.niveau = 0;
	}

	modifHP(nouvHP){
		this.hp = nouvHP;
	}

	modifDEGAT(nouvDG){
		this.degat = nouvDG;
	}

	modifDEP(nouvDEP){
		this.deplacement = nouvDEP;
	}

	modifTIR(nouvTIR){
		this.tir = nouvTIR;
	}

	calcPtsDepenser(){
		var pts = this.niveau * 5 - (this.hp + this.degat + this.deplacement + this.tir);
		if(pts < 0)
			pts = 0;
		return pts;
	}
}

/*
TO-DO
Faire en sorte qu'on utilise les données du joueur pour voir les infos.
Mettre un bouton d'enregistrement et permettre au joueur d'renregistrer ces données.
Faire en sorte que seul ceux qui sont connectés au site peuvent accéder à cette page.
*/