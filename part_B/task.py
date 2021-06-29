# task.py
import time


class Task:
    def __init__(self, value):
        self.status = 'ready'
        self.value = value

    def execute(self):
        new_value = self.value**2
        self.value = new_value
        time.sleep(0.1)
        return self.value
