class Counter:
    def __init__(self, value=0):
        self.value = value if value > 0 else 0

    def inc(self, delta=1):
        return Counter(max(self.value + delta, 0))

    def dec(self, delta=1):
        return self.inc(-delta)


c = Counter()
print(c.inc().inc(5).value)  # 4

# Старый экземпляр не должен изменяться
d = c.inc(100)
print(d.dec().value)  # 99

forty_two = Counter(-42)
print(forty_two.value)  # 42
