# main.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from counter import Counter
from task import Task


new_counter = Counter()
values = [2 for _ in range(10)]  # list comprehension is a better way (will not fail with matrices)
tasks = []
for value in values:
    tasks.append(Task(value))
with ThreadPoolExecutor(max_workers=2) as executor:
    for task in tasks:
        executor.submit(new_counter.update, task.execute())
print(new_counter.value)
