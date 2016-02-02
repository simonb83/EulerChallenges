strings = []

strings.append('08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'.split())
strings.append('49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'.split())
strings.append('81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'.split())
strings.append('52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'.split())
strings.append('22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'.split())
strings.append('24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'.split())
strings.append('32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'.split())
strings.append('67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'.split())
strings.append('24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'.split())
strings.append('21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'.split())
strings.append('78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'.split())
strings.append('16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'.split())
strings.append('86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'.split())
strings.append('19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'.split())
strings.append('04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'.split())
strings.append('88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'.split())
strings.append('04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'.split())
strings.append('20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'.split())
strings.append('20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'.split())
strings.append('01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'.split())

matrix = []

for i in range(len(strings)):
	for j in range(len(strings[i])):
		strings[i][j] = int(strings[i][j])
	matrix.append(strings[i])

maximum = 0
diff = 4

#First check rows
for i in range(len(matrix)):
	for j in range(0,len(matrix[i])-4):
		product = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
		if product > maximum:
			maximum = product

#Then check rows
for i in range(len(matrix)-4):
	for j in range(0,len(matrix)):
		product = matrix[j][i]*matrix[j][i+1]*matrix[j][i+2]*matrix[j][i+3]
		if product > maximum:
			maximum = product

#Check diagonals from left to right

diags1 = []

for i in range(0,20):
	j = 0
	temp = []
	for x in range(i,20):
		temp.append(matrix[j][x])
		j += 1
	diags1.append(temp)

for i in range(0,20):
	j = 0
	temp = []
	for x in range(i,20):
		temp.append(matrix[x][j])
		j += 1
	diags1.append(temp)

#Check diagonals from right to left

#reverse matrix
reversed_matrix = []

for i in range(len(matrix)):
	reversed_matrix.append(list(reversed(matrix[i])))

for i in range(0,20):
	j = 0
	temp = []
	for x in range(i,20):
		temp.append(reversed_matrix[j][x])
		j += 1
	diags1.append(temp)

for i in range(0,20):
	j = 0
	temp = []
	for x in range(i,20):
		temp.append(reversed_matrix[x][j])
		j += 1
	diags1.append(temp)

diags2 = []

for i in range(len(diags1)):
	if len(diags1[i]) >= 4:
		diags2.append(diags1[i])

for i in range(len(diags2)):
	#Get length of list
	length = len(diags2[i])
	for j in range(0,length-4):
		product = diags2[i][j]*diags2[i][j+1]*diags2[i][j+2]*diags2[i][j+3]
		if product > maximum:
			maximum = product

print maximum

