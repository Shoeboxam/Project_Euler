#!/usr/bin/python

zone = 5415423 		#configurable input
store = [ 1, 2 ]	#starter values
i = 1
total = 2

while max(store) <= zone: 				#continue finding fib numbers until zone is reached
	store.append(store[i] + store[i-1])	#calc fib number and add to end of list
	i += 1
	if not (store[i] % 2):				#check if number is even before adding to total
		total += store[i]

print total

print '-----------'



#def fibonacci(n):
#	if n > 1:
#		return fibonacci(n-1) + fibonacci(n-2)
#	else:
#		return 1
		
#print fibonacci(300)
