import itertools

def divisors(n):
	divs = [1]
	count = 2
	i = 2
	while i < n:
		if n % i == 0:
			divs.append(i)
		i += 1
	return divs


#Find all abundant numbers under X
x = 28123

abundant = []
abundant_sums = {}

for i in range(1,x):
	abundant_sums[i] = False
	if sum(divisors(i)) > i:
		abundant.append(i)

for i in range(len(abundant)):
	for j in range(i,len(abundant)):
		m = abundant[i] + abundant[j]
		if m < x:
			abundant_sums[m] = True
		else:
			break

total = 0

for i in range(1,x):
	if not abundant_sums[i]:
		total += i

print total
