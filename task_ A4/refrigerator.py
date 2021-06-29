import math


class Stream:

    def __init__(self, host, port):
        self.value = None
        self.host = host
        self.port = port

    def has_next(self):
        try:
            self.value = float(input())
        except ValueError:
            self.value = None
        return True if self.value is not None else False

    def next_value(self):
        if self.value is not None:
            return self.value


class WelfordStd:

    def __init__(self):
        self.n = 0
        self.old_m = 0
        self.new_m = 0
        self.old_s = 0
        self.new_s = 0

    def next_value(self, next_val):
        self.n += 1

        self.new_m = self.old_m + (next_val - self.old_m) / self.n
        self.new_s = self.old_s + (next_val - self.old_m) * (next_val - self.new_m)

        self.old_m = self.new_m
        self.old_s = self.new_s

    def variance(self):
        return self.new_s / (self.n - 1) if self.n > 1 else 0.0

    def standard_deviation(self):
        return math.sqrt(self.variance())
