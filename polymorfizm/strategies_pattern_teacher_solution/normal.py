class Normal():
    # BEGIN
    def get_next_step(self, field):
        for i in reversed(range(len(field))):
            row = field[i]
            if None in row:
                return [i, row.index(None)]
        return []
    # END
