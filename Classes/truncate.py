class Truncater():
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **options):
        self.options = {**self.OPTIONS, **options}

    def truncate(self, text, **options):
        current_options = {**self.options, **options}
        if len(text) <= current_options['length']:
            return text
        substr = text[:current_options['length']]
        return f"{substr}{current_options['separator']}"


# truncater = Truncater()

# print(truncater.truncate('one two'))  # one two

# print(truncater.truncate('one two', length=6))  # one tw...

# print(truncater.truncate('one two', separator='!'))  # one tw...

# truncater2 = Truncater(length=6, separator='*')
# print(truncater2.truncate('one two'))  # one tw*


def test_truncate():
    truncater = Truncater()
    assert truncater.truncate('one two') == 'one two'
    assert truncater.truncate('one two', length=6) == 'one tw...'
    assert truncater.truncate('one two', separator='.') == 'one two'
    assert truncater.truncate('one two', length=3) == 'one...'

    truncater = Truncater(length=3)
    assert truncater.truncate('one two') == 'one...'
    assert truncater.truncate('one two', separator='!') == 'one!'
    assert truncater.truncate('one two') == 'one...'
    assert truncater.truncate('one two', length=7) == 'one two'


test_truncate()
