from .. utils.make_interpolater import make_interpolater


def applay_map(obj, d, min, max):
    mesh = obj.data

    m = make_interpolater(min, max, 0, 1)

    # check if our mesh already has Vertex Colors, and if not add some... (first we need to make sure it's the active object)
    #obj.select = True
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()

    i = 0
    # for each polygon config its vertex color by d (map)
    max, min = 0, 0

    for poly in mesh.polygons:
        for _, index in enumerate(poly.vertices):
            c = 1-m(d[index])
            vcol_layer.data[i].color = (c, 0, 0, 1)
            i += 1
            if c > max:
                max = c
            if c < min:
                min = c

    # for debuggin check the color
    print(f'max {max} min {min}')
