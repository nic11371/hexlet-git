import os
import sys
from helpers import build_trie
from fixtures.tree2 import words as data

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_words(root, prefix):
    found_words = []
    prefix_list = []

    def walk(node, word_list=None):
        if node.end:
            found_words.append(''.join(word_list + [node.key]))
        for w in node.children:
            walk(node.children[w],  word_list + [node.key])

    for char in prefix:
        if char not in root.children:
            return []
        root = root.children[char]
    walk(root, prefix_list)

    return found_words


def solution(words, prefix):
    tree = build_trie(words)
    return find_words(tree, prefix)


print(solution(data, 'appre'))

# END


    # def walk(node, word_list=None):
    #     if word_list is None or word_list == []:
    #         word_list = prefix_list + []
    #     word_list.append(node.key)
    #     if node.end:
    #         found_words.append(''.join(word_list))
    #         word_list.clear()
    #     for w in node.children:
    #         walk(node.children[w], word_list)
    
        # walk(root)

# def find_words(root, prefix):
#     found_words = []
#     prefix_list = []

#     def walk(node, word_list=None):
#         if word_list is None or word_list == []:
#             word_list = prefix_list + []
#         word_list.append(node.key)
#         if node.end:
#             found_words.append(''.join(word_list))
#             word_list.clear()
#         for w in node.children:
#             walk(node.children[w], word_list)

#     for char in prefix:
#         if char not in root.children:
#             return []
#         root = root.children[char]
#         prefix_list.append(root.key)
#     walk(root)

#     return found_words
