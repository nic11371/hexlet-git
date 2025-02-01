class Application:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    def run(self, text):
        return self.sanitizer.sanitize(text)
