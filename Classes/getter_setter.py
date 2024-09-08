class HourClock:
    def __init__(self, hours=0):
        self.hours = hours

    @property
    def get_hours(self):
        return self.hours
    
    @get_hours.setter
    def set_hours(self, new_hour):
        self.hours = new_hour


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