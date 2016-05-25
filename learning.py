import bpy
import mathutils
import math

true=1
eyePosLeft = mathutils.Vector((-3.2,0,0))
eyePosRight = mathutils.Vector((3.2,0,0))
diameter=25
eyeScale=diameter/24

leftEye = bpy.data.objects["complexEyeGullstrandLeft"]
rightEye = bpy.data.objects["complexEyeGullstrandRight"]

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

bpy.ops.wm.save_as_mainfile(copy=true, filepath="shiftLeftEye.blend")
