n = int(input())

def count_div(num):
	if num % 2 != 0:
		return 0
	else:
		num //= 2
		return 1 + count_div(num)

ans = 1
max_count = 0
for i in range(1, n + 1):
	temp = count_div(i)
	if max_count < temp: 
		ans = i
		max_count = temp

print(ans)
	
