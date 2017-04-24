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
            texte = document.createTextNode("Nom: "+result[index].NAME + " " + calculateName(result[index]))
            node.appendChild(texte)
            node.appendChild(document.createElement("br"))
            node.appendChild(document.createTextNode("Niveau: "+result[index].NIVEAU))
            node.appendChild(document.createElement("br"))
            document.getElementById("searchResults").appendChild(node)

        });
    })

}
