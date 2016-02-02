
def divides(n):
	indicator = True
	
	for i in range(20):
		if n % (i+1) != 0:
			indicator = False
			break
	
	return indicator

num = 20

# print divides(10)

while True:
	num += 10

	if divides(num):
		print num
		break