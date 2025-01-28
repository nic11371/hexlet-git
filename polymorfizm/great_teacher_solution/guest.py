class Guest:
    def __init__(self):
        self.name = 'Guest'
        # BEGIN
        self.type = 'guest'
        # END

    def get_name(self):
        return self.name

    # BEGIN
    def get_type(self):
        return self.type
    # END
