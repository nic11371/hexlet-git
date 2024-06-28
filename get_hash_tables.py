class HashTable(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None

    def set(self, key, value):
        index = get_hash(key)
        self[index] = [key, value]


def make_table():
    return HashTable()


def get_hash(key):
    return sum(ord(ch) for ch in key) % 10 + 1


# BEGIN (write your solution here)
def get_or_default(table, key, default):
    hash = get_hash(key)
    if table[hash] is None:
        return default
    return table[hash][1]
# END


# hash_table = make_table()
# # метод set(ключ, значение) записывает значение по ключу в мапу
# hash_table.set("g", "bar")
# hash_table.set("e", "foo")

# print(get_or_default(hash_table, "g", "python"))  # bar
# print(get_or_default(hash_table, "a", "python"))  # python

table = make_table()
table.set("e", "hello")
table.set("k", "world")
table.set("m", "python")
print(get_or_default(table, "e", "bar"))
print(get_or_default(table, "k", "k"))
print(get_or_default(table, "f", "foo"))
