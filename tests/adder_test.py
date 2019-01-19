from unittest import TestCase
from adder import simple_add

class AdderTestCase(TestCase):

    def test_add(self):
        assert 11 == simple_add(5,6)
        assert 0 == simple_add(5,-5)
