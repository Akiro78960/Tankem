<?php
	class DTOpartie {
        public $id;
        public $id_map;
        public $creation_date;
        public $arrayJoueur1;
        public $arrayJoueur2;
        public $arrayProjectiles;
        public $arrayArmes;
        public $map;

		public function __construct($id, $id_map, $creation_date) {
			$this->id = $id;
			$this->id_map = $id_map;
			$this->creation_date = $creation_date;
			$this->arrayJoueur1 = [];
			$this->arrayJoueur2 = [];
			$this->arrayProjectiles = [];
			$this->arrayArmes = [];
		}
	}
