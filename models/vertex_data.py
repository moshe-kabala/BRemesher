class VertexData:
    """
    VertexData contain the important data such as density, is_last and direction
    """

    __slots__ = ("density", "is_last")

    def __init__(self, density=0, is_border=False):
        self.density = density
        self.is_last = is_border
