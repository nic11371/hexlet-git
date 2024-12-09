from fixtures.tree2 import words as data


class TrieNode:

    def __init__(self, text=''):
        '''
        Initializes a TrieNode with the given string and an initially
        empty dictionary mapping strings to TrieNodes.
        '''
        self.text = text
        self.children = dict()
        self.is_word = False

    def __str__(self):
        return '{} -> {}'.format(self.text, self.children)


class PrefixTree:
    def __init__(self, root):
        self.root = root

    def display(self):
        '''
        Prints the contents of this prefix tree.
        '''
        print('======================================================')
        self.__displayHelper(self.root)
        print('======================================================\n')

    def __displayHelper(self, current):
        '''
        Private helper for printing the contents of this prefix tree.
        '''
        print(current)
        for letter in current.children:
            self.__displayHelper(current.children[letter])

    def insert(self, word):
        '''
        Inserts the given word into this prefix tree.
        '''
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

    def find(self, word):
        '''
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        '''
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        if current.is_word: return current

    def __child_words_for(self, node, words):
        '''
        Private helper function. Cycles through all children
        of node recursively, adding them to words if they
        constitute whole words (as opposed to merely prefixes).
        See starts_with for usage.
        '''
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        '''
    def starts_with(self, prefix):
        found_words = []
        prefix_list = []

        def walk(node, word_list=None):
            if node.is_word:
                found_words.append(''.join(word_list + [node.text]))
            for w in node.children:
                walk(node.children[w],  word_list + [node.text])

        for char in prefix:
            if char not in self.root.children:
                return []
            self.root = self.root.children[char]
            prefix_list.append(self.root.text)
        walk(self.root, prefix_list[:-1])

        return sorted(found_words)


def build_trie(words):
    root = TrieNode(None)
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_word = True
    return root


def solution(words, prefix):
    tree = build_trie(words)
    root = PrefixTree(tree)
    return root.starts_with(prefix)


print(solution(data, 'appre'))
