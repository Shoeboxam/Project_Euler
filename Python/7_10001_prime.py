#!/usr/bin/python

def input_validated():
	while True:
		try:
			zone = int(raw_input("Int Zone: "))
		except ValueError:
			print("Must be an integer")
			continue
		else: 
			break

	return zone


def isprime(attempt):
	check = 2.0	#start checking for a factor

	while check <= attempt/2.0:	#continue checking until there can be no more factors

		if attempt % check == 0.0:	#if evenly divisible by check
			return False	#divisor found, so it is not prime	

		check += 1
	return True	#divisors could not be found



#main()
zone = 6 #input_validated()
instance = 0
attempt = 0.0
while instance <= zone:
	attempt += 1.0
	if isprime(attempt):
		instance += 1
print attempt


#