#Learning python concepts through mathematical functions

def gcd(a,b):
	"""Calculate the greatest common divisor of a and b,
	where b is not equal to 0.
	
	Returns a when b=0.	
	
	>>> gcd(2,4)
	2
	>>> gcd (10,0)
	10
	>>> gcd (10,5)
	5
	>>> gcd (21,7)
	7
	"""
	
	while b:
		a, b = b, a % b
	return a		
	
if __name__ == '__main__':
    import doctest
    doctest.testmod()
#doctest1
# Run the script without if_main...
# Do doctest through IDLE.

#doctest2
# Run it with if_main...
# If it compiles with no mistake, we're good.    

#unittest
#Run divisor_test.py