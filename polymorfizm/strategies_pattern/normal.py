class Normal:
    def __init__(self, field):
        self.field = field

    def next_step(self):
        for row_index in reversed(range(len(self.field))):
            for col_index, item in enumerate(self.field[row_index]):
                if item is None:
                    return 'computer', row_index, col_index
