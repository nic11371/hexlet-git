from algorithms_basics.Linked_lists.Linked_list import LinkedList


def get_linked_list_from_array(items):
    linked_list = LinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list
