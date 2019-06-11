""" 
Key commands: 
    p   - Toggle plants 
    s   - Scale plants 
    m   - Toggle background music 
    v   - Toggle video 
""" 

import viz
import vizact
import vizshape

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.MainView.move([0,0,-1])

#Create skylight
viz.MainView.getHeadLight().disable()
sky_light = viz.addLight(euler=(0,90,0))
sky_light.position(0,0,-1,0)
sky_light.color(viz.WHITE)
sky_light.ambient([0.9,0.9,1])

#Add the gallery model
gallery = viz.addChild('gallery.osgb')

#Add audio
music = viz.addAudio('bach_air.mid',loop=1)

#Add video
video = viz.addVideo('vizard.mpg',play=1,loop=1)

#Get a handle to Starry Night texture
painting = gallery.getTexture('painting_starry-night')

#Add an avatar
avatar = viz.addAvatar('vcc_male2.cfg',pos=[0,0,1])
avatar.state(1)

#Create static drop shadow to avatar
shadow_texture = viz.addTexture('shadow.png')
shadow = vizshape.addQuad(parent=avatar,axis=vizshape.AXIS_Y)
shadow.texture(shadow_texture)
shadow.zoffset()

#Move avatar around the room with a sequence of walk, turn, and wait actions

#Create action to wait 5-10 seconds
RandomWait = vizact.waittime(vizact.randfloat(5,10))

#A list of painting locations
avatarMove = [[-3.7,2.2,300],[-3.7,6.5,270],[0,8,0],[3.7,6.5,90],[3.7,2.6,90],[3.7,1,130]]
actions = []
for loc in avatarMove:
    #Add an action to walk to the next painting, turn towards it, and wait a few seconds
    actions.append(vizact.method.playsound('footsteps.wav',viz.LOOP))
    actions.append(vizact.walkTo([loc[0],0,loc[1]],turnSpeed=250.0))
    actions.append(vizact.method.playsound('footsteps.wav',viz.STOP))
    actions.append(vizact.turn(loc[2],250.0))
    actions.append(RandomWait)

#Repeat the sequence of actions forever
avatar.addAction(vizact.sequence(actions,viz.FOREVER))

#Place a plant in each room corner.
plantPositions = [[-3.5,0,-0.3],[-4,0,7.9],[4,0,7.9],[3.5,0,-0.3]]
plants = []
plants_root = viz.addGroup()
plants_root.visible(False)
for position in plantPositions:
    plant = viz.addChild('plant.osgb',parent=plants_root,pos=position,cache=viz.CACHE_CLONE)
    plants.append(plant)
    shadow.clone(parent=plant)

# Ceiling pigeon is watching you admire art
pigeon = viz.addAvatar('pigeon.cfg',pos=(1,8.1,5.9),euler=(180,0,0))
pigeon.state(1)

#Define callback functions for key events

#Scale the plants
def scalePlants(val):
    for plant in plants:
        plant.setScale([val]*3)

#Register key events
vizact.onkeydown('p',plants_root.visible,viz.TOGGLE)
vizact.onkeydown('s',scalePlants,vizact.choice([1.2,0.8,1]))
vizact.onkeydown('m',vizact.choice([music.play,music.stop]))
vizact.onkeydown('v',gallery.texture,vizact.choice([video,painting]),'painting_starry-night')