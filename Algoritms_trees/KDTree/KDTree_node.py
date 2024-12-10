class KDTreeNode:
    def __init__(self, point, dimension, parent):
        self.point = point
        self.dimension = dimension
        self.parent = parent
        self.left = None
        self.right = None
