<?php
    require_once("action/IndexAction.php");

    $action = new IndexAction();
    $action->execute();
?>

<!DOCTYPE html>
<html>
    <head>
        <script src="JS/spawn.js"></script>
        <script src="JS/Tile.js"></script>
        <script src="JS/Niveau.js"></script>
        <script src="JS/main.js"></script>
        <script src="JS/Selector.js"></script>
        <script src="JS/jquery.js"></script>
        <script src="JS/DTONiveau.js"></script>
        <script src="JS/DTOTuile.js"></script>
        <link rel="stylesheet" href="style.css" type="text/css"/>
        <title>level editor</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    </head>
    <body>
        <main>
            <div>
                Nom Niveau: <input type="text" id="nomNiveau"/>
                Taille X: <input type="text" id="tailleX" size="2"/>
                Taille Y: <input type="text" id="tailleY" size="2"/>
                <input type="button" id="tailleTuile" value="Nouvelle taille" OnClick="clickButton()"/>
                <input type="button" id="sauvegarder" value="Sauvegarder" OnClick="envoyerTables()"/>
            </div>
            <div>
                Status: <input type="text" id="status"/>
                Delai minimum des objets: <input type="text" id="itemDelMin"/>
                Delai maximum des objets: <input type="text" id="itemDelMax"/>
            </div>
            <canvas height="800", width="800" id="canvas"></canvas>
        </main>
    </body>
</html>
