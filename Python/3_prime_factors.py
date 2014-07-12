#!/usr/bin/python


zone = 54120

elements = []
check=2
while zone > 1:            #until no more factors
	while zone % check == 0: #check if evenly divisible
		elements.append(check)  #add the factor to the list
		zone = zone / check     #remove the factor from the zone
	check = check + 1  #check factors until match is found

print elements
print '---------'
