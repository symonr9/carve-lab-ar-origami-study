//Instantiate global variables.
var x;
var lapx;

function startTimer(){
	// Set the date we're counting down to
	var countDownDate = new Date().getTime();
	
	clearInterval(x);
	// Update the count down every 1 second
	x = setInterval(function() {

		// Get todays date and time
		var now = new Date().getTime();
		
		// Find the distance between now an the count down date
		var distance = now - countDownDate;
		
		// Time calculations for days, hours, minutes and seconds
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
		var mseconds = Math.floor((distance % 1000));
		// Output the result in an element with id="demo"
		document.getElementById("demo").innerHTML = minutes + ":" + seconds + ":" + mseconds + "";
		
	}, 10);
}

function lapstartTimer(){
	// Set the date we're counting down to
	var countDownDate = new Date().getTime();
	//countDownDate.setMilliseconds(t.getMilliseconds() - 1);
	
	clearInterval(lapx);
	// Update the count down every 1 second
	lapx = setInterval(function() {

		// Get todays date and time
		var now = new Date().getTime();

		// Find the distance between now an the count down date
		var distance = now - countDownDate;
		
		// Time calculations for days, hours, minutes and seconds
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
		var mseconds = Math.floor((distance % 1000));
		// Output the result in an element with id="demo"
		document.getElementById("lapdemo").innerHTML = minutes + ":" + seconds + ":" + mseconds + "";
		
	}, 10);
}
	

//The times of each step are recorded as milliseconds in the 
//database.
function changeToMs(stepNum){							
	stepNumSplit = stepNum.split(":");
	time = Number(stepNumSplit[2]) + Number(stepNumSplit[1] * 1000) + Number(stepNumSplit[0] * 1000 * 60);
	return time;
}
	
//Note: Boat has 15 steps, Swan has 10 steps.
$('#startTimerBtn').on('click', function (e) {
	//When startTimer is pressed for the first time...
	if(document.getElementById('startTimerBtn').innerHTML == "Start"){
		var validStart = false;
		var origamiType = document.getElementById("origamiTypeInput").value;
		var taskType = document.getElementById("taskTypeInput").value;
		var methodType = document.getElementById("methodTypeInput").value;
		var id = document.getElementById("participantID").value;
		
		$('#incompleteInput').val('None').change();
		
		var skippedStepsInput = document.getElementById("skippedStepsInput");
		skippedStepsInput.value = "";
		
		if(origamiType != "None" && taskType != "None" && methodType != "None" && id != ""){
			validStart = true;
		}
		
		if(validStart){
			document.getElementById("origamiTD").innerHTML = origamiType;
			document.getElementById("taskTD").innerHTML = taskType;
			document.getElementById("idTD").innerHTML = id;
			
			document.getElementById("currentStep").innerHTML = "STEP 1";
			
				
			if(taskType != "Test1" && taskType != "Test2"){
				if(origamiType == "Boat"){
					$('#instructionsDiv').text(boatInstructions[0]);
				}
				else if(origamiType == "Swan"){
					$('#instructionsDiv').text(swanInstructions[0]);
				}
			}
			else{
				$('#instructionsDiv').text("Test task: good luck!");
			}
			
			if(methodType == "Normal"){
				$('#instructionsDiv').text("Normal task: good luck!");
			}
			
			$('#instructionsDiv').css("color", "black");
					
			var i = 1; 
			for(i; i < 18; i++){
				document.getElementById("steptime" + i).innerHTML = "0:00:00";
				document.getElementById("stepname" + i).style.backgroundColor = "white";
				document.getElementById("steptime" + i).style.backgroundColor = "white";
				
				document.getElementById("lapsteptime" + i).innerHTML = "0:00:00";
				document.getElementById("lapsteptime" + i).style.backgroundColor = "white";
			}						
				
			//Remove Extra Steps
			switch(origamiType){
				case "Boat":
					var i = 16;
					for(i; i < 18; i++){
						document.getElementById("stepname" + i).style.backgroundColor = "lightgray";
						document.getElementById("steptime" + i).style.backgroundColor = "lightgray";
						document.getElementById("lapsteptime" + i).style.backgroundColor = "lightgray";
					}
					break;
				case "Swan":
					var i = 11;
					for(i; i < 18; i++){
						document.getElementById("stepname" + i).style.backgroundColor = "lightgray";
						document.getElementById("steptime" + i).style.backgroundColor = "lightgray";
						document.getElementById("lapsteptime" + i).style.backgroundColor = "lightgray";
					}
					break;
			}
			
			if(taskType == "Test1" || taskType == "Test2"){
				var i = 2;
				for(i; i < 18; i++){
					document.getElementById("stepname" + i).style.backgroundColor = "lightgray";
					document.getElementById("steptime" + i).style.backgroundColor = "lightgray";
					document.getElementById("lapsteptime" + i).style.backgroundColor = "lightgray";
				}
			}
			
			//Toggle the start timer button.
			document.getElementById("startTimerBtn").innerHTML = "Finish and Save";
			
			//Reset the timer.
			document.getElementById("demo").innerHTML = "01:00:00";
			//Start the timer.
			startTimer();
			lapstartTimer();
		}
		else{
			alert("Please provide the origami type, task type, method type, and participant ID first.");
		}
	}
	//Otherwise, startTimer has already been pressed. The button text would currently say
	//"Finish and Save". When this code is reached, the data recorded will be saved into the database.
	else{
		//Toggle the start timer button.
		document.getElementById("startTimerBtn").innerHTML = "Start";
		
		//Stop the timer.
		clearInterval(x);
		clearInterval(lapx);
		
		var origamiType = document.getElementById("origamiTypeInput").value;
		var taskType = document.getElementById("taskTypeInput").value;
		var methodType = document.getElementById("methodTypeInput").value;
		var id = document.getElementById("participantID").value;
		
		var incompleteInput = document.getElementById("incompleteInput").value;
		var skippedStepsInput = document.getElementById("skippedStepsInput").value;
		
		
		var today = new Date();
		var dd = today.getDate();
		var mm = today.getMonth()+1; //January is 0!
		var yyyy = today.getFullYear();

		if(dd<10) {
			dd = '0'+dd;
		} 

		if(mm<10) {
			mm = '0'+mm;
		} 

		today = mm + '-' + dd + '-' + yyyy;

		var totalTime = changeToMs(document.getElementById("demo").innerHTML); 
		var step1 = changeToMs(document.getElementById("lapsteptime1").innerHTML);
		var step2 = changeToMs(document.getElementById("lapsteptime2").innerHTML);
		var step3 = changeToMs(document.getElementById("lapsteptime3").innerHTML);
		var step4 = changeToMs(document.getElementById("lapsteptime4").innerHTML);
		var step5 = changeToMs(document.getElementById("lapsteptime5").innerHTML);
		var step6 = changeToMs(document.getElementById("lapsteptime6").innerHTML);
		var step7 = changeToMs(document.getElementById("lapsteptime7").innerHTML);
		var step8 = changeToMs(document.getElementById("lapsteptime8").innerHTML);
		var step9 = changeToMs(document.getElementById("lapsteptime9").innerHTML);
		var step10 = changeToMs(document.getElementById("lapsteptime10").innerHTML);
		var step11 = changeToMs(document.getElementById("lapsteptime11").innerHTML);
		var step12 = changeToMs(document.getElementById("lapsteptime12").innerHTML);
		var step13 = changeToMs(document.getElementById("lapsteptime13").innerHTML);
		var step14 = changeToMs(document.getElementById("lapsteptime14").innerHTML);
		var step15 = changeToMs(document.getElementById("lapsteptime15").innerHTML);

		//Perform a POST Request to push the data into the database.
		$.ajax({
			type: 'POST',
			url: './ajax.php',
			dataType: 'html',
			data: {
					totalTime: totalTime, 
					step1: step1, 
					step2: step2, 
					step3: step3, 
					step4: step4,
					step5: step5, 
					step6: step6,
					step7: step7,
					step8: step8, 
					step9: step9, 
					step10: step10, 
					step11: step11,
					step12: step12,
					step13: step13,
					step14: step14,
					step15: step15,
					origamiType: origamiType, 
					taskType: taskType,
					methodType: methodType,
					id: id, 
					incompleteInput: incompleteInput,
					skippedStepsInput: skippedStepsInput,
					action: 'submitForApproval'},
					success: function(result)
					{
						alert("Success, case data pushed into database!!");
					},
					error: function (xhr, ajaxOptions, thrownError) {
						alert(xhr.status);
						alert(xhr.responseText);
						alert(thrownError);
					}
		});
	}
});

$('#finishStepBtn').on('click', function (e) {
	//Get current step.
	var currentStep = document.getElementById("currentStep").innerHTML.substring(5);
	
	if(document.getElementById("stepname" + currentStep).style.backgroundColor != "lightgray"){				
		//Set the cell of the current step to the time of the timer.
		document.getElementById("steptime" + currentStep).innerHTML = document.getElementById("demo").innerHTML;
		document.getElementById("lapsteptime" + currentStep).innerHTML = document.getElementById("lapdemo").innerHTML;
		
		
		var origamiType = document.getElementById("origamiTypeInput").value;
		var taskType = document.getElementById("taskTypeInput").value;
		var methodType = document.getElementById("methodTypeInput").value;
		
		if(taskType != "Test1" && taskType != "Test2"){
			//Modify the instruction displayed to the appropriate instruction 
			//of the given origami and step.
			if(origamiType == "Boat"){
				$('#instructionsDiv').text(boatInstructions[currentStep]);
			}
			else if(origamiType == "Swan"){
				$('#instructionsDiv').text(swanInstructions[currentStep]);
			}
		}
		else{
			$('#instructionsDiv').text("Test task: good luck!");
		}
		
		if(methodType == "Normal"){
			$('#instructionsDiv').text("Normal task: good luck!");
		}
		
		$('#instructionsDiv').css("color", "black");
		
		//Convert current step string into an int.
		var currentStepNum = parseInt(currentStep);
		//Modify the current Step to the next one.
		document.getElementById("currentStep").innerHTML = "STEP " + (currentStepNum + 1);
		
		//Change the color of the step cell.
		document.getElementById("stepname" + currentStep).style.backgroundColor = "lightgreen";
		
		if(document.getElementById("stepname" + (currentStepNum + 1)).style.backgroundColor == "lightgray"){
			$('#instructionsDiv').text("Done!");
			$('#instructionsDiv').css("color", "green");
			clearInterval(x);
			clearInterval(lapx);
		}
		else{
			clearInterval(lapx);
			lapstartTimer();		
		}
	
		if(currentStepNum > 1){

		}
	}
	//If last step is reached
	else{
		$('#instructionsDiv').text("Done!");
		$('#instructionsDiv').css("color", "green");
		
		
		//Stop timer
		clearInterval(x);
		clearInterval(lapx);
	}
});

$('#rewindStepBtn').on('click', function (e) {
	//Get current step.
	var currentStep = document.getElementById("currentStep").innerHTML.substring(5);
	
	if(document.getElementById("stepname" + currentStep).style.backgroundColor != "lightgray"){				
		var currentStepNum = parseInt(currentStep);
		//Reset the cell of the cell before current step to 0.
		document.getElementById("steptime" + (currentStepNum - 1)).innerHTML = "0:00:00";
		document.getElementById("lapsteptime" + (currentStepNum - 1)).innerHTML = "0:00:00";
		
		//Reset the color of the step cell.
		document.getElementById("stepname" + (currentStepNum - 1)).style.backgroundColor = "white";
		

		//modify the current Step to the one before it.
		if(currentStepNum > 1){
			document.getElementById("currentStep").innerHTML = "STEP " + (currentStepNum - 1);
		}
	}
	else{
		//No error handling, please don't press this ;(
	}
});



///////////////////////////////////////////////////////////
//Instructions Stuff 
///////////////////////////////////////////////////////////


var boatInstructions = [
	"Fold the paper in half from left to right.",
	"Unfold the paper.",
	"Fold the paper in half from top to bottom. (Do not unfold the paper)",
	"After folding the paper in half in Step 3, fold the top-left and top-right corners towards the center of the paper so that the two corners meet close to the center of the bottom of the paper.",
	"There will be two rectangular sections at the bottom of your paper (a flap). Fold the top layer of the flap upwards. Crease the flap.",
	"Turn the paper over.",
	"Fold the other flap upwards as well. Crease the flap.",
	"Open up the paper by pulling the two long sides of the bottom of the paper apart and collapsing it into a diamond shape.",
	"This diamond shape will have two layers. Fold the first layer from the bottom corner of the diamond to the top corner.",
	"Turn the paper over.",
	"Fold this layer from the bottom corner of the diamond to the top corner as well.",
	"Open up the paper by pulling the two long sides of the bottom of the paper apart and collapsing it into a diamond shape.",
	"This diamond will have two separated layers of paper to its left and right. Grab the two layers and pull them gently apart.",
	"Flatten the bottom part of the paper to shape the body of the boat.",
	"Open up the sides of the boat.",
];

var swanInstructions = [
	"Position the paper like a diamond.",
	"Fold the bottom-left and bottom-right sides of the diamond-oriented paper towards the center so that the sides meet. Crease the fold.",
	"Flip the paper over.",
	"Repeat step 2 and fold the left and right sides of the paper towards the center so that the sides meet. Crease the fold.",
	"Fold the bottom corner of the paper towards the top of the paper.",
	"Take the part of the paper you just folded and fold down a small section to form the beak of the swan.",
	"Flip the paper over.",
	"Fold the left side of the paper to the right. Crease the paper you folded. The swan's beak will stick out slightly.",
	"While holding the swan’s body down, only pull the head and neck up.",
	"Crease the base of the swan’s neck."
];
