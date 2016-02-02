import time

start_time = time.time()

def sieve_for_primes_to(n):
    #Set initial size to floor of n/2
    size = n // 2
    #Initialize a sieve with all 1s
    sieve = [1]*size
    #The limit is defined by the square root of n
    limit = int(n**0.5)

    for i in range(1,limit):
        #If 
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

# def skip(n):
# 	return str(n)[-1] == '5'

# primes = [2]

# k = 10001
# m = 3

# while len(primes) < k:

# 	is_prime = True

# 	for i in range(len(primes)):
# 		if m % primes[i] == 0:
# 			is_prime = False
# 			break

# 	if is_prime:
# 		primes.append(m)

# 	m += 2

# print primes[-1]

n = 100000
while True:
	primes = sieve_for_primes_to(n)
	if len(primes) >= 10001:
		print primes[10000]
		break
	n += 100000

print("--- %s seconds ---" % (time.time() - start_time))




