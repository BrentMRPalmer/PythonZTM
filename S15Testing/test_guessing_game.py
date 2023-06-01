# Test Guess

import unittest
import guessing_game2

class TestGame(unittest.TestCase):
	def test_input_correct(self):
		result = guessing_game2.run_guess(5, 5)
		self.assertTrue(result)

	def test_input_wrong_guess(self):
		result = guessing_game2.run_guess(5, 2)
		self.assertFalse(result)

	def test_input_wrong_number(self):
		result = guessing_game2.run_guess(11, 2)
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()