class RBTreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent,
        self.is_red = False
