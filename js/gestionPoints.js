

window.onload = function(){
	var joueur = new Joueur();
	modifStats(joueur);
}

function modifStats(joueur){
	document.querySelector(".statModHP").innerHTML = joueur.hp;
	document.querySelector(".statModDEGAT").innerHTML = joueur.degat;
	document.querySelector(".statModDEP").innerHTML = joueur.deplacement;
	document.querySelector(".statModTIR").innerHTML = joueur.tir;
}

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
		var pts = niveau * 5 - (this.hp + this.degat + this.deplacement + this.tir);
		if(pts < 0)
			pts = 0;
		return pts;
	}
}