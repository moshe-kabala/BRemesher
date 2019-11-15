def map_vertex_by_face(bm):
    """
    map_vertex map each vertex by compering its paces normals 
    """
    d = {}
    count = 0
    max = 0
    min = 0
    for v in bm.verts:
        count = 0
        i = 0
        for f in v.link_faces:
            r = f.normal - v.normal
            count += abs(r.x) + abs(r.y) + abs(r.z)
            i += 1
            # print some info
            #print("%d -> %d via edge %d" % (v.index, v_other.index, e.index))
        if i > 0:
            count /= i
        d[v.index] = count
        # saving the max and min values
        if count > max:
            max = count
        if count < min:
            min = count
    return d, max, min
