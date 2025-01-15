class Node:
    def __init__(self, value, node=None):
        self.next = node
        self.value = value

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __repr__(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc))


def reverse(head, tail=None):
    if not head:
        return None
    while head:
        head.next, tail, head = tail, head, head.next
    return tail


def reverse_two(linked_list):
    reverse = None
    current = linked_list

    while current:
        reverse = Node(current.get_value(), reverse)
        current = current.get_next()
    return reverse


numbers = Node(1, Node(2, Node(3)))  # (1, 2, 3)
reversed_numbers = reverse(numbers)  # (3, 2, 1)
print(reversed_numbers)
