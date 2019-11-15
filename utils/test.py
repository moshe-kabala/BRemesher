import bpy
import bmesh

from .. utils.applay_map import applay_map
from .. algorithms.map_vertex import map_vertex_by_face

# task
# show the vertex color


VERTEX_COLOR_MAT_NAME = "VERTEX_COLOR_MAT_NAME"


def clear_all():
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_all()
    bpy.ops.object.delete(use_global=False, confirm=False)


def set_environment():
    """
    this function create material and change the mode of the view
    """

    # bpy.data.screens["Scripting"].shading.type = 'MATERIAL'
    # create material

    pass


def get_vertex_mat():
    mat = bpy.data.materials.get("VERTEX_COLOR_MAT_NAME")
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name=VERTEX_COLOR_MAT_NAME)
        mat.use_nodes = True
        matnodes = mat.node_tree.nodes
        # new attribute
        node = matnodes.new('ShaderNodeAttribute')
        node.attribute_name = "Col"

        # assign texture to material's displacement
        disp = matnodes['Material Output'].inputs[0]
        mat.node_tree.links.new(disp, node.outputs[0])

    return mat


def assign_mat(obj, mat):
     # Assign it to object
    if obj.data.materials:
        # assign to 1st material slot
        obj.data.materials[0] = mat
    else:
        # no slots
        obj.data.materials.append(mat)


def preper_obj(obj, save_edges=False, smooth=0):
    obj.modifiers.new(name="sub", type='SUBSURF')
    obj.modifiers["sub"].levels = 3
    if save_edges:
        obj.modifiers["sub"].subdivision_type = 'SIMPLE'

    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="sub")
    bpy.ops.sculpt.sculptmode_toggle()
    bpy.ops.sculpt.dynamic_topology_toggle()
    bpy.ops.sculpt.optimize()
    bpy.ops.sculpt.sculptmode_toggle()

    if True:
        bpy.ops.object.shade_smooth()
    else:
        bpy.ops.object.shade_flat()

    # assgin the material that created in set_environment function
    # Get material
    mat = get_vertex_mat()
    assign_mat(obj, mat)

    return obj


def add_monky(location=(0, 0, 0)):
    bpy.ops.mesh.primitive_monkey_add(
        size=2, enter_editmode=False, location=location)
    monk = bpy.context.object
    preper_obj(monk)
    return monk


def add_cube(location=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(
        size=2, enter_editmode=False, location=location)
    cube = bpy.context.object
    preper_obj(cube, True)
    return cube


def test_map(obj):
    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(obj.data)   # fill it in from a Mesh

    # mappin each vertex
    map_data,  min, max = map_vertex_by_face(bm)
    # add the map
    applay_map(obj, map_data,  min, max)
    bm.free()
