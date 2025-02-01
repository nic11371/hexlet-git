class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_content(self, body):
        self.body = body

    @classmethod
    def get_params(cls):
        return cls._params

    # BEGIN
    def __str__(self):
        # создается через метакласс
        params = type(self).get_params()
        open_tag = f"<{params['name']}>"
        if not params['pair']:
            return open_tag
        close_tag = f"</{params['name']}>"
        body = self.body if self.body else ""

        return f"{open_tag}{body}{close_tag}"
    # END
