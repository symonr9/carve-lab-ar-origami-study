<!--*****************************************************************************************************************
* Application Name: StopWatch
* Author: Symon Ramos
* Date: 3/5/19
* Description: This application allows data to be collected for origami tasks in either normal or augmented paper.
* The data is stored into a private database after being recorded. Numerous features, such as rewinding an invalid 
* step, accounting for skipped steps, and a checklist of the Experimental Protocol, are included.
*****************************************************************************************************************-->


<!--
Note: Future Implementation: References for creating charts within this web app. 
https://www.c-sharpcorner.com/blogs/chart-control-in-php-and-mysql-using-jpgraph1
https://gist.github.com/amrrashed/54287d69417c06295099
-->

<!DOCTYPE html>
<html lang="en">
<head>
	<?php require_once("./modules/header.php"); ?>
</head>
  
<body>

<?php require_once("./modules/navbar.php"); ?>

<br>
<div class="container">
	<div class="row">
		<div class="col-sm-4">
			<?php require_once("./modules/checklist.php"); ?>
		</div>
		
		<div class="col-sm-8">
			<div class="row">
				<div class="col-sm-12">
					<?php require_once("./modules/currentStepInterface.php"); ?>
				</div>
				
				<?php require_once("./modules/inputFields.php"); ?>

			</div>
			<br>
			<div class="row">
				<?php require_once("./modules/table.php"); ?>
			</div>
			
			<div class="row">
				<div id="finalTime"></div>
				<a href="" id="dlink"></a>
			</div>
		</div>
	</div>
	
</div>

</body>

<script type="text/javascript" src="./assets/stopwatch.js"></script>

</html>