from tree_node import Trie


def build_trie(words):
    root = Trie(None)
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie(char)
            node = node.children[char]
        node.end = True
    return root
