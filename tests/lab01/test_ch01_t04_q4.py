import itertools
import sys
import unittest
from unittest.mock import patch

from lab.lab01.ch01_t04_q4 import main, is_right_angle
from tests.unit_test_helper.console_test_helper import MyOutput


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.my_stdout = MyOutput()
        self.original_stdout = sys.stdout
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_false(self):
        user_input = ['2', '3', '4']
        for combination in itertools.permutations(user_input, 3):
            with patch('builtins.input', side_effect=combination):
                main()
        self.assertEqual("The triangle is not a right-angle triangle.\n" * 6, str(self.my_stdout))

    def test_true(self):
        user_input = ['4.5', '7.5', '6']
        for combination in itertools.permutations(user_input, 3):
            with patch('builtins.input', side_effect=combination):
                main()
        self.assertEqual("The triangle is a right-angle triangle.\n" * 6, str(self.my_stdout))

    def test_is_right_angle_true(self):
        user_input = [3, 4, 5]
        for combination in itertools.permutations(user_input, 3):
            self.assertTrue(is_right_angle(combination[0], combination[1], combination[2]))

    def test_is_right_angle_false(self):
        user_input = [2, 3, 4]
        for combination in itertools.permutations(user_input, 3):
            self.assertFalse(is_right_angle(combination[0], combination[1], combination[2]))

    def test_invalid(self):
        user_input = ['1', '2', "a"]
        for combination in itertools.permutations(user_input, 3):
            with self.assertRaises(SystemExit) as cm:
                with patch('builtins.input', side_effect=combination):
                    main()
            self.assertEqual(-1, cm.exception.code)
        self.assertEqual("Invalid input!\n" * 6, str(self.my_stdout))


if __name__ == '__main__':
    unittest.main()
