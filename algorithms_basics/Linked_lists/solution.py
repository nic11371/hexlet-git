import os
import sys
from algorithms_basics.Linked_lists.Linked_list import LinkedList
from algorithms_basics.Linked_lists.helpers import get_linked_list_from_array

sys.path.append(os.path.abspath('/usr/src/app/'))


def solution(arr):
    linked_list = get_linked_list_from_array(arr)
    reverse = LinkedList()

    if not linked_list.head:
        return reverse.to_array()

    reverse.prepend(linked_list.head.value)
    next_node = linked_list.head.next

    while next_node:
        reverse.prepend(next_node.value)
        next_node = next_node.next

    return reverse.to_array()

items = [[10, 20], 0, -1, ['hey']]

print(solution(items))  # [['hey'], -1, 0, [10, 20]]
print(solution([]))  # []
