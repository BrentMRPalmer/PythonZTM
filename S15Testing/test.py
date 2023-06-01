# Test
# py -m unittest -v 
# to run all tests at once

import unittest
import main

class TestMain(unittest.TestCase):
	def setUp(self):
		print("About to test a function")
	def test_do_stuff(self):
		'''comment'''
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'sfdjks'
		result = main.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, "Please Enter Number")

	def test_do_stuff4(self):
		test_param = ''
		result = main.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def tearDown(self):
		print("Cleaning up")

# Always called unittest.main(), even if the tested file has a different name
if __name__ == '__main__':
	unittest.main()
