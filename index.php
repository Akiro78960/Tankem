<?php
	require_once("action/indexAction.php");

	$action = new IndexAction();

	$action->execute();

	// require_once("Partial/header.php");
?>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css">
  <link rel="stylesheet" href="css/Untitled.css" type="text/css"> </head>

<body class="mx-auto">
  <nav class="navbar navbar-expand-md navbar-light bg-faded">
	<div class="container">
	  <a class="navbar-brand" href="#"><br></a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				  <span class="navbar-toggler-icon"></span>
			   </button>
	  <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
		<ul class="navbar-nav ">
		  <li class="nav-item active"> <a class="nav-link" href="index.php">Home</a> </li>
		  <li class="nav-item"> <a class="nav-link" href="#">Link</a> </li>
		  <li class="nav-item"> <a class="nav-link disabled" href="#">Disabled</a> </li>
		</ul>
	  </div>
	</div>
  </nav>
  <div class="py-5">
	<div class="container">
	  <div class="row">
		<div class="col-md-12">
		  <h1 class="display-1 text-center">Tank'Em<br></h1>
		</div>
	  </div>
	</div>
  </div>
  <div class="py-5 text-center">
	<div class="container">
	  <div class="row text-center">
		<div class="col-md-3 text-center mx-auto">
		  <form class="text-center">
	  	<?php 
				if ($action->wrongLogin) {
					?>
					<div class="error-div"><strong>Erreur : </strong>Connexion erronée</div>
					<?php
			  	}
		  	?>
			<div class="form-group text-center w-100" id="login-email" name = "username"> <label>Email address</label> <input type="value" class="form-control" placeholder="Enter email"> </div>
			<div class="form-group text-center w-100" id="login-password" name = "pwd"> <label class="text-center">Password</label> <input type="password" class="form-control" placeholder="Password"> </div> <button type="submit" class="btn btn-primary text-center">Login</button> </form>
		  <p class="">New to this website? Signup, it's free! There are hundreds of sexy singles near your area waiting to meet you.<br></p><a href="Signup.php" class="btn btn-primary">Signup<br></a></div>
	  </div>
	</div>
  </div>
  <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
  <script src="https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js"></script>
</body>

</html>