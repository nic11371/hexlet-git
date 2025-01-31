from abc import ABC, abstractmethod


class HTMLElement(ABC):
    ATTRIBUTE_NAMES = ['name', 'class']

    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    @classmethod
    def get_attribute_names(cls):
        return cls.ATTRIBUTE_NAMES

    def get_attributes(self):
        return self.attributes

    # BEGIN (write your solution here)
    @abstractmethod
    def is_valid(self):
        pass
    # END
