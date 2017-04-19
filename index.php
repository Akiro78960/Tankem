<?php
	require_once("action/IndexAction.php");

	$action = new IndexAction();

	$action->execute();

	require_once("partial/header.php");
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
  <div class="py-5 text-center">
	<div class="container">
	  <div class="row text-center">
		<div class="col-md-3 text-center mx-auto">
		  <form class="text-center">
			<div class="form-group text-center w-100" id="login-email"> <label>Email address</label> <input type="email" class="form-control" placeholder="Enter email"> </div>
			<div class="form-group text-center w-100" id="login-password"> <label class="text-center">Password</label> <input type="password" class="form-control" placeholder="Password"> </div> <button type="submit" class="btn btn-primary text-center">Login</button> </form>
		  <p class="">New to this website? Signup, it's free! There are hundreds of sexy singles near your area waiting to meet you.<br></p><a href="Signup.php" class="btn btn-primary">Signup<br></a></div>
	  </div>
	</div>
  </div>

<?php
	require_once("partial/footer.php");