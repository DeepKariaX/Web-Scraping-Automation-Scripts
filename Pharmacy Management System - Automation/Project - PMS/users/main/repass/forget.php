<?php
include("../dbconnect.php");

session_start();

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

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
                                    <input class="form-control" placeholder="Email" name="mail" required autofocus />
                                </div>
                    
                               
           <input type="submit" class="btn btn-primary" name="btn_check" value="CHECK">
                    <!-- This should be submit button but I replaced it with <a> for demo purposes-->
          </fieldset>









<?php


    
if (isset($_POST["btn_check"]))
{





$email=$_POST['mail'] ;
$_SESSION['email']=$email;
       

// check email from table

$stu="Select * from student_master where stu_mail='$email'";


$sturesult=$conn->query($stu);
$stucnt=mysqli_num_rows($sturesult);







       if($stucnt==1)
      {
        




       $abc="Select * from student_master where stu_mail='$email'";
       $q=mysqli_query($conn,"$abc");
       // echo $abc."<br><br>";
       $count= mysqli_num_rows($q);
       // echo $count;
       $row= mysqli_fetch_array($q);
       $otp= rand(100000,900000);
       $_SESSION['otp']=$otp;
      
        if($count>0)
        {
         

            //Load Composer's autoloader
            require 'files/vendor/autoload.php';

            $mail = new PHPMailer(true);                              // Passing `true` enables exceptions
           
            try {
                //Server settings
                $mail->SMTPDebug =0;                                 // Enable verbose debug output
                $mail->isSMTP();                                      // Set mailer to use SMTP
                $mail->Host = 'smtp.gmail.com';  // Specify main and backup SMTP servers
                $mail->SMTPAuth = TRUE;                               // Enable SMTP authentication
                $mail->Username = 'learning.management.system.guni@gmail.com';                 // SMTP username
                $mail->Password = 'lms_guni_lms';                           // SMTP password
                $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
                $mail->Port = 587;                                    // TCP port to connect to
                //Recipients
                $mail->setFrom('learning.management.system.guni@gmail.com', 'Learning Management System');
                $mail->addAddress($email, $email);     // Add a recipient
                //Content
                $mail->isHTML(true);                                  // Set email format to HTML
                $mail->Subject = 'Forget Password';
                $mail->Body = "Hi, $email.<br>Your <b>OTP</b> is <b>$otp</b>.";
               // $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
                 
                $mail->send();
                echo "<script>alert('OPT Has Been Send To Your Email');window.location='otp.php';</script>";
            }
            catch (Exception $e)
            {
                echo 'Message could not be sent. Mailer Error: ', $mail->ErrorInfo;
            }

        }
        else
        {
            echo "<script>alert('Email Not Found');</script>";
        }










      }        
      else
      {
                echo "<script>alert('Email not in System')</script>";
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