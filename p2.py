
i = 1
j = 2

sum = 2

while True:
	
	k = i+j
	i = j
	j = k

	if k <= 4000000 and k % 2 == 0:
		sum += k

	if k > 4000000:
		break

print sum