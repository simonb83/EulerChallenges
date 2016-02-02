

def divisors(n):
	divs = [1]
	count = 2
	i = 2
	while i < n:
		if n % i == 0:
			divs.append(i)
		i += 1
	return divs

#Calculate divisors and d for each number under 10000

result = {}

for i in range(1,10001):
	result[i] = sum(divisors(i))

amicable = []

for i in range(1,10001):
	a = result[i]
	if a in result:
		b = result[a]
		if b == i and i != a:
			if a not in amicable:
				amicable.append(a)
			if i not in amicable:
				amicable.append(i)

print amicable
print sum(amicable)