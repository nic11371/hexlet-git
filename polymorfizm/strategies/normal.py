class Normal:
    def __init__(self, field):
        self.field = field

    def go(self):
        for index, row in enumerate(reversed(self.field)):
            for i, item in enumerate(row):
                if item is None:
                    self.field[index][i] = 'computer'
                    return self.field
