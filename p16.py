import time
import math

def sig_digit(n):
	if len(str(n)) == 1:
		return [0,n]
	else:
		s = str(n)
		return [int(s[:-1]), int(s[-1])]

def multiply(n,li):
	carry = 0
	for j in range(len(li)-1,0,-1):
		[carry,li[j]] = sig_digit(li[j]*n + carry)

	final = carry + li[0]*n

	if len(str(final)) == 1:
		li[0] = final
	else:
		[c,d] = sig_digit(final)
		li[0] = d
		li.insert(0,c)
	return li



answer = [1]

start_time = time.time()

for i in range(100000):
	answer = multiply(2,answer)

string = ''.join(str(e) for e in answer)
print string


print("--- %s seconds ---" % (time.time() - start_time))