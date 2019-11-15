import math


class TailContainer:
    __slots__ = ["matrix", "min", "max", "x_length",
                 "y_length", "z_length", "origin_offset"]

    def __init__(self, min, max, x_length, y_length, z_length, origin_offset):
        min
        self.max = max
        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length

        self.origin_offset = origin_offset
        self.matrix = [[[None] * math.ceil(z_length / min)]*math.ceil(y_length / min)]math.ceil(x_length / min)

    def get_tail_idx(self, v):
        return v.x - v.x % self.min, v.y - v.y % self.min, v.y - v.z % self.min

    def insert_polys(polys):
        seen_vertex = {}
        for p in polys:
            for 

    def get_tail(self, v):
        x, y, z = self.get_tail_idx
        tail = self.matrix[x][y][z]
        if tail is None:
            tail = Tail()
            self.matrix[x][y][z] = tail
        return tail
