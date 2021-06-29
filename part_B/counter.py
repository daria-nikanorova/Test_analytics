# counter.py

class Counter:
    def __init__(self):
        self.value = 0

    def update(self, new_value):
        local = self.value
        local += new_value
        self.value = local
