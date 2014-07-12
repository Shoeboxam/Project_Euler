#!/usr/bin/python

def check(x):
	product = str(x)
	length = len(product)
	index = 0
	while index <= (length/2) and product[index] == product[(length-1)-index]:
		index += 1
		if index == int(length/2):
			palindromes.append(x)


palindromes = []
val_top = 999
val_bot = 100
for a in range(val_bot, val_top, 1):
	for b in range(val_bot, val_top, 1):
		check(a * b)

			

print '~~~~~~~~~'
print max(palindromes)

#print '~~~~~~~~~'
#print palindromes
