import re
import time

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def repeat_sequence(s):
	#start by seeing if last 3 characters repeat
	if s[-4:-1] == 3*s[-1]:
		return s[-1]
	else:
		for i in range(len(s)):
			char = s[i]
			indices = find(s,char)
			#Only do something if the character occurs more than once
			if len(indices) > 1:
				#Initial string
				for j in range(1,len(indices)):
					p1 = s[indices[0]:indices[j]]
					p2 = s[indices[j]:indices[j]+len(p1)]
					if p1 == p2:
						if len(p1) == 1 and s[-1] == p1:
							return p1
						elif len(p1) > 1:
							return p1
	return False

def divide(n,x):
	result = []
	carry = 1
	numerator = 10
	for i in range(x):
		result.append(int(numerator*carry/n))
		carry = numerator*carry % n
		if carry == 0:
			break
	return "".join(map(str, result))

# sequences = {}

start_time = time.time()

# # print divide(811,3000)

# for i in range(1,1000):
# 	# print i
# 	seq = divide(i,3000)
# 	if len(seq) < 20:
# 		sequences[i] = len(seq)
# 	else:
# 		sequences[i] = len(repeat_sequence(seq))
		
# v=list(sequences.values())
# k=list(sequences.keys())

# print k[v.index(max(v))]
# print sequences[k[v.index(max(v))]]
# # for k,v in sequences.items():
# # 	print "N = %s: %s" % (k,v)

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

# for p in (sieve_for_primes_to(1000)):
#     if p%2==0 or p%5==0:
#         continue
#     k = 1
#     while (10**k - 1)%p!=0:
#         k+=1
#     print p,":",k


# print sieve_for_primes_to(1000)
print repeat_sequence(divide(163,1000))
print len(repeat_sequence(divide(163,1000)))


print("--- %s seconds ---" % (time.time() - start_time))