import string

file = open('/Users/simonbedford/Documents/Coding/euler/names.txt','r')

s = string.ascii_uppercase
scores = {}

for j in range(len(s)):
	scores[s[j]] = j+1

def score(name):
	sc = 0
	for i in range(len(name)):
		sc += scores[name[i]]
	return sc

n = ""

for line in file:
	n += line.strip()

names = n.split(',')

for i in range(len(names)):
	names[i] = names[i].replace('"','')

names = sorted(names)

s = string.ascii_uppercase
scores = {}

for j in range(len(s)):
	scores[s[j]] = j+1

name_scores = {}

#Now we can loop through all names

for i in range(len(names)):
	name_scores[names[i]] = score(names[i])*(i+1)

total = 0
for value in name_scores.itervalues():
	total += value

print total
	