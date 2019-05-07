"""
This module was generated by Vizconnect.
Version: 1.01
Generated on: 2015-10-01 17:51:54.203000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()
	
	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: initialize a new display
	_name = 'zsight_60'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: set the fullscreen monitor
			viz.window.setFullscreenMonitor(0)
			viz.window.setFullscreen(True)
			
			#VC: set some parameters
			Hofs = [0,0]
			Vofs = [0,0]
			Rofs = [0,0]
			VerticalSpan = False
			
			#VC: create the raw object
			import sensics
			sensics.zSight_60(stereo=[viz.STEREO_HORZ,viz.STEREO_VERT][VerticalSpan], leftHorizontalShift=Hofs[0], rightHorizontalShift=Hofs[1], leftVerticalShift=Vofs[0], rightVerticalShift=Vofs[1], leftRollShift=Rofs[0], rightRollShift=Rofs[1], window=_window)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Sensics', model='zSight 60')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('optical_heading'))

	#VC: set the name of the default
	vizconnect.setDefault('display', 'zsight_60')

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'ppt_rhead'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = 'localhost'
			markerId = 1
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')

	#VC: initialize a new tracker
	_name = 'ppt_lhead'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = 'localhost'
			markerId = 2
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')

	#VC: initialize a new tracker
	_name = 'ppt_rhand'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = 'localhost'
			markerId = 4
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')

	#VC: initialize a new tracker
	_name = 'ppt_lhand'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = 'localhost'
			markerId = 5
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')

	#VC: initialize a new tracker
	_name = 'osv3_sensor_bus'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			port = 11
			sensorIndex = 0
			
			#VC: create the raw object
			InertialLabs = viz.add('InertialLabs.dle')
			sensors = InertialLabs.addSensorBus(port=port)
			try:
				sensor = sensors[sensorIndex]
			except:
				viz.logWarn("** WARNING: can't connect to InertialLabs OSv3 (Sensor Bus) on port {0} with index {1}. It's likely that not enough sensors are connected.".format(port, sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Inertial Labs', model='OSv3 Sensor Bus')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: reset orientation
			_link.preEuler([0, 0, 0], target=viz.LINK_ORI_OP, priority=-20)
			
			#VC: apply offsets
			_link.preEuler([90, 0, 180])

	#VC: initialize a new tracker
	_name = 'optical_heading'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['ppt_lhead'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['ppt_rhead'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['osv3_sensor_bus'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			leftPosTracker = vizconnect.getTracker('ppt_lhead').getNode3d()
			rightPosTracker = vizconnect.getTracker('ppt_rhead').getNode3d()
			oriTracker = vizconnect.getTracker('osv3_sensor_bus').getNode3d()
			distance = 0.39
			
			#VC: create the raw object
			from vizconnect.util.virtual_trackers import OpticalHeading
			rawTracker[_name] = OpticalHeading(leftPosTracker, rightPosTracker, oriTracker, distance=distance)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Optical Heading')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: reset orientation
			_link.preEuler([0, 0, 0], target=viz.LINK_ORI_OP, priority=-20)
			
			#VC: apply offsets
			_link.preTrans([0, -0.14, 0.05])

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'joystick'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			import vizjoy
			rawInput[_name] = vizjoy.add()
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Joystick')
	
		#VC: init the mappings for the wrapper
		if initFlag&vizconnect.INIT_WRAPPER_MAPPINGS:
			#VC: on-state mappings
			if initFlag&vizconnect.INIT_MAPPINGS_ON_STATE:
				vizconnect.getInput(_name).setOnStateEventList([
						vizconnect.onstate(lambda rawInput: rawInput['joystick'].isButtonDown(1), vizconnect.getInput(_name).setMode),# make=Generic, model=Joystick, name=joystick, signal=Button 1
				])

	#VC: set the name of the default
	vizconnect.setDefault('input', 'joystick')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()
	
	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()
	
	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()

	#VC: initialize a new tool
	_name = 'grabber'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.display.stencil',1)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = False
			highlightMode = tools.highlighter.MODE_OUTLINE
			placementMode = tools.placer.MODE_MID_AIR
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				#def update(tool):
					#if rawInput['joystick'].isInMode('super') and rawInput['joystick'].isButtonDown(4):# make=Generic, model=Joystick, name=joystick, signal=Button 4
						#tool.grab()
				#rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getTracker('ppt_rhand'))

	#VC: initialize a new tool
	_name = 'grabber2'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.display.stencil',1)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = True
			highlightMode = tools.highlighter.MODE_OUTLINE
			placementMode = tools.placer.MODE_MID_AIR
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')

	#VC: set the name of the default
	vizconnect.setDefault('tool', 'grabber')

	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()
	
	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_STARTUP)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')


