import os
import sys
from algorithms_basics.Linked_lists.Linked_list import LinkedList
from algorithms_basics.Linked_lists.helpers import get_linked_list_from_array

sys.path.append(os.path.abspath('/usr/src/app/'))


def solution(lists):
    arr = []
    link = get_linked_list_from_array(lists)
    arr.append(link)
    linked_list = LinkedList()
    # linked_list = LinkedList()
    return arr


items = [[10, 20], 0, -1, ['hey']]

print(solution(items))  # [['hey'], -1, 0, [10, 20]]
solution([])  # []
