<?php
	require_once("action/InfosAction.php");

	$action = new InfosAction();

	$action->execute();

	require_once("Partial/header.php");
?>
  <div class="py-5">
	<div class="container">
	  <div class="row">
		<div class="col-md-12">
		  <h1 class="display-1 text-center">Tank'Em<br></h1>
		</div>
	  </div>
	</div>
  </div>
  <div class="modal">
	<div class="modal-dialog">
	  <div class="modal-content">
		<div class="modal-header"> <button class="close" data-dismiss="modal" type="button">×</button>
		  <h4 class="modal-title">Modal title</h4>
		</div>
		<div class="modal-body">
		  <p>One fine body...</p>
		</div>
		<div class="modal-footer"> <a class="btn btn-default" data-dismiss="modal">Close</a> <a class="btn btn-primary">Save
				changes</a> </div>
	  </div>
	</div>
  </div>
  <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
  <script src="https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js"></script>
</body>

</html>