
multiples = []

for i in range(999):
	if (i+1) % 3 == 0 or (i+1) % 5 == 0:
		multiples.append(i+1)

print sum(multiples)