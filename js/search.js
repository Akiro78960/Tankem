// $(document).ready(function() {
//     console.log("ready");
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
        result = JSON.parse(r)
        console.log(result);
        $(result).each(function(index) {
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
            texte = document.createTextNode(""+result[index].USERNAME + " " + calculateName(result[index]) + " ("+result[index].SURNAME+" "+result[index].NAME+")")
            txtname.appendChild(texte)
            colName.appendChild(txtname)
            row1.appendChild(colName)
            row1.style="background-color:E0E0E0;border:1px solid black"


            //row2
            colImg = document.createElement("div")
            img = document.createElement("img")
            colImg.className="col-sm-2"
            img.src="images/tankAlpha.png"
            img.style="width:150px; height:150px; background-color:"+result[index].COULEURTANK
            colImg.appendChild(img)

            col1Stats = document.createElement("div")
            col1Stats.className="col-sm-5"
            col1Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;border-left: 1px solid black; border-right: 1px solid black; padding-left:3%; margin-left:3%;"
            col1Stats.appendChild(document.createTextNode("Niveau: "+result[index].NIVEAU))
            col1Stats.appendChild(document.createElement("br"))
            col1Stats.appendChild(document.createTextNode("Parties gagnees: "+result[index].PARTIEGAGNE))
            col1Stats.appendChild(document.createElement("br"))
            col1Stats.appendChild(document.createTextNode("Parties jouees: "+result[index].PARTIEJOUE))
            col1Stats.appendChild(document.createElement("br"))
            if(result[index].PARTIEGAGNE == 0){
                col1Stats.appendChild(document.createTextNode("Ratio victoire: 0%"))
            }else{
                col1Stats.appendChild(document.createTextNode("Ratio victoire: "+(result[index].PARTIEJOUE/result[index].PARTIEGAGNE)*100+"%"))
            }

            row2.appendChild(colImg)
            row2.appendChild(col1Stats)


            //row3
            


            node.appendChild(row1)
            node.appendChild(row2)
            node.appendChild(row3)
            // node.appendChild(document.createElement("br"))
            // node.appendChild(document.createTextNode("Niveau: "+result[index].NIVEAU))
            // node.appendChild(document.createElement("br"))
            document.getElementById("searchResults").appendChild(node)

        });
    })

}
