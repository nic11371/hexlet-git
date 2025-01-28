class User:
    def __init__(self, name):
        self.name = name
        # BEGIN
        self.type = 'user'
        # END

    def get_name(self):
        return self.name

    # BEGIN
    def get_type(self):
        return self.type
    # END
