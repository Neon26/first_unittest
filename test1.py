from unittest import TestCase, main
from wbsq import zero_number

array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
array3 = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
array4 = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
array5 = [0, 0]
array6 = [0]
array7 = []


class ZeroAtEnd(TestCase):
    def test_1(self):
        self.assertEqual(zero_number(array1), [1, 3, 12, 0, 0])

    def test_2(self):
        self.assertEqual(zero_number(array2),[1, 7, 8, 10, 12, 4, 0, 0, 0, 0])

    def test_3(self):
        self.assertEqual(zero_number(array3),[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

    def test_4(self):
        self.assertEqual(zero_number(array4),[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_5(self):
        self.assertEqual(zero_number(array5), [0, 0])

    def test_6(self):
        self.assertEqual(zero_number(array6), [0])

    def test_7(self):
        self.assertEqual(zero_number(array7), [])


