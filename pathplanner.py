import bpy

obj = bpy.context.object

keyframes = []


def grab_data(scene):
    keyframe = {
        "frame_time": bpy.context.scene.frame_float,
        "unit": 1000,
        "position": {
            "x": obj.location.x,
            "y": obj.location.y,
            "z": obj.location.z,
        },
    }

    keyframes.append(keyframe)


bpy.app.handlers.frame_change_post.append(grab_data)
