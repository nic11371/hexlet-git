class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)

    def _storage(self):
        _attr_instance = self.get_attribute('tag')
        _collection = _attr_instance.split()
        return _collection

    def __str__(self, data):
        new_string = " ".join(data)
        self.attributes['tag'] = new_string

    def add_tag(self, tag_name):
        storage = self._storage()
        if tag_name not in storage:
            storage.append(tag_name)
        self.__str__(storage)

    def remove_tag(self, tag_name):
        storage = self._storage()
        if tag_name in storage:
            storage.remove(tag_name)
        self.__str__(storage)

    def toggle_tag(self, tag_name):
        storage = self._storage()
        if tag_name in storage:
            self.remove_tag(tag_name)
            return
        self.add_tag(tag_name)
        return
    # END


div = HTMLElement({'tag': 'one two'})
print(div.get_attribute('tag'))

div.add_tag('small')
print(div.get_attribute('tag'))

div.add_tag('small')
print(div.get_attribute('tag'))

div.remove_tag('two')
print(div.get_attribute('tag'))

div.toggle_tag('small')
print(div.get_attribute('tag'))

div.toggle_tag('small')
print(div.get_attribute('tag'))
