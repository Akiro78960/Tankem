var resultSearch = null
var mapFavorites = []
var currentPage = 0
var usernameLoggedIn = null


function search(){
    var searchbar = document.getElementById("searchBar")
    $.ajax({
        url: 'ajaxSearch.php',
        type: 'POST',
        data: {searchKey: searchbar.value}
    })
    .done(function(r) {
        document.getElementById("searchResults").innerHTML=""
        resultSearch = JSON.parse(r)[0]
        usernameLoggedIn = JSON.parse(r)[1]
        console.log(resultSearch);
        console.log(usernameLoggedIn);
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
            displayInfos()
        })
    })
}

function displayInfos(){
    document.getElementById("searchResults").innerHTML=""
    // $(resultSearch).each(function(index) {
    for (var i = 0; i < 5; i++) {
            if(resultSearch[5*currentPage+i] != null){

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
                if(resultSearch[5*currentPage+i].USERNAME == usernameLoggedIn){
                    texte = document.createTextNode(""+resultSearch[5*currentPage+i].USERNAME + " " + calculateName(resultSearch[5*currentPage+i]) + " ("+resultSearch[5*currentPage+i].SURNAME+" "+resultSearch[5*currentPage+i].NAME+")")
                }else {
                    texte = document.createTextNode(""+resultSearch[5*currentPage+i].USERNAME + " " + calculateName(resultSearch[5*currentPage+i]))
                }
                txtname.appendChild(texte)
                colName.appendChild(txtname)
                row1.appendChild(colName)
                row1.style="background-color:E0E0E0;border:1px solid black"


                //row2
                colImg = document.createElement("div")
                img = document.createElement("img")
                colImg.className="col-sm-2"
                img.src="images/tankAlpha.png"
                img.style="width:150px; height:150px; background-color:"+resultSearch[5*currentPage+i].COULEURTANK
                colImg.appendChild(img)

                //col1 Stats
                col1Stats = document.createElement("div")
                col1Stats.className="col-sm-5"
                col1Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;border-left: 1px solid black; border-right: 1px solid black; padding-left:3%; margin-left:3%;"
                col1Stats.appendChild(document.createTextNode("Niveau: "+resultSearch[5*currentPage+i].NIVEAU))
                col1Stats.appendChild(document.createElement("br"))
                col1Stats.appendChild(document.createTextNode("Parties gagnees: "+resultSearch[5*currentPage+i].PARTIEGAGNE))
                col1Stats.appendChild(document.createElement("br"))
                col1Stats.appendChild(document.createTextNode("Parties jouees: "+resultSearch[5*currentPage+i].PARTIEJOUE))
                col1Stats.appendChild(document.createElement("br"))
                if(resultSearch[5*currentPage+i].PARTIEJOUE == 0){
                    col1Stats.appendChild(document.createTextNode("Ratio victoire: 0%"))
                }else{
                    col1Stats.appendChild(document.createTextNode("Ratio victoire: "+((resultSearch[5*currentPage+i].PARTIEGAGNE/resultSearch[5*currentPage+i].PARTIEJOUE)*100).toFixed(2)+"%"))
                }

                col2Stats = document.createElement("div")
                col2Stats.className="col-sm-4"
                col2Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;"

                if(mapFavorites[5*currentPage+i].length > 0){
                    col2Stats.appendChild(document.createTextNode("Map favorite: "+mapFavorites[5*currentPage+i][0].NOMNIVEAU))
                }else{
                    col2Stats.appendChild(document.createTextNode("Map favorite: "+"None"))
                }

                row2.appendChild(colImg)
                row2.appendChild(col1Stats)
                row2.appendChild(col2Stats)

                node.appendChild(row1)
                node.appendChild(row2)
                node.appendChild(row3)
                document.getElementById("searchResults").appendChild(node)
            }
        }

    // });
}


function goPrevious(){
    if(currentPage > 0){
        currentPage--
        displayInfos()
    }
}

function goNext(){
    if((currentPage+1) < (resultSearch.length/5)){
        currentPage++
        displayInfos()
    }
}
