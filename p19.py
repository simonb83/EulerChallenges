
#Initial
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}

leap = []
sundays = []

def pass_year(day,year):
	# print "start day is %s start year is %s" % (days[day],year)
	#Case 1 year is divisible by 4, but not by 100
	k = 0
	if year % 4 == 0:
		if year % 100 != 0:
			k = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
			leap.append(year)
		#Case 2 year is divisible by 4 and by 100 and by 400
		elif year % 100 == 0 and year % 400 == 0:
			k = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
			leap.append(year)

		else:
			k = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31

	else:
		k = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31	

	for j in range(k):
		day = (day+1) % 7

	return day

def pass_year_2(day,year):
	# print "start day is %s start year is %s" % (days[day],year)
	#Case 1 year is divisible by 4, but not by 100
	k = 0
	if year % 4 == 0:
		if year % 100 != 0:
			k = 29
			leap.append(year)
		#Case 2 year is divisible by 4 and by 100 and by 400
		elif year % 100 == 0 and year % 400 == 0:
			k = 29
			leap.append(year)

		else:
			k = 28

	else:
		k = 28

	d = 0
	#January
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Jan",d,year))
	#February
	d = 0
	for j in range(k):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Feb",d,year))
	#March
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Mar",d,year))
	#April
	d = 0
	for j in range(30):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Apr",d,year))
	#May
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"May",d,year))
	#June
	d = 0
	for j in range(30):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Jun",d,year))
	#July
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Jul",d,year))
	#August
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Aug",d,year))
	#September
	d = 0
	for j in range(30):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Sep",d,year))
	#October
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Oct",d,year))
	#November
	d = 0
	for j in range(30):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Nov",d,year))
	#December
	d = 0
	for j in range(31):
		d += 1
		day = (day+1) % 7
		if d == 1 and day == 0 and year >= 1901 and year <= 2000:
			sundays.append("%s, %s-%s, %s" % (days[day],"Dec",d,year))

	return day


# def pass_year(year,day):
# 	initial = day
# 	k = 31 + 28 + 31
# 	#days in Jan = 31
# 	for j in range(k):
# 		initial = ((initial+1) % 7)
# 	return initial

day = 0
year = 1900

for j in range(101):
	day = pass_year_2(day,year)
	year += 1

print "%s, %s" % (year-1,days[day])

for day in sundays:
	print day

print len(sundays)