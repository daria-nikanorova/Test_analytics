import numpy as np
from refrigerator import WelfordStd
import time
import matplotlib.pyplot as plt


def welford_std(n):
    all_time_result = []
    up = 1
    while up <= n:
        start = time.time()
        std_values = []
        values_lst = np.random.uniform(0, 1, size=up)
        mr_welford = WelfordStd()
        for val in values_lst:
            mr_welford.next_value(val)
            std_value = mr_welford.standard_deviation()
            std_values.append(std_value)
        end = time.time()
        time_result = end - start
        all_time_result.append(time_result)
        up *= 10
    return all_time_result


def numpy_std(n):
    all_time_result = []
    up = 1
    while up <= n:
        start = time.time()
        std_values = []
        input_values = []
        values_lst = np.random.uniform(0, 1, size=up)
        for val in values_lst:
            input_values.append(val)
            std_value = np.std(input_values)
            std_values.append(std_value)
        end = time.time()
        time_result = end - start
        all_time_result.append(time_result)
        up *= 10
    return all_time_result


times_welford_std = welford_std(100000)
times_np_std = numpy_std(100000)


xs = [10 ** i for i in range(len(times_welford_std))]

# image size
plt.figure(figsize=(10, 6))
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['font.size'] = 15

# labels are needed for a legend
plt.plot(xs, times_welford_std, label='Welford std')
plt.plot(xs, times_np_std, label='Numpy std')

plt.title('Welford std vs Numpy std')

# add labels
plt.xlabel('number of randomly taken floats')
plt.ylabel('time, s')

# add legend
plt.legend()

# add grid
plt.grid()

plt.savefig('Welford_numpy_std.png')





