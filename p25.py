

fib = [1,1]

ind = 2

while True:
	n = fib[ind-1] + fib[ind-2]
	fib.append(n)
	if len(str(n)) == 1000:
		break
	ind += 1

print ind
print fib[ind-1]
print fib[ind]