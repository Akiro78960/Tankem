<?php
	class DTOspawn {
		public static $pos_x;
		public static $pos_y;
		public static $id_niveau;
		public static $no_player;

		public function __construct($pos_x, $pos_y, $id_niveau, $no_player) {
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
			$this->id_niveau = $id_niveau;
			$this->no_player = $no_player;
		}
	}
