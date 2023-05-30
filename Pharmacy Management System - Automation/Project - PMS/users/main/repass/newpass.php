<?php
include("../dbconnect.php");

session_start();



?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Ganpat University</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="all,follow">
    <!-- Bootstrap CSS-->
    <link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
    <!-- Font Awesome CSS-->
    <link rel="stylesheet" href="vendor/font-awesome/css/font-awesome.min.css">
    <!-- Fontastic Custom icon font-->
    <link rel="stylesheet" href="css/fontastic.css">
    <!-- Google fonts - Poppins -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
    <!-- theme stylesheet-->
    <link rel="stylesheet" href="css/style.blue.css" id="theme-stylesheet">
    <!-- Custom stylesheet - for your changes-->
    <link rel="stylesheet" href="css/custom.css">
    <!-- Favicon-->
    <link rel="shortcut icon" href="img/favicon.ico">
    <!-- Tweaks for older IEs--><!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
  </head>
  <body>
    <div class="page login-page">
      <div class="container d-flex align-items-center">
        <div class="form-holder has-shadow">
          <div class="row">
            <!-- Logo & Information Panel-->
            <div class="col-lg-6">
              <div class="info d-flex align-items-center">
                <div class="content">
                  <div class="logo">
                    <h1>Welcome to Ganpat University Student Login </h1>
                  </div>
                </div>
              </div>
            </div>
            <!-- Form Panel    -->
            <div class="col-lg-6 bg-white">
              <div class="form d-flex align-items-center">
                <div class="content">
                  <form role="form" method="post">
				   <fieldset>
                     <div class="form-group">
                                    <input class="form-control" placeholder="Password" name="pass" required autofocus />
                                </div>
                      <div class="form-group">
                                    <input class="form-control" placeholder="Re-Password" name="repass" required autofocus />
                                </div>
                   
					 <input type="submit" class="btn btn-primary" name="btn_change" value="Change">
                    <!-- This should be submit button but I replaced it with <a> for demo purposes-->
					</fieldset>



<?php


 

$pass="";
$repass="";
$email="";

if(isset($_POST["btn_change"]))
{

    $pass=$_POST["pass"];
    $repass=$_POST["repass"];
    $email=$_SESSION["email"];

if($pass == $repass)
{
    $pass = $pass;

    

// check email from table

$stu="Select * from student_master where stu_mail='$email'";



$sturesult=$conn->query($stu);
$stucnt=mysqli_num_rows($sturesult);






        if($stucnt==1)
        {
            $table="student_master";
            $qry="update $table set stu_pass='$pass' where stu_mail='$email'";
            $fire=$conn->query($qry);
            // echo "<script>alert('Your Password Sucessfully Updated');</script>";
            header("location:../StudentLogin.php");
        }       
        else
        {
            echo "<script>alert('Email is Wrong');</script>";       
        }
    

                                
}
else
{
    echo "<script>alert('Password and Re-Password is wrong');</script>";
    $pass = "";
}



}









?>










                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="copyrights text-center">
        <a href="https://www.google.com" class="external"></a>
        
      </div>
    </div>
    <!-- Javascript files-->
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="vendor/popper.js/umd/popper.min.js"> </script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <script src="vendor/jquery.cookie/jquery.cookie.js"> </script>
    <script src="vendor/chart.js/Chart.min.js"></script>
    <script src="vendor/jquery-validation/jquery.validate.min.js"></script>
    <!-- Main File-->
    <script src="js/front.js"></script>
  </body>
</html>