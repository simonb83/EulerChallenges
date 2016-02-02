

def divisors(n):
	count = 2
	i = 2
	while i**2 <= n:
		if n % i == 0:
			count += 2
		i += 1
	return count

new = 0
i = 1

while True:
	new += i

	if divisors(new) > 500:
		break
	i += 1


print new
