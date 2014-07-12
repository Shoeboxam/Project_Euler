#!/usr/bin/python

#Project Euler
#Shoeboxam
zone = 893782


total = 0

for three in range(0, zone, 3):
	total += three
	
for five in range(0, zone, 5):
	total += five
	
for fifteen in range(0, zone, 15):
	total -= fifteen
	
print total
print '----------'
