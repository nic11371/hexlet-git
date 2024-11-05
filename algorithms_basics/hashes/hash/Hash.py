from algorithms_basics.hashes.lists.LinkedList import LinkedList


class Hash:
    def __init__(self):
        self.table = []
        self.count = 0

    def hash(self, s):
        k = 65537
        m = 2**20

        result = 0
        power = 0
        for i in range(len(s)):
            result = (result + power * ord(s[i])) % m
            power = (power * k) % m

        return result

    def calculate_index(self, table, key):
        try:
            return self.hash(str(key)) % len(table)
        except ZeroDivisionError:
            return self.hash(str(key))

    def rebuild_table_if_need(self):
        if len(self.table) == 0:
            self.table = [None for _ in range(128)]
        else:
            load_factor = self.count / len(self.table)

            if load_factor >= 0.8:
                new_table = [None for _ in range(len(self.table) * 2)]
                for list_ in self.table:
                    for pair in list_:
                        new_index = self.calculate_index(new_table, pair['key'])
                        if new_table[new_index] is None:
                            new_table[new_index] = LinkedList()

                        new_table[new_index].append(pair)

                self.table = new_table

    def set(self, key, value):
        self.rebuild_table_if_need()

        index = self.calculate_index(self.table, key)
        if self.table[index] is None:
            self.table[index] = LinkedList()

        self.table[index].append(
            {'key': key, 'value': value}
        )
        self.count += 1

    def get(self, key):
        index = self.calculate_index(self.table, key)
        if self.table[index] is None:
            return None

        for pair in self.table[index]:
            if pair['key'] == key:
                return pair['value']

        return None
