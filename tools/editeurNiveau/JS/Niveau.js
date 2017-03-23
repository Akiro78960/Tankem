class Niveau{
    constructor(x,y){
        this.tailleX = x
        this.tailleY = y
        this.itemDelay = 10
        this.tabTile= []
        for (var x = 0; x < this.tailleX; x++) {
            this.tabTile[x] = new Array()
            for (var y = 0; y < this.tailleY; y++) {
                this.tabTile[x][y] = new Tile(x,y)
            }
        }
        this.tabTile[1][1].type = 1
        this.tabTile[2][2].type = 2
        this.tabTile[3][3].type = 3
        this.tabTile[4][4].type = 4
        this.tabTile[2][2].hasTree = 1
        this.tabTile[4][4].hasTree = 1
        this.tabTile[1][1].hasTree = 1
    }
    setSize(x,y){
        this.tailleX = x
        this.tailleY = y
    }
    setTile(x,y,type){
        this.tabTile[x][y].type=type
    }
}
