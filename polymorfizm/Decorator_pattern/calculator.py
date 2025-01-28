class Calculator:
    def __init__(self, acc=0):
        self.acc = acc

    def add(self, num):
        new_acc = self.acc + num
        return self.__class__(new_acc)

    def sub(self, num):
        new_acc = self.acc - num
        return self.__class__(new_acc)

    def mul(self, num):
        new_acc = self.acc * num
        return self.__class__(new_acc)

    def result(self):
        return self.acc
