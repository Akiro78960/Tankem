<html>
    <head>
    <title>Search Box Example 2 - default placeholder text gets cleared on click</title>
    <meta name="ROBOTS" content="NOINDEX, NOFOLLOW" />
    <!-- JAVASCRIPT to clear search text when the field is clicked -->
    <script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="js/search.js"></script>
    <script type="text/javascript">
    // window.onload = function(){
    // 	//Get submit button
    // 	var submitbutton = document.getElementById("tfq");
    // 	//Add listener to submit button
    // 	if(submitbutton.addEventListener){
    // 		submitbutton.addEventListener("click", function() {
    // 			if (submitbutton.value == 'Search our website'){//Customize this text string to whatever you want
    // 				submitbutton.value = '';
    // 			}
    // 		});
    // 	}
    // }
    </script>
    </head>
    <body>
        <div class="searchArea" style="text-align:center">
            <input type="text" id="searchBar"size="21" maxlength="120" placeholder="chercher un joueur">
            <input type="button", id="btnfind" value="find" onclick="search()">
        </div>
    </body>
</html>
