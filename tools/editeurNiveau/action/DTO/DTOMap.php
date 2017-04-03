<?php
	class DTOmap {
        public static $id_niveau;
        public static $name;
        public static $creation_date;
        public static $status;
        public static $size_x;
        public static $size_y;
        public static $item_delay_min;
        public static $item_delay_max;
        public static $array_tuiles;
        public static $array_spawns;

		public function __construct($id_niveau, $name, $creation_date, $status,
									$size_x, $size_y, $item_delay_min,
									$item_delay_max, $array_tuiles,
									$array_spawns) {
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
			$this->id_niveau = $id_niveau;
			$this->type_tuile = $type_tuile;
			$this->has_tree = $has_tree;
			$this->id_niveau = $id_niveau;
			$this->name = $name;
			$this->creation_date = $creation_date;
			$this->status = $status;
			$this->size_x = $size_x;
			$this->size_y = $size_y;
			$this->item_delay_min = $item_delay_min;
			$this->item_delay_max = $item_delay_max;
			$this->array_tuiles = $array_tuiles;
			$this->array_spawns = $array_spawns;
		}
	}
