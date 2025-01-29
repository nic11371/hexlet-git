class Easy:
    def __init__(self, field):
        self.field = field

    def next_step(self):
        for row_index, row in enumerate(self.field):
            for col_index, item in enumerate(row):
                if item is None:
                    return 'computer', row_index, col_index
