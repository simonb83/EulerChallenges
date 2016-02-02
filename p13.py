import math

file = open('/Users/simonbedford/Documents/Coding/euler/13.txt','r')

def sig_digit(n):
	if len(str(n)) == 1:
		return [0,n]
	else:
		s = str(n)
		return [int(s[:-1]), int(s[-1])]

matrix = []

for line in file:
	
	string = str(line).rstrip()
	split = list(string)

	for i in range(len(split)):
		split[i] = int(split[i])

	matrix.append(split)

# matrix = [list("37107287533902102798797998220837590246510135740250"),list("46376937677490009712648124896970078050417018260538"),list("74324986199524741059474233309513058123726617309629")]

# for i in range(len(matrix)):
# 	for j in range(len(matrix[i])):
# 		matrix[i][j] = int(matrix[i][j])

answer = [0]*50

carry = 0

for j in range(49,0,-1):
	total = 0

	for k in range(len(matrix)):
		total += matrix[k][j]

	[carry,answer[j]] = sig_digit(total+carry)

total = 0

for j in range(len(matrix)):
	total += matrix[j][0]

total += carry
answer[0] = total

print answer
string = ''.join(str(e) for e in answer)
answer = string[0:10]

print answer

