class HourClock:
    def __init__(self, position=0):
        self.position = position

    @property
    def hours(self):
        return self.position

    @hours.setter
    def hours(self, new):
        self.position = new % 12


clock = HourClock()
print(clock.hours)  # 0
# в начале часовая стрелка всегда на нуле
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 5
print(clock.hours)  # 10
clock.hours += 5
print(clock.hours)  # 3
clock.hours -= 4
print(clock.hours)  # 11
clock.hours = 123
print(clock.hours)  # 3