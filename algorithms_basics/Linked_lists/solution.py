import os
import sys
from algorithms_basics.Linked_lists.Linked_list import LinkedList
from algorithms_basics.Linked_lists.helpers import get_linked_list_from_array

sys.path.append(os.path.abspath('/usr/src/app/'))


def solution(arr):
    linked_list = get_linked_list_from_array(arr)
    head = linked_list.head
    tail = linked_list.tail
    while head:
        linked_list.prepend(head.next)
    reverse = LinkedList.to_array(linked_list)
    return reverse


items = [[10, 20], 0, -1, ['hey']]

print(solution(items))  # [['hey'], -1, 0, [10, 20]]
# solution([])  # []
