from tree_node import RBTreeNode


def build_RBTree(data):
    root = RBTreeNode(data['value'])
    root.is_red = data['isRed']
    if 'left' in data and data['left']:
        root.left = build_RBTree(data['left'])
        root.left.parent = root
    if 'right' in data and data['right']:
        root.right = build_RBTree(data['right'])
        root.right.parent = root
    return root
