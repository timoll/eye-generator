import bpy
import mathutils
import math

true=1
eyePosLeft = mathutils.Vector((-3.2,0,0))
eyePosRight = mathutils.Vector((3.2,0,0))
glassesPos = mathutils.Vector((0, 4.2, -1.2))
diameter=25
eyeScale=diameter/24

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
        scene.frame_step=4
        scene.render.resolution_y=1080
        scene.render.resolution_x=1920
    elif cam == 'eye':
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

leftEyeKey=[]
leftEyeKey.append([1, mathutils.Vector((-math.pi/2, 0, math.pi/12))])
leftEyeKey.append([31, mathutils.Vector((-math.pi/2, 0, -math.pi/12))])
leftEyeKey.append([61, mathutils.Vector((-math.pi/2+math.pi/12, 0, 0))])
leftEyeKey.append([91, mathutils.Vector((-math.pi/2-math.pi/12, 0, 0))])
leftEyeKey.append([121, mathutils.Vector((-math.pi/2, 0, 0))])

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

for keyFrame in leftEyeKey:
    cf = keyFrame[0]
    bpy.context.scene.frame_set(cf)
    leftEye.rotation_euler = keyFrame[1]
    leftEye.keyframe_insert(data_path='rotation_euler', frame=(cf))

for keyFrame in rightEyeKey:
    cf = keyFrame[0]
    bpy.context.scene.frame_set(cf)
    rightEye.rotation_euler = keyFrame[1]
    rightEye.keyframe_insert(data_path='rotation_euler', frame=(cf))

for keyFrame in glassesKey:
    cf =keyFrame[0]
    bpy.context.scene.frame_set(cf)
    glasses.rotation_euler = keyFrame[1]
    glasses.location = keyFrame[2]
    glasses.keyframe_insert(data_path='rotation_euler', frame=(cf))
    glasses.keyframe_insert(data_path='location', frame=(cf))

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
