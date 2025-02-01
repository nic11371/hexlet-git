from abc import ABC, abstractmethod


class Enumerable(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

    # BEGIN (write your solution here)
    def max_by(self, fn):
        iterator = self.get_iterator()
        max_sign = max(iterator, key=fn, default=None)
        return max_sign
    # END
