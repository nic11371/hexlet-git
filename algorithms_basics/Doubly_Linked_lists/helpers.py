from algorithms_basics.Doubly_Linked_lists.Double_Linked_list import DoubleLinkedList


def get_double_linked_list_from_array(items):
    linked_list = DoubleLinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list
