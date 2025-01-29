class CalcLogger:
    # BEGIN (write your solution here)
    def __init__(self, calc):
        self.calc = calc

    prints = []

    def add(self, num):
        x = self.calc.add(num)
        self.prints.append(f"Первое число: {self.calc.acc} Второе число: {num} Сумма: {x.acc}")
        return self.__class__(x)

    def sub(self, num):
        x = self.calc.sub(num)
        self.prints.append(f"Первое число: {self.calc.acc} Второе число: {num} Разность: {x.acc}")
        return self.__class__(x)

    def mul(self, num):
        x = self.calc.mul(num)
        self.prints.append(f"Первое число: {self.calc.acc} Второе число: {num} Результат: {x.acc}")
        return self.__class__(x)

    def result(self):
        print('\n'.join(self.prints))
        self.prints.pop()
        x = self.calc
        return x.acc
    # END
