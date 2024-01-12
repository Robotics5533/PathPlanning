import bpy
import json
import os

obj = bpy.context.object
file_name = obj.name_full
filepath = "C:\\Users\\Electric Horsepower\\Desktop"
keyframes = []
seperate = os.seperator
unit = 1000

def grab_data(s):
    scene = bpy.context.scene
    
    keyframe = {
        "frame_time": scene.frame_float,
        "position": {
            "x": obj.location.x,
            "y": obj.location.y,
            "z": obj.location.z,
            
        },
    }
    print(keyframe)
    keyframes.append(keyframe)
    if scene.frame_float == scene.frame_end:
        with open(os.path.join(filepath, filename), "w") as json_out:
            json.dump({"keyframes":keyframes,"unit":unit}, json_out)






bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(grab_data)
