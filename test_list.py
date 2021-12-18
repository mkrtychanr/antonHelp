from logging import setLogRecordFactory
import unittest
import list


a = []
b = []
c = []
list.writeToList(a, 'numbers.txt')
list.writeToList(b, 'numbers1.txt')
list.writeToList(c, 'numbers2.txt')

class TestWriteFromFile(unittest.TestCase):

    def test_write(self):
        self.assertEqual(a, [123, 32])
        self.assertEqual(b, [1, 4])
        self.assertEqual(c, [5, 6, 56, 146])

class MathOperationsTest(unittest.TestCase):

    def test_summa(self):
        self.assertEqual(list.sumE(a), 155)
        self.assertEqual(list.sumE(b), 5)
        self.assertEqual(list.sumE(c), 213)

    def test_minimum(self):
        self.assertEqual(list.minE(a), 32)
        self.assertEqual(list.minE(b), 1)
        self.assertEqual(list.minE(c), 5)

    def test_maximum(self):
        self.assertEqual(list.maxE(a), 123)
        self.assertEqual(list.maxE(b), 4)
        self.assertEqual(list.maxE(c), 146)

    def test_pr(self):
        self.assertEqual(list.prE(a), 3936)
        self.assertEqual(list.prE(b), 4)
        self.assertEqual(list.prE(c), 245280)

