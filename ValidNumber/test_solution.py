from unittest import TestCase
from ValidNumber.validNumber import Solution


class Test(TestCase):
    def test_all_numbers(self):
        solution = Solution()
        self.assertEqual(solution.isNumber(' 1 '), True)
        self.assertEqual(solution.isNumber("1"), True)
        self.assertEqual(solution.isNumber(""), False)
        self.assertTrue(solution.isNumber("113544566"), True)


    def test_dot_numbers(self):

        solution = Solution()
        self.assertEqual(solution.isNumber('0.1'), True)
        self.assertEqual(solution.isNumber('0.1a'), False)



    def test_e_numbers(self):

        solution = Solution()
        self.assertEqual(solution.isNumber('2e10'), True)
        self.assertEqual(solution.isNumber('ae1'), False)
        self.assertEqual(solution.isNumber('1.5e10'), True)
        self.assertEqual(solution.isNumber('223'), True)
