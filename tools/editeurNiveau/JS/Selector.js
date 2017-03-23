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
        console.log(this.x);
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
                if (this.x>0) {
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
            default:

        }
    }
}
