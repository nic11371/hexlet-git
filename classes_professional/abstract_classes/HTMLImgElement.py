from classes_professional.abstract_classes.HTMLElement import HTMLElement


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        attributes = set(super().get_attributes())
        attr = set(self.get_attribute_names())

        if not attributes:
            return True
        if attributes - attr:
            return False
        else:
            return True
    # END


img1 = HTMLImgElement({'class': 'rounded', 'src': 'path/to/image'})
print(img1.is_valid())  # True

img2 = HTMLImgElement({'class': 'rounded', 'href': 'path/to/image'})
print(img2.is_valid())  # False


