
def is_palindrome(n):
	return str(n) == str(n)[::-1]

palindromes = []

for i in range(100,1000):
	for j in range(100,1000):
		k = i*j
		if is_palindrome(k):
			palindromes.append(k)

print max(palindromes)