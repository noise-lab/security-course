<?php
ob_start();

$db_host="localhost"; // Host name 
$db_username="project2"; // Mysql username 
$db_password="ac5ebdce383d36d7498e24553b8b96c158a23577fb747317"; // Mysql password 
$db_name="project2"; // Database name 

mysql_connect($db_host, $db_username, $db_password) or die("Cannot connect to MySQL.");
mysql_select_db($db_name) or die("Cannot select database.");

$username = 'victim';
$password = '719a67994e0d14244f00cb06a9f33371';
$hash = md5($password, true);
$query = "INSERT INTO users (username,password,passwordhash) VALUES('$username', '$password', '$hash')";
$results = mysql_query($query);
	
if (mysql_errno() > 0) {
    echo "Error in MySQL query.";
} else {
    echo "Done.";
}

ob_end_flush();
?>
