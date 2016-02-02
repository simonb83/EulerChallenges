import time

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


def in_primes(k):
	i = 0
	while primes[i] <= k:
		if primes[i] == k:
			return True
		i += 1
	return False

start_time = time.time()

#Get primes up to 2000000
n = 87400
primes = sieve_for_primes_to(n)
b_values = sieve_for_primes_to(1000)

for i in range(len(b_values)):
	b_values.append(-1*b_values[i])

consec_primes = {}
current_max = 0
a_max = 0
b_max = 0

max_val = 1000
min_val = -1000

for a in range(min_val+1,max_val,2):
	for j in range(len(b_values)):
		b = b_values[j]
		n = 0
		count = 0
		while in_primes(n**2 + a*n + b):
			n += 1
		if n > current_max:
			a_max = a
			b_max = b
			current_max = n

print a_max*b_max

print("--- %s seconds ---" % (time.time() - start_time))