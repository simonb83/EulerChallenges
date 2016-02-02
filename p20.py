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

start_time = time.time()

matrix = [1]

for i in range(1,1001):
	matrix = multiply(i,matrix)

while len(str(matrix[0])) > 1:
	[m,n] = sig_digit(matrix[0])
	matrix[0] = n
	matrix.insert(0,m)

string = ''.join(str(e) for e in matrix)
# print string

print sum(matrix)

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

s = str(math.factorial(1000))
split = list(s)

sum2 = 0

for k in range(len(split)):
	sum2 += int(split[k])

print sum2
print("--- %s seconds ---" % (time.time() - start_time))


