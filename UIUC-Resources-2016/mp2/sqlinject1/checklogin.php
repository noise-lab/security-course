<?php
ob_start();

$db_host="localhost"; // Host name 
$db_username="project2-ro"; // Mysql username
$db_password="5923d6e6cd5d99d7079205bf17130c44dfe07de6ab66612b9344c374fd6419bc"; // TODO: change Mysql password to new dbro.secret
$db_name="project2"; // Database name 

mysql_connect($db_host, $db_username, $db_password) or die("Cannot connect to MySQL.");
mysql_select_db($db_name) or die("Cannot select database.");

if (isset($_POST['username']) and isset($_POST['password'])) {
    $username = str_replace("'", "''", $_POST['username']);
    $password = str_replace("'", "''", $_POST['password']);

    $query = "SELECT * FROM users WHERE username='$username' and password='$password'";
    $results = mysql_query($query);

    if (mysql_errno() > 0) {
        echo "Error in MySQL query.";
    } elseif (mysql_num_rows($results) > 0) {
        echo "<h1>Login successful! (" . htmlspecialchars($username) . ")</h1>";
	if ($username == "victim") {
  	   echo "<p><b>Submit the following line as your solution:</b><br>";
	   echo "<tt>username=" . rawurlencode($_POST['username']) . "&password=" . rawurlencode($_POST['password']);
	}
    } else {
        echo "Incorrect username or password.";
    }
} else {
    echo "Invalid submission.";
}

ob_end_flush();
?>
