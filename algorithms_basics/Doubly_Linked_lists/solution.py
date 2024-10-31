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

    first = reverse.append(linked_list.head.value)
    first_next = linked_list.head.next
    if first_next.next is not None:
        second_next = first_next.next
    # third = second_next.value
    first.head.previous = first_next
    first.head.next = first_next.next
    first_next.next = first.head
    second = reverse.prepend(first_next.value)
    first_next.previous = None

    return reverse.to_array()

items = [[1, 2], [3, [4, 5]], 1, 6, 7]
items2 = [1, 2, 3, 4, 5]
items3 = [[1, None], [3, [4, 5]]]
items4 = [1, 2, 1, 1, 1, 2]

print(solution(items))  # [[3, [4, 5]], [1, 2], 1, 6, 7]
print(solution(items2)) # [2, 1, 3, 4, 5]
print(solution(items3)) # [[3, [4, 5]], [1, None]]
print(solution(items4)) # [2, 1, 1, 1, 1, 2]
print(solution([]))  # []
