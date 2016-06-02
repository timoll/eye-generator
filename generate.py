import bpy
import mathutils
import math
import json
import sys
import argparse

argv = sys.argv
try:
     index = argv.index("--") + 1
except ValueError:
     index = len(argv)

print(argv)
argv = argv[index:]
print(argv)
parser = argparse.ArgumentParser(description='Generate Eye Animation')
parser.add_argument("jsonFile", help="Json-File with information about animation")
args=parser.parse_args(argv)
jsonData=open(args.jsonFile)
data = json.load(jsonData)
print(data["Eye Position Left"])

true=1
eyePosLeft = mathutils.Vector(data["Eye Position Left"])
eyePosRight = mathutils.Vector(data["Eye Position Right"])
glassesPos = mathutils.Vector((0, 4, -1.2))
diameter=data["Diameter"]
eyeScale=diameter/24
lastFrame=data["Last Frame"]

leftEye = bpy.data.objects['complexEyeGullstrandLeft']
rightEye = bpy.data.objects['complexEyeGullstrandRight']
glasses = bpy.data.objects['glasses']
leftDownCam = bpy.data.objects['LeftDown']
leftUpCam = bpy.data.objects['LeftUp']
rightDownCam = bpy.data.objects['RightDown']
rightUpCam = bpy.data.objects['RightUp']
sceneCam = bpy.data.objects['Scene']

def setCam( cam ):
    scene=bpy.data.scenes['Scene']
    if cam == 'scene':
        bpy.data.lamps['Sun'].node_tree.nodes['Emission'].inputs[1].default_value=0.5
        scene.frame_step=4
        scene.render.resolution_y=1080
        scene.render.resolution_x=1920
    elif cam == 'eye':
        bpy.data.lamps['Sun'].node_tree.nodes['Emission'].inputs[1].default_value=5
        scene.frame_step=1
        scene.render.resolution_y=240
        scene.render.resolution_x=320
    return


leftEye.scale = (eyeScale, eyeScale, eyeScale)
rightEye.scale = (eyeScale, eyeScale, eyeScale)

locLeft = leftEye.location
locRight = rightEye.location
rotLeft = leftEye.rotation_euler
rotRight = rightEye.rotation_euler

leftEye.location = eyePosLeft
rightEye.location = eyePosRight

rightEyeKey=[]
rightEyeKey.append([1, mathutils.Vector((-math.pi/2, 0, math.pi/12))])
rightEyeKey.append([31, mathutils.Vector((-math.pi/2, 0, -math.pi/12))])
rightEyeKey.append([61, mathutils.Vector((-math.pi/2+math.pi/12, 0, 0))])
rightEyeKey.append([91, mathutils.Vector((-math.pi/2-math.pi/12, 0, 0))])
rightEyeKey.append([121, mathutils.Vector((-math.pi/2, 0, 0))])

glassesKey=[]
glassesKey.append([1, mathutils.Vector((math.pi/2, 0, 0)), glassesPos + mathutils.Vector((0,0,0))])
glassesKey.append([31, mathutils.Vector((math.pi/2, math.pi/36, 0)), glassesPos + mathutils.Vector((0,0,0.5))])
glassesKey.append([61, mathutils.Vector((math.pi/2+math.pi/36, 0, 0)), glassesPos + mathutils.Vector((0,0,1))])
glassesKey.append([91, mathutils.Vector((math.pi/2, -math.pi/36, 0)), glassesPos + mathutils.Vector((0,0,0))])
glassesKey.append([121, mathutils.Vector((math.pi/2, 0, 0)), glassesPos + mathutils.Vector((0,0,0))])

factor=math.pi/180

for keyFrame in data["Left Eye Keyframes"]:
    cf = keyFrame["Frame"]
    bpy.context.scene.frame_set(cf)
    leftEye.rotation_euler = [x*factor for x in keyFrame["Rotation"]]
    leftEye.keyframe_insert(data_path='rotation_euler', frame=(cf))

for keyFrame in data["Right Eye Keyframes"]:
    cf = keyFrame["Frame"]
    bpy.context.scene.frame_set(cf)
    rightEye.rotation_euler = [x*factor for x in keyFrame["Rotation"]]
    rightEye.keyframe_insert(data_path='rotation_euler', frame=(cf))

for keyFrame in data["Glasses Keyframes"]:
    cf = keyFrame["Frame"]
    bpy.context.scene.frame_set(cf)
    glasses.rotation_euler = [x*factor for x in keyFrame["Rotation"]]
    glasses.location = glassesPos + mathutils.Vector(keyFrame["Position"])
    glasses.keyframe_insert(data_path='rotation_euler', frame=(cf))
    glasses.keyframe_insert(data_path='location', frame=(cf))

bpy.data.scenes['Scene'].frame_end = lastFrame
setCam('eye')
bpy.context.scene.camera = rightUpCam
bpy.data.scenes['Scene'].render.filepath ='//rightup/'
bpy.ops.wm.save_as_mainfile(copy=true, filepath='rightUp.blend')

bpy.context.scene.camera = rightDownCam
bpy.data.scenes['Scene'].render.filepath ='//rightdown/'
bpy.ops.wm.save_as_mainfile(copy=true, filepath='rightDown.blend')

bpy.context.scene.camera = leftUpCam
bpy.data.scenes['Scene'].render.filepath ='//leftup/'
bpy.ops.wm.save_as_mainfile(copy=true, filepath='leftUp.blend')

bpy.context.scene.camera = leftDownCam
bpy.data.scenes['Scene'].render.filepath ='//leftdown/'
bpy.ops.wm.save_as_mainfile(copy=true, filepath='leftDown.blend')

setCam('scene')
bpy.context.scene.camera = sceneCam
bpy.data.scenes['Scene'].render.filepath ='//scene/'
bpy.ops.wm.save_as_mainfile(copy=true, filepath='scene.blend')
