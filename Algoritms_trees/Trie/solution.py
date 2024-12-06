import os
import sys
from helpers import build_trie
from fixtures.tree2 import words as data

sys.path.append(os.path.abspath('/usr/src/app/'))


# BEGIN (write your solution here)
def find_words(root, prefix, prefix_list=None, found_words=None):
    if prefix_list is None:
        prefix_list = []
    if found_words is None:
        found_words = []
    if root.key is not None:
        prefix_list.append(root.key)
    for char_prefix in prefix:
        if char_prefix not in root.children:
            return []
        root = root.children[char_prefix]
        prefix_list.append(root.key)

    d_2 = copy.deepcopy(d)
    for key in root.children:
        find_words(root.children[key], prefix, prefix_list)

    return prefix_list


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
