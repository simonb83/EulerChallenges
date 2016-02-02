import math

n = 600851475143

factors = []

initial = 2

while n > 1:
	while n % initial == 0:
		factors.append(initial)
		n = n/initial
	initial += 1

largest_prime_factor = max(factors)

print largest_prime_factor


