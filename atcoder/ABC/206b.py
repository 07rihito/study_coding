n = int(input())

is_loop = True
total = 0
day = 1
while is_loop:
	total += day
	if n <= total:
		break
	day += 1

print(day)
