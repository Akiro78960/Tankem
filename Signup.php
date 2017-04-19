<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css">
  <link rel="stylesheet" href="Untitled.css" type="text/css">
  <title>Signup</title>
  <meta name="description" content="This page is used to signup for Tankem"> </head>

<body>
  <nav class="navbar navbar-expand-md navbar-light bg-faded">
    <div class="container">
      <a class="navbar-brand" href="#"><br></a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
               </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
        <ul class="navbar-nav ">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Home</a> </li>
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
  <div class="py-5 mx-auto text-center bg-faded" id="mainContainer">
    <div class="w-100 container">
      <div class="row text-center w-100 mx-auto" id="fixedcontainer">
        <div class="col-md-11 text-center mx-auto">
          <form class="">
            <div class="form-group w-25" id="signupemail"> <label>Email address</label> <input type="email" class="form-control" placeholder="Enter email"> </div>
            <div class="form-group w-25" id="signupPrenom"> <label>Prenom<br></label> <input type="text" class="form-control" placeholder="Prenom"> </div>
            <div class="form-group w-25" id="signupPassword"> <label>Password</label> <input type="password" class="form-control" placeholder="Password"> </div>
            <div class="form-group w-25" id="nom"> <label>Nom<br></label> <input type="text" class="form-control" placeholder="Nom"> </div>
            <div class="form-group w-25" id="reEnterPassword"> <label>Re-enter&nbsp;Password</label> <input type="password" class="form-control" placeholder="Re-enter Password"> </div>
            <div class="form-group w-25" id="signupUsername"> <label>Nom utilisateur</label> <input type="text" class="form-control" placeholder="Nom utilisateur"> </div>
            <div class="form-group w-25" id="registerColor"> <label>Couleur de tank voulue</label> <input type="color" class="form-control"> </div> <button type="submit" class="btn btn-primary">Register</button></form>
        </div>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
  <script src="https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js"></script>
</body>

</html>