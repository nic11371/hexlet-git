from HTMLElement import HTMLElement


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        attributes = set(super().get_attributes())
        type = super().get_attributes()
        attr = set(self.get_attribute_names())
        types = set(self.TYPE_NAMES)

        if attributes - attr:
            return False

        if type.get('type') and type.get('type') in types:
            return True
        return False
    # END
