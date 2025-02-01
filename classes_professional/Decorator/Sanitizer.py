class Sanitizer:
    # BEGIN (write your solution here)
    def sanitize(self, text):
        return text.strip()
    # END


base_sanitizer = Sanitizer()
# передаем в обертку объект base_sanitizer
# sanitizer = SanitizerStripTagsDecorator(base_sanitizer)
print(base_sanitizer.sanitize('text   '))  # 'text'
print(base_sanitizer.sanitize(' boom '))  # 'boom'
# base_sanitizer('<p>some text</p>')  ## "some text"
