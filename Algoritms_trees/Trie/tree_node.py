class Trie:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.end = False
