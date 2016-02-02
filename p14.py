import time
import operator


start_time = time.time()

length_list = {}


def next_num(n):
	if n % 2 == 0:
		return n/2
	else:
		return (3*n + 1)


def seq_length(n):
	if n == 1:
		return 1
	elif n in length_list:
		return length_list[n]
	else:
		return (1+seq_length(next_num(n)))

for i in range(1,1000000):
	length_list[i] = seq_length(i)
	# print "n: %s, length: %s" % (i,length_list[i])

maxx = max(length_list.values())
key = [x for x,y in length_list.items() if y ==maxx][0]

print key
print length_list[key]

print("--- %s seconds ---" % (time.time() - start_time))