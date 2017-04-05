import unittest
from dori_work import *

class TestApples(unittest.TestCase):
    def test_get_apple(self):
        my_object = Apples()
        my_object.get_apple()
        self.assertEquals(my_object.get_apple(), "apple")


class TestSum_stuff(unittest.TestCase):
    def test_sum_all(self):
        new_individual = Sum_stuff([6, 7])
        self.assertEquals(new_individual.sum_all(), 13)


if __name__ == '__main__':
    unittest.main()
