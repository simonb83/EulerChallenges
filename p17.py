
singles = {0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
special = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
hundreds = {1:'hundred'}
thousand = {1: 'thousand'}

def split_number(n):
	if len(str(n)) == 1:
		return [0,0,0,n]
	elif len(str(n)) == 2:
		return [0,0,int(str(n)[0]),int(str(n)[1])]
	elif len(str(n)) == 3:
		return [0,int(str(n)[0]),int(str(n)[1]),int(str(n)[2])]
	elif len(str(n)) == 4:
		return [int(str(n)[0]),int(str(n)[1]),int(str(n)[2]),int(str(n)[3])]

def count_letters(lis):
	s = 0

	#for thousands
	if lis[0] > 0:
		s += len(singles[lis[0]]) + len(thousand[1])

	#hundreds
	if lis[1] > 0:
		s += len(singles[lis[1]]) + len(hundreds[1])

	#and
	if lis[1] > 0 and (lis[2] > 0 or lis[3] > 0):
		s += 3
	
	#teens
	if lis[2] == 1 and lis[3] > 0:
		digits = int(str(lis[2])+str(lis[3]))
		s += len(special[digits])

		return s

	#ten
	if lis[2] == 1 and lis[3] == 0:
		s += len(tens[1])

	#twenty - ninety
	if lis[2] > 1:
		s += len(tens[lis[2]])

	#units
	if lis[3] > 0:
		s += len(singles[lis[3]])

	return s

sum1 = 0
#First twenty numbers
for i in range(1,1001):
	sum1 += count_letters(split_number(i))


# print count_letters(split_number(127))
# print len("one hundred and twenty seven".replace(" ", ""))

print sum1