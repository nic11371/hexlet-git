from HTMLElement import HTMLElement


# BEGIN (write your solution here)
class HTMLPairElement(HTMLElement):

    def get_text_content(self):
        return self.body

    def set_text_content(self, data):
        self.body = data

    def __str__(self):
        attr = self._stringify_attributes()
        body = self.get_text_content()
        tag = self.get_tag_name()
        return f"<{tag}{attr}>{body}</{tag}>"
# END
