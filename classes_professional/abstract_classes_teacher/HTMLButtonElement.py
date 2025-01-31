from HTMLElement import HTMLElement


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        attributes = self.get_attributes()
        names = attributes.keys()
        valid_names = self.get_attribute_names()
        diff = names - set(valid_names)

        return (not diff) \
            and ('type' in attributes) \
            and (attributes['type'] in self.TYPE_NAMES)
    # END


button1 = HTMLButtonElement({'class': 'rounded', 'type': 'button'})
print(button1.is_valid())  # True

button2 = HTMLButtonElement({'class': 'rounded'})
print(button2.is_valid())  # False
