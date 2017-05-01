window.onload = function(){
	afficherJoueurs();
}

function afficherJoueurs() {
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
		var template = document.querySelector("#mon-template").innerHTML;
		document.getElementById("contHallOfFame").innerHTML = "";
		tabJoueur = JSON.parse(data);
		tabJoueur = quickSort(tabJoueur, 0, tabJoueur.length-1);
		tabJoueur.reverse(); //Pour inverser l'array
		$(tabJoueur).each(function(i) {
			if(i == 10){
				return false;
			}
			console.log(tabJoueur[i]);
			var newElement = document.createElement("div");
			newElement.innerHTML = template;
			newElement.querySelector('.numero').innerHTML = i + 1;
			newElement.querySelector('.nomJoueur').innerHTML = tabJoueur[i].USERNAME;
			newElement.querySelector('.niveauFavori').innerHTML = "Niveau préféré : ";
			newElement.querySelector('.ratio').innerHTML = "Ratio victoires/défaites : " + ratio(tabJoueur[i]);
			newElement.querySelector('.nbPartiesJoues').innerHTML = "Parties jouées : " + tabJoueur[i].PARTIEJOUE;
			document.getElementById("contHallOfFame").appendChild(newElement);
		});
	})
}

function ajaxNiveau(idJoueur) {
	$.ajax({
		type : "POST",
		url : "ajaxJouers2.php",
		data : {
			
		}
	})
	.done(function(data) {
		var id = JSON.parse(id);
		return id;
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