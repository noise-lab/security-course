<?php
ob_start();

$db_host="localhost"; // Host name
$db_username="inject_3"; // Mysql username
$db_password=""; // TODO: change Mysql password to new db.sqlinejct_3.secret
$db_name="proj2_inject3"; // Database name

mysql_connect($db_host, $db_username, $db_password) or die("Cannot connect to MySQL.");
mysql_select_db($db_name) or die("Cannot select database.");

if (isset($_GET['id'])) {
    $id= $_GET['id'];

    $query = "SELECT * FROM inject3_users WHERE id='$id' LIMIT 0,1";
    $result = mysql_query($query);
    // Only uncomment the following code for debugging!
    // We don't want to leak information.
    /* if (mysql_errno() > 0) {
       die(mysql_error());
    } */
    $row = mysql_fetch_array($result);
}

ob_end_flush();
?>


<!DOCTYPE html>
<html>
  <head>
    <title>sqlinject3</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style>
      .content { margin-top: 50px; }
      h2 { margin-top: 0; margin-bottom: 20px; }
    </style>
  </head>
  <body>
  <!--
	 "What could go wrong?"

                            jhalderm
  -->
    <div class="container">
      <div class="content">
	<div class="well" style="max-width: 475px; margin: 0 auto 10px;">
	  <h2>sqlinject3</h2>
          Enter the user ID:
          <form class="form-inline">
	    <div class="form-group">
              <input type="text" class="form-control" placeholder="id" name="id">
	    </div>
	    <button class="btn btn-primary" type="submit">Search</button>
          </form>
    <b>Results:</b><br>
    <?php
        if($row) {
            echo 'First name: ' . $row['first_name'];
            echo "<br>";
            echo 'Last name: ' . $row['last_name'];
        }
    ?>

	</div>
      </div>
    </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
