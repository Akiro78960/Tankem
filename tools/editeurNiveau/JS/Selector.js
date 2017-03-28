class Selector{
    constructor(x,y,size){
        this.x = x;
        this.y = y;
        this.size = size;
    }

    tick(){
        var pixX = this.x * this.size + debX;
        var pixY = this.y * this.size + debY;
        ctx.strokeStyle = "red";
        ctx.beginPath();
        ctx.moveTo(pixX,pixY);
        ctx.lineTo(pixX + this.size, pixY);
        ctx.lineTo(pixX + this.size, pixY + this.size);
        ctx.lineTo(pixX, pixY + this.size);
        ctx.lineTo(pixX, pixY);
        ctx.stroke();
    }

    updatePosition(e){

        switch (e.key) {
            case "ArrowRight":
                if(this.x<niveau.tailleX-1){
                    ++this.x;
                }
                break
            case "ArrowLeft":
                if (this.x>0) {
                    --this.x;
                }
                break
            case "ArrowDown":
                if(this.y<niveau.tailleY-1){
                    ++this.y;
                }
                break
            case "ArrowUp":
                if (this.y>0) {
                    --this.y;
                }
                break
            case "0":
                niveau.setTile(this.x, this.y, 0)
                break;
            case "1":
                niveau.setTile(this.x, this.y, 1)
                break;
            case "2":
                niveau.setTile(this.x, this.y, 2)
                break;
            case "3":
                niveau.setTile(this.x, this.y, 3)
                break;
            case "4":
                niveau.setTile(this.x, this.y, 4)
                break;
            case "q":
                if(!niveau.isSpawnHere(this.x, this.y, 0))
                niveau.toggleTree(this.x, this.y)
                break
            case "a":
                var spawn = niveau.tabSpawn[0]
                if(!niveau.tabTile[this.x][this.y].hasTree && !niveau.isSpawnHere(this.x, this.y, 1)){
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else{
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[0].changePos(this.x, this.y)
                }
                break
            case "s":
                var spawn = niveau.tabSpawn[1]
                if(!niveau.tabTile[this.x][this.y].hasTree && !niveau.isSpawnHere(this.x, this.y, 2)){
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[1].changePos(this.x, this.y)
                }
                break
            case "d":
                var spawn = niveau.tabSpawn[2]
                if(!niveau.tabTile[this.x][this.y].hasTree && !niveau.isSpawnHere(this.x, this.y, 3)){
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[2].changePos(this.x, this.y)
                }
                break
            case "f":
                var spawn = niveau.tabSpawn[3]
                if(!niveau.tabTile[this.x][this.y].hasTree && !niveau.isSpawnHere(this.x, this.y, 4)){
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[3].changePos(this.x, this.y)
                }
                break
            default:
        }
    }
}
