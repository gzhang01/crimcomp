(# A1_Zhang_George.py
# Crimson Tech Comp Assignment 1
# George Zhang

from collections import Counter

# Takes a string and swaps most common letter with least common letter
def swapchars(string):
	counter = Counter(string)
	# Finds most and least common letter in string
	for i in range(len(counter)):
		most = counter.most_common()[i][0]
		if most.isalpha():
			break
	for i in range(1, len(counter)):
		least = counter.most_common()[-i][0]
		if least.isalpha():
			break
	# Constructs string to be returned
	ret = ""
	for c in string:
		if c == most: ret += least
		elif c == least: ret += most
		else: ret += c
	return ret

# Takes a number n and an arbitrary number of strings and concatenates the 
# longest n strings. If n is -1, all strings are concatenated. If n > total
# number of strings, all strings are concatenated.
def sortcat(n, *strs):
	# Creates and sorts string arguments based on length (longest first)
	strlist = list(strs)
	strlist.sort(key = len, reverse = True)
	ret = ""
	# Concatenates first n elements or all elements of list based on value of n
	for i in range(n if n != -1 and n < len(strlist) else len(strlist)):
		ret += strlist[i]
	return ret

# Blue's Clues / Booze #nomnom #turnup
# Opens states.txt and indexes contents into dictionary
abbrev = {}
with open('states.txt', 'r') as f:
	for line in f:
		# Assumes all lines are of form STATE,ABB
		datum = line.split(',')
		abbrev[datum[1][:2]] = datum[0]

# Takes in a state abbreviation and returns full name of state
def find_state(abb):
	return abbrev[abb] if abb in abbrev else "State not found!"

print find_state('PA')

# Takes in state name and returns its abbreviation
def find_abbrev(state):
	for abb in abbrev:
		if abbrev[abb] == state:
			return abb
	return "State not found!"

print find_abbrev("Nebraska")

# If Blue had to ship wine to several states, she could write a for loop that
# cycles through all the states she had to ship wine to and call my function
# every time. If Blue doesn't know how to code, then I could edit my function
# to take a list of states and cycle through the list, creating a list of 
# abbreviations to return

# But Blue should learn to code


