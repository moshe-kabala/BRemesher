import bpy
# import random

from .. utils.test import clear_all, add_monky, test_map, add_cube, set_environment


TestVertexMapID = "view3d.test_bremesher_vertex_map"


class TestVertexMap(bpy.types.Operator):
    bl_idname = TestVertexMapID
    bl_label = "Simple operator"
    bl_description = "Test BRemesher vertex map"

    def execute(self, context):

        # first lets clean the schema
        clear_all()

        set_environment()

        # create some monky
        monk = add_monky()

        test_map(monk)

        box = add_cube((3, 0, 0))
        test_map(box)
        # saving to access from the commend line
        #bpy.monk = monk
        return {'FINISHED'}
