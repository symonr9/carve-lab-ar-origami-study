<?php 

$dbhost = 'oniddb.cws.oregonstate.edu';
$dbname = 'ramossy-db';
$dbuser = 'ramossy-db';
$dbpass = 'pRv0DFcOgN3DeZgP';

$mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

?>
