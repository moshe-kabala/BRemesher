import bpy
from .. utils.test import test_map, assign_mat, get_vertex_mat

TestMapActiveID = "view3d.bremesher_test_map_on_active"


class TestMapActive(bpy.types.Operator):
    bl_idname = TestMapActiveID
    bl_label = "test_map_on_active"
    bl_description = "test map on an active object"

    def execute(self, context):
        obj = bpy.context.active_object
        if obj is None:
            self.report({'INFO'}, "Please select any object")
        else:
            self.report({'INFO'}, "Processing ...")
            mat = get_vertex_mat()
            assign_mat(obj, mat)
            test_map(obj)
            self.report({'INFO'}, "Done")

        return {'FINISHED'}
