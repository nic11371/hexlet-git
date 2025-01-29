class CalcLogger:
    # BEGIN
    def __init__(self, calculator):
        self.calculator = calculator
        self._log = []

    def _add_message(self, message):
        self._log.append(message)

    def _get_log(self):
        return self._log

    def add(self, num):
        first_num = self.calculator.acc
        self.calculator = self.calculator.add(num)
        message = f'Первое число: {first_num} Второе число: {num} Сумма: {self.calculator.result()}'
        self._add_message(message)
        return self

    def sub(self, num):
        first_num = self.calculator.acc
        self.calculator = self.calculator.sub(num)
        message = f'Первое число: {first_num} Второе число: {num} Разность: {self.calculator.result()}'
        self._add_message(message)
        return self

    def mul(self, num):
        first_num = self.calculator.acc
        self.calculator = self.calculator.mul(num)
        message = f'Первое число: {first_num} Второе число: {num} Результат: {self.calculator.result()}'
        self._add_message(message)
        return self

    def result(self):
        print('\n'.join(self._get_log()))
        return self.calculator.acc