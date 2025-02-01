from lxml import etree
from classes_professional.Decorator.Sanitizer import Sanitizer
from classes_professional.Decorator.Application import Application


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    # BEGIN (write your solution here)
    def sanitize(self, text):
        text_without_tags = strip_tags(text)
        text_without_space = self.sanitizer.sanitize(text_without_tags)
        return text_without_space
    # END


sanitizer = Sanitizer()
decorated = SanitizerStripTagsDecorator(sanitizer)
app = Application(decorated)
print(app.run('<p>text<p>'))  # 'text'
print(app.run('  <hr>   another text '))   # 'another text'
