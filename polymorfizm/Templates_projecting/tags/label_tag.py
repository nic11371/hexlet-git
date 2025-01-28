# BEGIN (write your solution here)
class LabelTag:
    def __init__(self, submit, input_tag):
        self.submit = submit
        self.input_tag = input_tag

    def render(self):
        return f"<label>{self.submit}{self.input_tag.render()}</label>"

    def __str__(self):
        return self.render()
# END
