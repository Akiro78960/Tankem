var ctx = null
var niveau = null
var sizeTuile =50;
var longueurGrid = null;
var hauteurGrid = null;
var debX = null;
var debY = null;
var imgblock1 = new Image()
var imgblock2 = new Image()
var imgblock3 = new Image()
var imgblock4 = new Image()
var imgtree = new Image()
var selector = null;
var is0pushed = false
var is1pushed = false
var is2pushed = false
var is3pushed = false
var is4pushed = false


document.onkeydown = function (e) {
    console.log(e);
    switch(e.key){
        case "0":
            is0pushed=true
            break
    }
    selector.updatePosition(e)
}

document.onkeyup = function(e){
    switch(e.key){
        case "0":
            is0pushed=false
            break
    }
}

window.onload = function(){

    ctx = document.getElementById("canvas").getContext("2d")
    niveau = new Niveau(12,12)

    imgblock1.src="images/block1.png"
    imgblock2.src="images/block2.jpg"
    imgblock3.src="images/block3.jpg"
    imgblock4.src="images/block4.png"
    imgtree.src="images/treeAlpha.png"

    longueurGrid = sizeTuile * niveau.tailleX;
    hauteurGrid = sizeTuile * niveau.tailleY;
    debX = (document.getElementById("canvas").width - longueurGrid) / 2;
    debY = (document.getElementById("canvas").height - hauteurGrid) / 2;

    selector = new Selector(0,0,sizeTuile);

    tick()
}

function tick(){

    ctx.clearRect(0,0,document.getElementById("canvas").width,document.getElementById("canvas").height)
    drawTiles();
    drawGrid();
    selector.tick();

    window.requestAnimationFrame(tick)
}

function drawGrid(){
    ctx.strokeStyle = "black"
    for(var i = 0; i <= niveau.tailleY; ++i){
        ctx.beginPath();
        ctx.moveTo(debX,debY + sizeTuile * i);
        ctx.lineTo(debX + sizeTuile * niveau.tailleX, debY + sizeTuile * i);
        ctx.stroke();
    }
    for(var i = 0; i <= niveau.tailleX; ++i){
        ctx.beginPath();
        ctx.moveTo(debX + sizeTuile * i, debY);
        ctx.lineTo(debX + sizeTuile * i, debY + sizeTuile * niveau.tailleY);
        ctx.stroke();
    }
}

function drawTiles() {
    for(var y = 0; y < niveau.tailleY; ++y){
        for(var x = 0; x < niveau.tailleX; ++x){
            switch(niveau.tabTile[x][y].type){
                case 0:
                    ctx.fillStyle = "grey"
                    ctx.fillRect(debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile)
                    break
                case 1:
                    ctx.drawImage(imgblock1,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 2:
                    ctx.drawImage(imgblock2,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 3:
                    ctx.drawImage(imgblock3,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
                case 4:
                    ctx.drawImage(imgblock4,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
                    break
            }
            if(niveau.tabTile[x][y].hasTree){
                ctx.drawImage(imgtree, sizeTuile/4+ debX + x * sizeTuile, sizeTuile/4+ debY + y * sizeTuile, sizeTuile/2, sizeTuile/2)
            }
        }
    }
}

function clickButton(){
    var tailleXinput = parseInt(document.getElementById("tailleX").value)
    var tailleYinput = parseInt(document.getElementById("tailleY").value)
    if(tailleXinput >= 6 && tailleXinput <= 12 && tailleYinput >= 6 && tailleYinput <= 12){
        niveau.setSize(tailleXinput, tailleYinput)
        console.log("tailleX: " + tailleXinput + "  tailleY: " + tailleYinput);
    }
    longueurGrid = sizeTuile * niveau.tailleX;
    hauteurGrid = sizeTuile * niveau.tailleY;
    debX = (document.getElementById("canvas").width - longueurGrid) / 2;
    debY = (document.getElementById("canvas").height - hauteurGrid) / 2;
}
