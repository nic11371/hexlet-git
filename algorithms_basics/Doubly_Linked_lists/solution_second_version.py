import os
import sys

sys.path.append(os.path.abspath('/usr/src/app/'))

from double_linked_list.DoubleLinkedListNode import DoubleLinkedListNode  # noqa: E402, E501
from helpers.helper import get_double_linked_list  # noqa: E402


def solution(items):
    double_linked_list = get_double_linked_list(items)

    if double_linked_list.tail == double_linked_list.head:
        return double_linked_list.to_array()

    head = double_linked_list.head
    head_next = head.next
    new_head = DoubleLinkedListNode(head_next.value, head, None)
    new_second_node = DoubleLinkedListNode(head.value, head_next.next, new_head)

    double_linked_list.head = new_head
    double_linked_list.head.next = new_second_node

    if double_linked_list.tail != head_next:
        third_node = head_next.next
        third_node.previous = new_second_node

    return double_linked_list.to_array()

items = [[1, 2], [3, [4, 5]], 1, 6, 7]
items2 = [1, 2, 3, 4, 5]
items3 = [[1, None], [3, [4, 5]]]
items4 = [1, 2, 1, 1, 1, 2]

print(solution(items))  # [[3, [4, 5]], [1, 2], 1, 6, 7]
print(solution(items2)) # [2, 1, 3, 4, 5]
print(solution(items3)) # [[3, [4, 5]], [1, None]]
print(solution(items4)) # [2, 1, 1, 1, 1, 2]
print(solution([]))  # []