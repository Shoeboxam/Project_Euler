def square_sum():
	sum = 0
	for value in range(zone+1):
		sum += value * value
	return sum
	
def sum_square():
	sum = 0
	for value in range(zone+1):
		sum += value
	return (sum * sum)
	
	
while True:
	try:
		zone = int(raw_input("Int Zone: "))
	except ValueError:
		print("Must be an integer")
		continue
	else: 
		break

print "Difference: %s" % (sum_square()-square_sum())
