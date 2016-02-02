import itertools

digits = ['0','1','2','3','4','5','6','7','8','9']

lex1 = []

for subset in itertools.permutations(digits, len(digits)):
	m = "".join(subset)
	lex1.append(m)

print sorted(lex1)[1000000-1]
print sorted(lex1)[1000000]
print sorted(lex1)[1000000+1]
