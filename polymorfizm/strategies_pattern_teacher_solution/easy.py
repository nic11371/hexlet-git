class Easy():
    # BEGIN
    def get_next_step(self, field):
        for i, row in enumerate(field):
            if None in row:
                return [i, row.index(None)]
        return []
