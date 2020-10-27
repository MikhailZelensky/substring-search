from timeit import timeit
from tests.algorithm_test import TESTS
from algorithms import ALGORITHMS
import matplotlib.pyplot as plt


class Benchmark:

    def __init__(self):
        self.tests = TESTS
        self.n_times = 100

        self.test_time = {}
        for test in self.tests:
            self.test_time[test.name] = {alg.name(): [] for alg in ALGORITHMS}

    def run(self):
        execute = 'alg.search(test.substring, test.text)'
        for alg in ALGORITHMS:
            for test in TESTS:
                for i in range(self.n_times):
                    self.test_time[test.name][alg.name()].append(
                        timeit(execute, globals=locals(), number=1))

    def report(self):
        data = self.test_time
        exp = 1e5
        figure, axes = plt.subplots(len(data), figsize=(15, 30))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(data[test][alg]))
                y_arr = list(map(lambda x: x * exp, data[test][alg]))

                axes[i].scatter(x_arr, y_arr, label=alg)
                axes[i].set_title(test)
                axes[i].set_xlabel('runs')
                axes[i].set_ylabel('time powed %s' % exp)
                axes[i].legend()
        figure.savefig('report.png', format='png')


if __name__ == '__main__':
    benchmark = Benchmark()
    benchmark.run()
    benchmark.report()
