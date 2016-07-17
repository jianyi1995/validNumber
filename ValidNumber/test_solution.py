from unittest import TestCase
from ValidNumber.validNumber import Solution


class Test(TestCase):
    def test_all_numbers(self):
        solution = Solution()
        self.assertEqual(solution.isNumber("1"), True)
        self.assertEqual(solution.isNumber(""), False)
        self.assertTrue(solution.isNumber("113544566"), True)
