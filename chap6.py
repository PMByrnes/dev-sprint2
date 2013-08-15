# Enter your answers for chapter 6 here
# Name: Pat Byrnes (PMByrnes)


# Ex. 6.6
#1: Calling middle with two letters produces just quotation marks.
#Same result for both 1 letter and none.

def first(word):
	return word[0]   #gets the first letter of the string
def last(word):
	return word[-1]  #gets the last letter of the string
def middle(word):
	return word[1:-1] #gets all except the first and last
	
def is_palendrome(word):
	word = str.lower(word)
	if len(word) <=1:
		return 'This is a Palendrome'
	if last(word) != first(word):
		return 'This is not a Palendrome'
	return is_palendrome(middle(word))
	


# Ex 6.8

def MCD(a, b):
	if a == b:
		return 'these are equal'
	elif a < b:
		if b%a == 0:
			return 'The MCD is', a
		while b%a != 0:
			a = a-1
		return 'The MCD is', a
	else:
		if a%b == 0:
			return 'The MCD is', b
		while b%a != 0:
			b = b-1
		return 'The MCD is', b
				