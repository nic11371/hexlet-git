from polymorfizm.strategies_pattern_teacher_solution.easy import Easy
from polymorfizm.strategies_pattern_teacher_solution.normal import Normal


class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN
        if level == 'easy':
            self.strategy = Easy()
        if level == 'normal':
            self.strategy = Normal()

    def go(self, row=None, col=None):
        if row is None and col is None:
            row, col = self.strategy.get_next_step(self.field)
            self.field[row][col] = 'AI'
            return self.is_winner('AI')

        self.field[row][col] = 'Player'
        return self.is_winner('Player')

    def is_winner(self, type):
        horizontal = self.field
        vertical = list(map(list, zip(*horizontal)))
        diagonal1 = [self.field[0][0], self.field[1][1], self.field[2][2]]
        diagonal2 = [self.field[2][0], self.field[1][1], self.field[0][2]]

        for row in horizontal:
            if self.has_player_placed_all_the_marks(row, type):
                return True

        for column in vertical:
            if self.has_player_placed_all_the_marks(column, type):
                return True

        if self.has_player_placed_all_the_marks(diagonal1, type):
            return True
        if self.has_player_placed_all_the_marks(diagonal2, type):
            return True

        return False

    def has_player_placed_all_the_marks(self, row, type):
        return all(value == type for value in row)
# END
