import unittest

from Scoring import FizzBuzz

class FizzBuzzTests(unittest.TestCase):

	#
	# Feature 1 Test Suite
	#

	def test_feat1_Num_1(self):
		self.assertEqual(FizzBuzz().feature1(1), 1)

	def test_feat1_Num_2(self):
		self.assertEqual(FizzBuzz().feature1(2), 2)

	def test_feat1_Num_3(self):
		self.assertEqual(FizzBuzz().feature1(4), 4)

	def test_feat1_Fizz_1(self):
		self.assertEqual(FizzBuzz().feature1(3), "fizz")

	def test_feat1_Fizz_2(self):
		self.assertEqual(FizzBuzz().feature1(9), "fizz")

	def test_feat1_Fizz_3(self):
		self.assertEqual(FizzBuzz().feature1(123), "fizz")

	def test_feat1_Buzz_1(self):
		self.assertEqual(FizzBuzz().feature1(5), "buzz")

	def test_feat1_Buzz_2(self):
		self.assertEqual(FizzBuzz().feature1(20), "buzz")

	def test_feat1_Buzz_3(self):
		self.assertEqual(FizzBuzz().feature1(200), "buzz")

	def test_feat1_FizzBuzz_1(self):
		self.assertEqual(FizzBuzz().feature1(15), "fizz buzz")

	def test_feat1_FizzBuzz_2(self):
		self.assertEqual(FizzBuzz().feature1(45), "fizz buzz")

	def test_feat1_FizzBuzz_3(self):
		self.assertEqual(FizzBuzz().feature1(315), "fizz buzz")

	#
	# Feature 2 Test Suite
	#

	def test_feat2_Num_1(self):
		self.assertEqual(FizzBuzz().feature2(11), 11)

	def test_feat2_Pop_1(self):
		self.assertEqual(FizzBuzz().feature2(7), "pop")

	def test_feat2_Pop_2(self):
		self.assertEqual(FizzBuzz().feature2(28), "pop")

	def test_feat2_Pop_3(self):
		self.assertEqual(FizzBuzz().feature2(77), "pop")

	def test_feat2_FizzPop_1(self):
		self.assertEqual(FizzBuzz().feature2(21), "fizz pop")

	def test_feat2_FizzPop_2(self):
		self.assertEqual(FizzBuzz().feature2(63), "fizz pop")

	def test_feat2_FizzPop_3(self):
		self.assertEqual(FizzBuzz().feature2(126), "fizz pop")

	def test_feat2_BuzzPop_1(self):
		self.assertEqual(FizzBuzz().feature2(35), "buzz pop")

	def test_feat2_BuzzPop_2(self):
		self.assertEqual(FizzBuzz().feature2(70), "buzz pop")

	def test_feat2_BuzzPop_3(self):
		self.assertEqual(FizzBuzz().feature2(140), "buzz pop")

	def test_feat2_FizzBuzzPop_1(self):
		self.assertEqual(FizzBuzz().feature2(105), "fizz buzz pop")

	def test_feat2_FizzBuzzPop_2(self):
		self.assertEqual(FizzBuzz().feature2(210), "fizz buzz pop")

	def test_feat2_FizzBuzzPop_3(self):
		self.assertEqual(FizzBuzz().feature2(315), "fizz buzz pop")

	#
	# Feature 3 Test Suite
	#

	def test_feat3_Custom_1(self):
		self.assertEqual(FizzBuzz().custom(1, 2, "fuzz"), 1)

	def test_feat3_Custom_2(self):
		self.assertEqual(FizzBuzz().custom(2, 2, "fuzz"), "fuzz")

	def test_feat3_Custom_3(self):
		self.assertEqual(FizzBuzz().custom(8, 2, "fuzz"), "fuzz")

	def test_feat3_Linked_1(self):
		self.assertEqual(FizzBuzz().linked(4, 2, "fuzz", 3, "bizz"), "fuzz")

	def test_feat3_Linked_2(self):
		self.assertEqual(FizzBuzz().linked(9, 2, "fuzz", 3, "bizz"), "bizz")

	def test_feat3_Linked_3(self):
		self.assertEqual(FizzBuzz().linked(12, 2, "fuzz", 3, "bizz"), "fuzz bizz")

if __name__ == "__main__":
	unittest.main()