<?php
	class DTOtuile {
		public static $pos_x;
		public static $pos_y;
		public static $id_niveau;
		public static $type_tuile;
		public static $has_tree;

		public function __construct($pos_x, $pos_y, $id_niveau, $type_tuile, $has_tree) {
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
			$this->id_niveau = $id_niveau;
			$this->type_tuile = $type_tuile;
			$this->has_tree = $has_tree;
		}
	}
