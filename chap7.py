# Enter your answers for chapter 7 here
# Name: Pat Byrnes (PMByrnes)


# Ex. 7.5
from math import factorial, pi

def estimate_pi(k):
	part1 = (2.0*(2**0.5))/9801  #this gets the part of the equation before the Sigma
	num = factorial(4.0*k) * (1103.0 + 26390.0*k) #numerator
	den = (factorial(k)**4.0) * (396.0**(4.0*k))  #denominator
	rs = (part1 *(num/den))  #equation for right side
	est_pi = 1/rs
	print est_pi
	
"""for some reason I can't get the exact equation to work.
It seems like if I call estimate_pi(0) I'll get roughly pi.
But each number above zero seems to return an exponentially large number,
which makes it difficult to progress on this example."""

# How many iterations does it take to converge?