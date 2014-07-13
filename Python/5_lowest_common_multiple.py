zone = 489 #configurable input


factor_list = []
for input in range(2, zone):#factor all
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
	
#print factor_list #test output
#print '-----'

##retrieve highest frequencies of prime factors
maximum = dict()
for dictionary in factor_list:
	for key in dictionary.iterkeys():
		if key not in maximum.keys() or maximum[key] < dictionary[key]:
			maximum[key] = dictionary[key]
			
#print maximum #test output
#print '-----'


#meld values and frequencies
total = 1
for key in maximum:
	total *= pow(key, maximum[key])
print total
		

print '---------'
