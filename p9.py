
[a,b,c] = [0,0,0]

#generate pythagorean tiples, check if they sum to 1000

for diff in range(1,20):

	for m in range(1,20):
		n = m + diff

		a = n**2 - m**2
		b = 2*n*m
		c = n**2 + m**2

		if a+b+c == 1000:
			print [a,b,c]
			print a*b*c
		