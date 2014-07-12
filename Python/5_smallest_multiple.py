#!/usr/bin/python
#not functional... will probably end up rewriting this with a better method

zone = 20
factor_list = []

for input in range(zone):#factor all
	check=2
	factors = dict()
	
	while input > 1: #until no more factors
		while input % check == 0:
			if check in factors:
				factors[check] += 1
			else:
				factors.update({check:1})	
			input /= check
		check += 1
	
	factor_list.append(factors)
print factor_list #test output

##calculate repeated primes

instance = [0] * zone

for key in range(zone):
	for dictionary in factor_list:
		try:
			if instance[key] < dictionary[key]:
				instance[key] = dictionary[key]
		except:
			0
	instance[key] += 1
	
#meld dict and repeats
meld = []
for dictionary in factor_list:
	for key in dictionary.iterkeys():
		meld.append(key * instance[key])
print meld

total = 1
for value in meld:
	total *= value
print total
	
		

print '---------'
