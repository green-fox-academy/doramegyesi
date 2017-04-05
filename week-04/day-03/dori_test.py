import unittest
from dori_work import Apples

class TestApples(unittest.TestCase):
    def test_get_apple(self):
        my_object = Apples()
        my_object.get_apple()
        self.assertEquals(my_object.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()
