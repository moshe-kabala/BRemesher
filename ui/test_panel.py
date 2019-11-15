import bpy
from .. ops.test_setup_map import TestVertexMapID
from .. ops.test_map_on_active import TestMapActiveID

TestPanelID = "Test_BRemsher_panel"


class TestPanel(bpy.types.Panel):
    """
     panel for testing the BRemsher addon
    """
    bl_idname = TestPanelID
    bl_category = "Test Panel"
    bl_label = "Test Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator(TestVertexMapID, text="Test Map")
        row.operator(TestMapActiveID, text="Test Map on Selected")
