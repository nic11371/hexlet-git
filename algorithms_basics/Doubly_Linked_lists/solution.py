import os
import sys
from algorithms_basics.Doubly_Linked_lists.Double_Linked_list import DoubleLinkedList
from algorithms_basics.Doubly_Linked_lists.helpers import get_double_linked_list_from_array

sys.path.append(os.path.abspath('/usr/src/app/'))


def solution(arr):
    linked_list = get_double_linked_list_from_array(arr)
    reverse = DoubleLinkedList()

    if not linked_list.head:
        return reverse.to_array()

    reverse.prepend(linked_list.head.value)
    next_node = linked_list.head.next

    while next_node:
        reverse.prepend(next_node.value)
        next_node = next_node.next

    return reverse.to_array()

items = [[10, 20], 0, -1, ['hey']]

print(solution(items))  # [0, [10, 20], -1, ['hey']]
print(solution([]))  # []
