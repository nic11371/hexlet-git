class BTreeNode:
    def __init__(self, keys):
        self.leaf = False
        self.keys = keys
        self.children = []
