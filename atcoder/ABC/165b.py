x = int(input())

year = 0
deposit = 100
while deposit < x:
	deposit = deposit + deposit // 100 
	year += 1

print(year)
