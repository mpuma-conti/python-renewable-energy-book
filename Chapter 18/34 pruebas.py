import unittest

def suma(a, b):
    return a + b

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()