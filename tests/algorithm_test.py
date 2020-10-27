from collections import namedtuple
import unittest
from pkg_resources import resource_stream
from algorithms import ALGORITHMS
from algorithms.algorithm import Algorithm


TestData = namedtuple('TestData', ['name', 'text', 'substring', 'expected'])


def load_texts(filename):
    with resource_stream(__name__, filename) as file:
        return file.read().decode('utf-8')


def load_answers(filename):
    return list(map(int, load_texts(filename).split()))


PROVERB = load_texts('test texts/proverb.txt')
SEQUENCE = load_texts('test texts/large_sequence.txt')
VOYNA_I_MIR = load_texts('test texts/voyna_i_mir_tom_1.txt')
ANSWER_KNYAZ = load_answers('test answers/knyaz_answer.txt')
ANSWER_ADREY = load_answers('test answers/Andrey_answer.txt')

TESTS = [
    TestData('begin', PROVERB, 'You', [0]),
    TestData('end', PROVERB, 'eggs', [48]),
    TestData('e', PROVERB, 'e',
             [13, 20, 22, 35, 45, 48]),
    TestData('князь', VOYNA_I_MIR, 'князь', ANSWER_KNYAZ),
    TestData('Андрей', VOYNA_I_MIR, 'Андрей', ANSWER_ADREY),
    TestData('corona', SEQUENCE, 'ACAATTAATTGCCAGGAACCTAA', [28553])
]


class TestAlgorithms(unittest.TestCase):

    def test_algorithm_is_algorithm(self):
        for algorithm in ALGORITHMS:
            self.assertIsInstance(algorithm(), Algorithm)

    def test_usual(self):
        for test in TESTS:
            for alg in ALGORITHMS:
                actual = alg.findall(test.substring, test.text)
                self.assertEqual(actual, test.expected,
                                 f'Error in {test.name} with {alg.name()}')


if __name__ == '__main__':
    unittest.main()
