from polymorfizm.strategies.easy import Easy
from polymorfizm.strategies.normal import Normal


class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN (write your solution here)
        self.user = 'user'
        self.computer = 'computer'
        self.level = level
        self.levels = {
            'easy': Easy(self.field),
            'normal': Normal(self.field)
        }

    def gorizontal(self):
        one = self.field[0][0] == self.field[0][1] == self.field[0][2] == 'user'
        two = self.field[1][0] == self.field[1][1] == self.field[1][2] == 'user'
        three = self.field[2][0] == self.field[2][1] == self.field[2][2] == 'user'
        return one or two or three

    def vertical(self):
        one = self.field[0][0] == self.field[1][0] == self.field[2][0] == 'user'
        two = self.field[0][1] == self.field[1][1] == self.field[2][1] == 'user'
        three = self.field[2][0] == self.field[2][1] == self.field[2][2] == 'user'
        return one or two or three

    def diagonal(self):
        one = self.field[0][0] == self.field[1][1] == self.field[2][2] == 'user'
        two = self.field[0][2] == self.field[1][1] == self.field[2][0] == 'user'
        return one or two

    def go(self, row=None, col=None):
        level = self.levels[self.level]
        if row is None or col is None:
            level.go()
            if self.gorizontal() or self.vertical() or self.diagonal():
                return True
            return False
        self.field[row][col] = self.user
        if self.gorizontal() or self.vertical() or self.diagonal():
            return True
        else:
            return False


# END
# По умолчанию выбран easy уровень. Его можно изменить, передав строку 'normal'
game = TicTacToe()

# Если переданы аргументы, то ходит игрок. Первый аргумент — строка, второй — столбец.
game.go(1, 1)
# Ход компьютера
game.go()

game.go(0, 1)
game.go()

# Метод go возвращает True, если текущий ход победный и False в ином случае
is_winner = game.go(2, 1)  # True
print(is_winner)
