from tree_node import BTreeNode


def buildBTree(data):
    root = BTreeNode(data['keys'])
    root.leaf = data['leaf']
    if not data['leaf']:
        for child in data["children"]:
            root.children.append(buildBTree(child))
    return root
