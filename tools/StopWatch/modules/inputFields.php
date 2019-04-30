<div class="input-group">
  <select class="custom-select" id="origamiTypeInput">
	<option selected value="None">Select Origami</option>
	<option value="Boat">Boat</option>
	<option value="Swan">Swan</option>
  </select>
  <div class="input-group-append">
	<button type="button" class="btn btn-dark" id="startTimerBtn">Start</button>
  </div>
</div>
<br>
<div class="input-group">
  <select class="custom-select" id="methodTypeInput">
	<option selected value="None">Select Method</option>
	<option value="Normal">Normal</option>
	<option value="Augmented">Augmented</option>
  </select>
  <select class="custom-select" id="taskTypeInput">
	<option selected value="None">Select Task</option>
	<option value="First1">First Task (Origami 1)</option>
	<option value="Second1">Second Task (Origami 1)</option>
	<option value="Third1">Third Task (Origami 1)</option>
	<option value="Test1">Test (Origami 1)</option>
	<option value="" disabled>-------------------------------</option>
	<option value="First2">First Task (Origami 2)</option>
	<option value="Second2">Second Task (Origami 2)</option>
	<option value="Third2">Third Task (Origami 2)</option>
	<option value="Test1">Test (Origami 2)</option>
	<option value="" disabled>-------------------------------</option>
  </select>
  <div class="input-group-append">
  <div class="input-group mb-3">
	  <div class="input-group-prepend">
		<span class="input-group-text" id="inputGroup-sizing-default">Participant ID:</span>
	  </div>
	  <input id="participantID" type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default"></input>
	</div>
  </div>
  
</div>
<br>

<div class="input-group">
  <select class="custom-select" id="incompleteInput">
	<option selected value="None">If Incomplete...</option>
	<option value="finishedStep1">Finished at Step 1</option>
	<option value="finishedStep2">Finished at Step 2</option>
	<option value="finishedStep3">Finished at Step 3</option>
	<option value="finishedStep4">Finished at Step 4</option>
	<option value="finishedStep5">Finished at Step 5</option>
	<option value="finishedStep6">Finished at Step 6</option>
	<option value="finishedStep7">Finished at Step 7</option>
	<option value="finishedStep8">Finished at Step 8</option>
	<option value="finishedStep9">Finished at Step 9</option>
	<option value="finishedStep10">Finished at Step 10</option>
	<option value="finishedStep11">Finished at Step 11</option>
	<option value="finishedStep12">Finished at Step 12</option>
	<option value="finishedStep13">Finished at Step 13</option>
	<option value="finishedStep14">Finished at Step 14</option>
	<option value="finishedStep15">Finished at Step 15</option>
  </select>
  <div class="input-group-append">
  <div class="input-group mb-3">
	  <div class="input-group-prepend">
		<span class="input-group-text" id="inputGroup-sizing-default">Skipped Steps:</span>
	  </div>
	  <input id="skippedStepsInput" type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default"></input>
	</div>
  </div>
</div>