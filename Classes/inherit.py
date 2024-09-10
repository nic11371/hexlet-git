class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        super().inc(amount)
        self.value = min(self.value, self.limit)


counter = LimitedCounter(limit=10)
counter.inc()
counter.inc(7)
print(counter.value)  # 8
counter.dec(10)
print(counter.value)  # 0
counter.inc(7)
counter.inc(7)
print(counter.value)  # 10