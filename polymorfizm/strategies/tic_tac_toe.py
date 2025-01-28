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

    def gorizontal(self, res):
        one = self.field[0][0] == self.field[0][1] == self.field[0][2] == res
        two = self.field[1][0] == self.field[1][1] == self.field[1][2] == res
        three = self.field[2][0] == self.field[2][1] == self.field[2][2] == res
        return one or two or three

    def vertical(self, res):
        one = self.field[0][0] == self.field[1][0] == self.field[2][0] == res
        two = self.field[0][1] == self.field[1][1] == self.field[2][1] == res
        three = self.field[2][0] == self.field[2][1] == self.field[2][2] == res
        return one or two or three

    def diagonal(self, res):
        one = self.field[0][0] == self.field[1][1] == self.field[2][2] == res
        two = self.field[0][2] == self.field[1][1] == self.field[2][0] == res
        return one or two

    def is_winner(self, is_res):
        return self.gorizontal(is_res) or \
            self.vertical(is_res) or self.diagonal(is_res)

    def go(self, row=None, col=None):
        level = self.levels[self.level]
        if row is None or col is None:
            computer, row_index, col_index = level.next_step()
            self.field[row_index][col_index] = computer
            return self.is_winner('computer')
        else:
            self.field[row][col] = self.user
            return self.is_winner('user')


# END

# WIN USER
# #По умолчанию выбран easy уровень.Его можно изменить, передав строку 'normal'
# game = TicTacToe()

# game.go(1, 1)
# # Ход компьютера
# game.go()
#
# game.go(0, 1)
# game.go()
#
# # Метод go возвращает True, если текущий ход победный и False в ином случае
# is_winner = game.go(2, 1)  # True

# WIN COMPUTER

# game = TicTacToe()
# game.go(1, 1)
# game.go()
# game.go(1, 2)
# game.go()
# game.go(2, 2)
# is_winner = game.go()

# WIN COMPUTER NORMAL

game = TicTacToe('normal')
game.go(0, 2)
game.go()
game.go(0, 1)
game.go()
game.go(1, 2)
is_winner = game.go()
print(is_winner)
