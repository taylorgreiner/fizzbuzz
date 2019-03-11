'''
FizzBuzz provides methods developed for the Fizz Buzz Kata at http://agilekatas.co.uk/katas/fizzbuzz-kata
'''

class FizzBuzz():

	'''
	Feature1 takes a number and returns fizz for multiples of 3, buzz for multiples of 5 and fizz buzz for
	numbers that are multiples of 3 and 5
	'''
	def feature1(self, num):
		if num % (5 * 3) == 0:
			return "fizz buzz"
		elif num % 5 == 0:
			return "buzz"
		elif num % 3 == 0:
			return "fizz"
		else:
			return num

	'''
	Feature2 takes the same parameters as feature1 and adds multiples of 7 to the game. For multiples of 7
	it returns pop, fizz pop for multiples of 3 and 7, buzz pop for multiples of 5 and 7, and fizz buzz pop
	for multiples of 3 and 5 and 7.
	'''

	def feature2(self, num):
		if num % (3 * 5 * 7) == 0:
			return "fizz buzz pop"
		elif num % (5 * 7) == 0:
			return "buzz pop"
		elif num % (7 * 3) == 0:
			return "fizz pop"
		elif num % (5 * 3) == 0:
			return "fizz buzz"
		elif num % 7 == 0:
			return "pop"
		elif num % 5 == 0:
			return "buzz"
		elif num % 3 == 0:
			return "fizz"
		else:
			return num

	'''
	Custom allows a user to provide their own substitution to the game and return a word for multiples of the
	supplied number.
	'''

	def custom(self, num, sub_num, sub_word):
		if num % sub_num == 0:
			return sub_word
		else:
			return num

	'''
	Linked allows a user to play Fizz Buzz, however the user supplies their own 2 numbers and custom words for
	each of the multiples.
	'''

	def linked(self, num, sub_num_1, sub_word_1, sub_num_2, sub_word_2):
		if num % (sub_num_1 * sub_num_2) == 0:
			return sub_word_1 + " " + sub_word_2
		elif num % sub_num_2 == 0:
			return sub_word_2
		elif num % sub_num_1 == 0:
			return sub_word_1
		else:
			return num