<?php

$totalTime = $_POST['totalTime'];
$step1 = $_POST['step1'];
$step2 = $_POST['step2'];
$step3 = $_POST['step3'];
$step4 = $_POST['step4'];
$step5 = $_POST['step5'];
$step6 = $_POST['step6'];
$step7 = $_POST['step7'];
$step8 = $_POST['step8'];
$step9 = $_POST['step9'];
$step10 = $_POST['step10'];
$step11 = $_POST['step11'];
$step12 = $_POST['step12'];
$step13 = $_POST['step13'];
$step14 = $_POST['step14'];
$step15 = $_POST['step15'];
$origamiType = $_POST['origamiType'];
$taskType = $_POST['taskType'];
$methodType = $_POST['methodType'];
$id = $_POST['id'];
$incompleteInput = $_POST['incompleteInput'];
$skippedStepsInput = $_POST['skippedStepsInput'];


include_once('./config.php');

/*
	The following code is within the config file: 
		$dbhost = '#hostname';
		$dbname = '#dbname';
		$dbuser = '#dbuser';
		$dbpass = '#dbpass';

		$mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
		if ($mysqli->connect_errno) {
			echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
		}
*/

//Note: Please modify this query if this code is to be 
//used to interfact with another database.
$query = "INSERT INTO  `ramossy-db`.`origami_data` (`id` ,`origami_type` ,`task_type`, `method_type` ,`incomplete_input` ,`skipped_steps` ,`total_time` ,`step1` ,`step2` ,`step3` ,`step4` ,`step5` ,`step6` ,`step7` ,`step8` ,`step9` ,`step10` ,`step11` ,`step12` ,`step13` ,`step14` ,`step15` , `date_time`) VALUES ('" . $id . "',  '" . $origamiType . "',  '" . $taskType . "','" . $methodType . "','" . $incompleteInput . "',  '" . $skippedStepsInput ."',  '" . $totalTime . "',  '" . $step1 . "',  '" . $step2 . "',  '" . $step3 . "',  '" . $step4 . "',  '" . $step5 . "',  '" . $step6 . "',  '" . $step7 . "',  '" . $step8 . "',  '" . $step9 . "',  '" . $step10 . "',  '" . $step11 . "',  '" . $step12 . "',  '" . $step13 . "',  '" . $step14 . "',  '" . $step15 . "',  NULL)";
$mysqli->query($query);

?>
			
					