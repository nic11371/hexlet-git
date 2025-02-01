class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_content(self, body):
        self.body = body

    @classmethod
    def get_params(cls):
        return cls._params

    # BEGIN (write your solution here)
    def __str__(self):
        body = self.body if self.body else ""
        params = self.get_params()
        if params['pair']:
            return f"<{params['name']}>{body}</{params['name']}>"
        return f"<{params['name']}>"
    # END
