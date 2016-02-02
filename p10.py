import math
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

# initial = {}

n = 5
# max_n = int(math.ceil(math.sqrt(n)))

# for i in range(2,n):
# 	initial[i] = True

# for i in range(2,max_n):
# 	if initial[i]:
# 		for j in range(2,n/i+1):
# 			initial[i*j] = False

# primes = []
# initial_sum = 0

# for k,v in initial.items():
#     if v == True and v<n:
#        primes.append(k)
#        initial_sum += k

# print initial_sum

print sieve_for_primes_to(n)[-1]

print("--- %s seconds ---" % (time.time() - start_time))