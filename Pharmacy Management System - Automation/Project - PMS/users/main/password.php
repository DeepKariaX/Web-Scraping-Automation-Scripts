 <?php
		include('dbconnect.php');
		session_start();

		// $query = "SELECT * FROM student_master WHERE stu_enro='".$_POST['username']."' AND stu_pass='".$_POST['userpassword']."';";

		$query = "SELECT * FROM ".$_POST['role']." WHERE email='".$_POST['email']."' AND password='".$_POST['password']."';";
		// echo $query;
		$qry1=$conn->query($query);
		$fdata=$qry1->fetch_assoc();

		if($fdata['email'] == $_POST['email'] && $fdata['password'] == $_POST['password'])
		{
			$_SESSION['role'] = $fdata['role'];
			$_SESSION['id'] = $fdata['id'];
			
			header("Location:dashboard/index.php");	
			exit;
		}
		else
		{
			header("Location:login.php?er=2");
			exit;
		}

?>