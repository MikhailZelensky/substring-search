import unittest
from benchmark import Benchmark


class TestUtils(unittest.TestCase):

    def test_correct_init(self):
        Benchmark()

    def test_run(self):
        Benchmark().run()


if __name__ == '__main__':
    unittest.main()
