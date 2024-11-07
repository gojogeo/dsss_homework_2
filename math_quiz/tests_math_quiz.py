import unittest
from math_quiz import Rand_Int, Math_Operator, Math_Operation


class TestMathGame(unittest.TestCase):

    def test_Rand_Int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Rand_Int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Math_Operator(self):
        # TODO
        pass

    def test_Math_Operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (12, 4, '*','12 * 4', 48),
                (50, 10, '-', '50 - 10', 40)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                p, a = Math_Operation(num1, num2, operator)
                self.assertEqual(p, expected_problem)
                self.assertEqual(a, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
