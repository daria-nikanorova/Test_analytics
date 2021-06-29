from refrigerator import WelfordStd, Stream
import resource


stream = Stream(port=12, host=88)
mr_welford = WelfordStd()


while stream.has_next():
    value = stream.next_value()
    mr_welford.next_value(value)
    welford_std = mr_welford.standard_deviation()
    welford_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
    print(f'Standard deviation = {welford_std}\n'
          f'Used {welford_memory} Mb')
