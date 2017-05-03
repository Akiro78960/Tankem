window.onload = function(){
	ajaxJoueurs();
}

function afficherJoueurs(tabJoueur) {
	var template = document.querySelector("#mon-template").innerHTML;
	document.getElementById("contHallOfFame").innerHTML = "";
	$(tabJoueur).each(function(i) {
		if(i == 10){
			return false;
		}
		var newElement = document.createElement("div");
		newElement.innerHTML = template;
		newElement.querySelector('.numero').innerHTML = i + 1;
		newElement.querySelector('.nomJoueur').innerHTML = tabJoueur[i].USERNAME;
		// newElement.querySelector('.niveauFavori').innerHTML = "Niveau préféré : " + ajaxNiveauFavori(tabJoueur[i].ID);
		// console.log(ajaxNiveauFavori(tabJoueur[i].ID));
		newElement.querySelector('.ratio').innerHTML = "Ratio victoires/défaites : " + ratio(tabJoueur[i]);
		newElement.querySelector('.nbPartiesJoues').innerHTML = "Parties jouées : " + tabJoueur[i].PARTIEJOUE;
		document.getElementById("contHallOfFame").appendChild(newElement);
		ajaxNiveauFavori(tabJoueur[i].ID, i);
	});
}

function ajaxNiveauFavori(id, idNode) {
	$.ajax({
		type : "POST",
		url : "ajaxNiveauFavori.php",
		data : {
			idJoueur: id
		}
	})
	.done(function(data){
		var niveauPref = JSON.parse(data);
		console.log(niveauPref);
		if(niveauPref.length == 0){
			niveauPref = "Aucun niveau préféré!"
		}
		else{
			niveauPref = niveauPref[0].IDMAP;
		}
		document.getElementById("contHallOfFame").children[idNode].querySelector('.niveauFavori').innerHTML = niveauPref;
	})
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
		tabJoueur = quickSort(tabJoueur, 0, tabJoueur.length-1);
		tabJoueur.reverse(); //Pour inverser l'array
		afficherJoueurs(tabJoueur);
	})
}



function ratio(joueur){
	if(joueur.PARTIEJOUE == 0)
		return 0;
	else
		return joueur.PARTIEGAGNE / joueur.PARTIEJOUE;
}

//Quicksort (yaaaay)
function swap(items, firstIndex, secondIndex){
    var temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function partition(items, left, right) {
	var pivot = ratio(items[Math.floor((right + left) / 2)]);
	var i = left;
    var j = right;

    while (i <= j) {
		while (ratio(items[i]) < pivot) {
            i++;
        }
		while (ratio(items[j]) > pivot) {
            j--;
        }
        if (i <= j) {
            swap(items, i, j);
            i++;
            j--;
        }
    }
    return i;
}

function quickSort(items, left, right) {
    var index;

    if (items.length > 1) {
        index = partition(items, left, right);
        if (left < index - 1) {
            quickSort(items, left, index - 1);
        }
        if (index < right) {
            quickSort(items, index, right);
        }
    }

    return items;
}

//TO-DO : faire un select dans une autre table (Joueur-Niveau)