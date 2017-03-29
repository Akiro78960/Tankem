class DTOTuile{
	constructor(posX, posY, type, hasTree){
		this.posX = posX;
		this.posY = posY;
		this.type = type;
		this.hasTree = hasTree;
		this.idNiveau = 0;
	}

	setId(id){
		this.idNiveau = id;
	}
}