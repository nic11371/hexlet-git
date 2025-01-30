from HTMLPairElement import HTMLPairElement


# BEGIN (write your solution here)
class HTMLDivElement(HTMLPairElement):
    def __init__(self, attributes=None):
        super().__init__(attributes)
        self.body = ""

    def get_tag_name(self):
        return "div"


# END
div = HTMLDivElement({'name': 'div', 'data-toggle': 'true'})
div.get_text_content()
div.set_text_content('Body Text')
div.get_text_content()  # Body Text
print(div)  # => '<div name="div" data-toggle="true">Body Text</div>'
