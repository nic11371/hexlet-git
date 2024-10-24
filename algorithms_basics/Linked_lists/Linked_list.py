from algorithms_basics.Linked_lists.Linked_node import LinkedListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        # Делаем новый узел головой
        new_node = LinkedListNode(value, self.head)
        self.head = new_node

        # Если нет хвоста, этот узел будет и хвостом
        if not self.tail:
            self.tail = new_node

        return self

    def append(self, value):
        new_node = LinkedListNode(value)

        # Если нет головы, этот узел будет головой
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self

        # Присоеденяем новый узел к концу, делаем его хвостом
        self.tail.next = new_node
        self.tail = new_node

        return self

    def delete(self, value):  # noqa: C901
        if not self.head:
            return None

        deleted_node = None
        # Проверяем с головы какие ноды надо удалять
        while self.head and self.head.value == value:
            deleted_node = self.head
            self.head = self.head.next

        current_node = self.head

        # Если у головы не нашли, проверяем остальные значения в списке
        if current_node is not None:
            while current_node.next:
                if current_node.next.value == value:
                    deleted_node = current_node.next
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next

        # Проверяем хвост
        if self.tail.value == value:
            self.tail == current_node

        return deleted_node

    def find(self, value):
        if not self.head:
            return None

        current_node = self.head

        # Перебираем список с головы, первое найденное значение возвращаем
        while current_node:
            if current_node.value is not None and current_node.value == value:
                return current_node

            # Делаем текущей следующий элемент списка
            current_node = current_node.next

        return None

    def is_empty(self):
        return self.head is None and self.tail is None

    def to_array(self):
        result = []
        if self.head is None:
            return result
        current_node = self.head
        while current_node:
            if current_node.value is not None:
                result.append(current_node.value)
            current_node = current_node.next
        return result
