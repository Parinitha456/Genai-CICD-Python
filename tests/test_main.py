# import unittest
# from main import add, subtract  # Import the functions to test

# class TestMathOperations(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-1, 1), 0)
    
#     def test_subtract(self):
#         self.assertEqual(subtract(5, 3), 2)
#         self.assertEqual(subtract(0, 1), -1)

# if __name__ == '__main__':
#     unittest.main()

import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
