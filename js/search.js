var resultSearch = null
var mapFavorites = []

// $(document).ready(function() {
//     console.log("ready")
//     var resultSearch = null
//     var mapFavorites = []
// });

function search(){
    var searchbar = document.getElementById("searchBar")
    $.ajax({
        url: 'ajaxSearch.php',
        type: 'POST',
        data: {searchKey: searchbar.value}
    })
    .done(function(r) {
        document.getElementById("searchResults").innerHTML=""
        resultSearch = JSON.parse(r)
        console.log(resultSearch);
        getFavoritMap()

    })
}

function getFavoritMap(){
    $(resultSearch).each(function(index, el) {
        $.ajax({
            type : "POST",
            url : "ajaxNiveauFavori.php",
            data : {
                idJoueur: resultSearch[index].ID
            }
        })
        .done(function(favouritmap) {
            mapFavorites[index] = JSON.parse(favouritmap)
            getNameFavMap(index)
        })
    })
}

function getNameFavMap(index){
        if(mapFavorites[index].length == 0){
            mapFavorites[index] = "NONE"
        }else{
            $.ajax({
                type : "POST",
                url : "ajaxGetNomMap.php",
                data : {
                    idNiveau: mapFavorites[index][0].IDNIVEAU
                }
            })
            .done(function(r) {
                console.log("success");
                reponse = JSON.parse(r)
                mapFavorites[index] = reponse[0].NAME
                console.log(mapFavorites[index]);

                    displayInfos()
            })
        }
}

function displayInfos(){
    document.getElementById("searchResults").innerHTML=""
    $(resultSearch).each(function(index) {
        /////////////AJAX PRINCIPAL///////////
        node = document.createElement("div")
        node.className = "container"
        node.style="background-color:F0F0F0; padding:1%; margin:1% auto;"
        row1 = document.createElement("div")
        row1.className="row"
        row2 = document.createElement("div")
        row2.className="row"
        row3 = document.createElement("div")
        row3.className="row"

        //row1
        colName = document.createElement("div")
        colName.className="col-sm-12"
        txtname = document.createElement("h4")
        txtname.className="text-center"
        texte = document.createTextNode(""+resultSearch[index].USERNAME + " " + calculateName(resultSearch[index]) + " ("+resultSearch[index].SURNAME+" "+resultSearch[index].NAME+")")
        txtname.appendChild(texte)
        colName.appendChild(txtname)
        row1.appendChild(colName)
        row1.style="background-color:E0E0E0;border:1px solid black"


        //row2
        colImg = document.createElement("div")
        img = document.createElement("img")
        colImg.className="col-sm-2"
        img.src="images/tankAlpha.png"
        img.style="width:150px; height:150px; background-color:"+resultSearch[index].COULEURTANK
        colImg.appendChild(img)

        //col1 Stats
        col1Stats = document.createElement("div")
        col1Stats.className="col-sm-5"
        col1Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;border-left: 1px solid black; border-right: 1px solid black; padding-left:3%; margin-left:3%;"
        col1Stats.appendChild(document.createTextNode("Niveau: "+resultSearch[index].NIVEAU))
        col1Stats.appendChild(document.createElement("br"))
        col1Stats.appendChild(document.createTextNode("Parties gagnees: "+resultSearch[index].PARTIEGAGNE))
        col1Stats.appendChild(document.createElement("br"))
        col1Stats.appendChild(document.createTextNode("Parties jouees: "+resultSearch[index].PARTIEJOUE))
        col1Stats.appendChild(document.createElement("br"))
        if(resultSearch[index].PARTIEGAGNE == 0){
            col1Stats.appendChild(document.createTextNode("Ratio victoire: 0%"))
        }else{
            col1Stats.appendChild(document.createTextNode("Ratio victoire: "+(resultSearch[index].PARTIEJOUE/resultSearch[index].PARTIEGAGNE)*100+"%"))
        }

        col2Stats = document.createElement("div")
        col2Stats.className="col-sm-4"
        col2Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;"

        col2Stats.appendChild(document.createTextNode("Map favorite: "+mapFavorites[index]))

        row2.appendChild(colImg)
        row2.appendChild(col1Stats)
        row2.appendChild(col2Stats)

        node.appendChild(row1)
        node.appendChild(row2)
        node.appendChild(row3)
        document.getElementById("searchResults").appendChild(node)

    });
}
