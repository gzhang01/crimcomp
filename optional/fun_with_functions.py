# George Zhang
# Crimson Comp Optional Assignment
# fun_with_functions.py

##################### HELPER FUNCTIONS #####################
# Finds the greatest common divisor of two numbers
def gcd(a, b):
	smaller, larger = min(a, b), max(a, b)
	while larger >= smaller:
		larger = larger - smaller
	if larger == 0: 
		return smaller
	else:
		return gcd (smaller, larger)

# Finds the least common multiple of two numbers
def lcm(a, b):
	return a * b / gcd(a, b)

##################### PROBLEM 1 #####################
# Finds the least common multiple of an arbitrary amount of numbers
def lcm(*args):
	answer = lcm(args[0], args[1])
	for i in args[2:]:
		answer = lcm(answer, i)
	return answer

# Prints out information on what you've spent money on
def spending_tracker(**kwargs):
	total = 0
	string = ""
	for key, value in kwargs.iteritems():
		string = string + "{0}: ${1}\n".format(key, value)
		total = total + value
	return string + "Total: ${0}".format(total)

##################### PROBLEM 2 (and 3) #####################
# Let's say I wrote a checkbook program that has a function that logs a transaction.
# Let's say that some transactions are sketchy and I don't want the program to know
# what I spent my money on. Other transactions, though, should be detailed with the
# name of the company I gave my money to. Logging many transactions at once may use
# the following function:
def log_transaction(*args, **kwargs):
	for i in args:
		print "Sketchy Company: ${0}".format(i)
	for key, value in kwargs.iteritems():
		print "{0}: ${1}".format(key, value)

# This function might be run with the following:
# log_transaction(10, 20, 14, 1000000, CVS = 8, Target = 17, NSTAR = 200)

# OR PERHAPS EVEN THIS:
# sketch = [10, 20, 14, 1000000]
# not_sketch = {'CVS': 8, 'Target': 17, 'NSTAR': 200}
# log_transaction(*sketch, **not_sketch)

##################### PROBLEM 3 AND 4 #####################
def test_gcd():
	if gcd(2, 5) != 1: return False
	if gcd(10, 5) != 5: return False
	if gcd(49, 7) != 7: return False
	if gcd(1071, 462) != 21: return False
	return True

def test_lcm():
	if lcm(2, 5) != 10: return False
	if lcm(7, 14) != 14: return False
	if lcm(100, 30) != 300: return False
	if lcm(72, 91) != 72*91: return False
	return True

def test_lcm_multiple():
	if lcm(2, 5, 3) != 30: return False
	if lcm(2, 5, 3, 7) != 210: return False
	if lcm(4, 6, 9) != 36: return False
	numbers = [15, 21, 77, 100]
	if lcm(*numbers) != 23100: return False
	return True

def test_spending_tracker():
	if spending_tracker(food = 200, entertainment = 300, rent = 250) != "food: $200\nrent: $250\nentertainment: $300\nTotal: $750": return False
	if spending_tracker(noms = 1000, rent = 1) != "noms: $1000\nrent: $1\nTotal: $1001": return False
	monthly_spending = {'sloths': 1000000, 'food': 2}
	if spending_tracker(**monthly_spending) != "food: $2\nsloths: $1000000\nTotal: $1000002": return False
	return True

def run_tests():
	if not test_gcd: print "Failed gcd test"
	elif not test_lcm: print "Failed lcm test"
	elif not test_lcm_multiple: print "Failed multiple lcm test"
	elif not test_spending_tracker(): print "Failed spending tracker"
	else: print "Passed all tests"

run_tests()